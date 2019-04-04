import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="bech32",
    version="1.1.0",
    description="Reference implementation for Bech32 and segwit addresses.",
    long_description=README,
    long_description_content_type="text/markdown",
    maintainer="fiatjaf",
    maintainer_email="fiatjaf@alhur.es",
    url="https://github.com/fiatjaf/bech32",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["bech32"],
    include_package_data=True,
    install_requires=[],
)
