# from distutils.core import setup, find_packages
import sys

from setuptools import find_packages, setup

# For old pip versions
if sys.version_info < (3, 7):
    sys.exit("Sorry, Python < 3.7 is not supported")

setup(
    name="Payton",
    version="0.0.2.39",
    author="Sinan ISLEKDEMIR",
    author_email="sinan@islekdemir.com",
    # Packages
    packages=find_packages(),
    # Include additional files into the package
    include_package_data=True,
    # Details
    url="https://github.com/sinanislekdemir/payton",
    #
    license="GNU GPLv3",
    description="Payton 3D Kickstart Toolkit",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">3.7",
    # Dependent packages (distributions)
    install_requires=["numpy", "Pillow", "PyOpenGL", "pyrr", "PySDL2", "read"],
)
