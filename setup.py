import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="units_converter",
    version="0.0.1",
    author="Francisco Torres",
    author_email="fratorhe@vki.ac.be",
    description="A small tool to convert units in Python, using Pint and Quantulum3.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="-",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['PySimpleGUI',
                      'quantulum3',
                      'pint'])
