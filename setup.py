#!/usr/bin/env python
# coding=utf-8

import pathlib
from itertools import chain

from setuptools import setup, find_packages

import versioneer

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


tests_require = [
    "deepdiff",
    "flake8",
    "black",
    "hypothesis",
    "mock",
    "pep8-naming",
    "pytest",
    "pytest-flake8",
    "python-rapidjson",
    "rio_cogeo",
]

EXTRAS_REQUIRE = {
    "test": tests_require,
    # If packaging ard/wagl.
    "wagl": ["h5py"],
    # The (legacy) prepare scripts
    "ancillary": ["scipy", "checksumdir", "netCDF4", "gdal"],
}
EXTRAS_REQUIRE["all"] = list(chain(EXTRAS_REQUIRE.values()))

setup(
    name="eodatasets3",
    description="Packaging, metadata and provenance for OpenDataCube EO3 datasets",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(exclude=("tests", "tests.*")),
    package_data={"": ["*.json", "*.yaml"]},
    license="Apache Software License 2.0",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    url="https://github.com/GeoscienceAustralia/eo-datasets",
    install_requires=[
        "attrs",
        "boltons",
        "cattrs",
        "ciso8601",
        "click",
        "jsonschema",
        "numpy",
        "pyproj",
        "rasterio",
        "ruamel.yaml",
        "shapely",
        "structlog",
        "xarray",
    ],
    tests_require=tests_require,
    extras_require=EXTRAS_REQUIRE,
    entry_points="""
        [console_scripts]
        eo3-validate=eodatasets3.validate:run
        eo3-prepare=eodatasets3.scripts.prepare:run
        eo3-recompress-tar=eodatasets3.scripts.recompress:main
        eo3-package-wagl=eodatasets3.scripts.packagewagl:run
        eo3-to-stac=eodatasets3.scripts.tostac:run
    """,
)
