import pytest
import os
from datetime import datetime
from tg_pytest_json.report import JSONReport


def pytest_addoption(parser):
    """Add command-line and ini options for JSON reporting."""
    group = parser.getgroup("terminal reporting")
    group.addoption(
        "--json",
        nargs="?",  # Allow optional argument
        dest="json_path",
        const="",   # Default to empty string if no value is provided
        help="Where to store the JSON report (optional). If omitted, a timestamped report will be created at the project root.",
    )
    parser.addini("json_report", "Where to store the JSON report")


def _json_path(config):
    """Determine the JSON report path from CLI option or ini setting."""
    cli_path = config.option.json_path
    ini_path = config.getini("json_report")

    if cli_path:
        return cli_path
    if ini_path:
        return ini_path

    # Auto-generate filename at project root
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    filename = f"{timestamp}_report.json"
    root_dir = config.rootpath if hasattr(config, "rootpath") else os.getcwd()
    return os.path.join(str(root_dir), filename)


@pytest.fixture
def json_report_path(request):
    """Fixture to provide the JSON report path."""
    return _json_path(request.config)


def pytest_configure(config):
    """Configure pytest for JSON reporting."""
    config._json_environment = []
    json_path = _json_path(config)

    if json_path and not hasattr(config, "workerinput"):
        config._json = JSONReport(json_path)
        config.pluginmanager.register(config._json)

    if hasattr(config, "workeroutput"):
        config.workeroutput["json_environment"] = config._json_environment


@pytest.mark.optionalhook
def pytest_testnodedown(node):
    """Handle distributed testing (xdist)."""
    if hasattr(node, "workeroutput"):
        node.config._json_environment = node.workeroutput["json_environment"]


def pytest_unconfigure(config):
    """Unregister the JSON report plugin on pytest exit."""
    if hasattr(config, "_json"):
        config.pluginmanager.unregister(config._json)
        del config._json
