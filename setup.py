from setuptools import setup
from .monitor import version

setup(
    name="SystemMonitor",
    version=version.version(),
    description="Monitors and logs basic system information",
    author="Joaquim Gomez",
    author_email="info@joaquimgomez.com",
    license="MIT",
    packages=["monitor"],
    install_requires=["psutil", "ping3"],
    zip_safe=False,
    entry_points={
        "console_scripts": ["monitor=monitor.command:main"],
    },
)
