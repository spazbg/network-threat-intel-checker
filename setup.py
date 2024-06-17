from setuptools import setup, find_packages

setup(
    name="network_intel",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
        "psutil",
    ],
    entry_points={
        "console_scripts": [
            "network_intel=network_intel.app:main",
        ],
    },
)
