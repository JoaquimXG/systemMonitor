from setuptools import setup

version = {}
with open("monitor/version.py") as fp:
        exec(fp.read(), version)

setup(
    name="SystemMonitor",
    version=version['__version__'],
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
