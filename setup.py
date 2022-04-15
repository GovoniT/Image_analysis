import setuptools
import os

NAME = "Image_analysis"
VERSION = "0.0.1"
AUTHOR = "Tony Govoni"
EMAIL = "tony.govoni@epfl.ch"
DESCRIPTION = "Image_analysis is a python code that allow you from a recorded video to track rectangular colored object."
LONG_DESCRIPTION = "Image_analysis is a python code that allow you from a recorded video to track rectangular colored object."
URL = ""
REQUIRES_PYTHON = ">=3.7.0"

thelibFolder = os.path.dirname(os.path.realpath(__file__))
requirementPath =os.path.join(thelibFolder,"requirement.txt")
REQUIRED = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        REQUIRED = f.read().splitlines()

README = "README.md"
PACKAGE_DIR = "."
LICENSE = "Apache License 2.0"


setuptools.setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    url=URL,
    include_package_data=True,
    package_dir={"": PACKAGE_DIR},
    license=LICENSE,
    packages=[NAME],
    python_requires=REQUIRES_PYTHON,
    keywords=["computervision", "objectdetection"],
    install_requires=REQUIRED,
    # See: https://pypi.org/classifiers/
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
)
