from setuptools import setup

setup(
    name='pytest-json',
    version='0.0.1',
    author='Tim Copeland',
    license='MIT',
    description='A pytest plugin to generate JSON reports, with ATX support.',
    url='https://github.com/tpc8486/test_guide_pytest_json',
    packages=['pytest_json'],
    install_requires=['pytest'],
    python_requires='>=3.10',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Framework :: Pytest',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'pytest11': [
            'json = pytest_json.plugin',
        ],
    },
)
