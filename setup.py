from setuptools import setup

setup(
    name='pytest-json',
    version='0.0.1',
    packages=['pytest_json'],
    install_requires=['pytest', 'ruff'],
    entry_points={
        'pytest11': [
            'json = pytest_json.plugin',
        ],
    },
)
