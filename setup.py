import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="bech32",
    version="1.2.0",
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
    package_data={"bech32": ["py.typed"]},
    install_requires=[],
    python_requires=">=3.5",
    zip_safe=False,  # mypy needs this to be able to find the package
)
