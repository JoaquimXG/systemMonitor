from setuptools import setup

setup(
    name="Windows System Monitor",
    version="0.1",
    description="Monitors and logs basic system information",
    author="Joaquim Gomez",
    author_email="info@joaquimgomez.com",
    license="MIT",
    packages=["monitor"],
    install_requires=["psutil"],
    zip_safe=False,
    entry_points={
        "console_scripts": ["monitor=monitor.command:main"],
    },
)
