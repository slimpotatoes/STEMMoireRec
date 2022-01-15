import os
from setuptools import setup

# Test to be done later
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "STEMMoireRec",
    version = "0.0.1",
    author = "Alexandre Pofelski",
    author_email = "alexandre.pofelski@gmail.com",
    description = ("Python package to reconstruct an oversampled micrograph from a STEM Moire hologram."),
    license = "BSD 3-Clause License",
    url = "https://github.com/slimpotatoes/STEMMoireRec",
    packages=['STEMMoireRec'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: BSD License",
    ],
    python_requires='>=3.7',
    install_requires=read('requirements.txt')
)