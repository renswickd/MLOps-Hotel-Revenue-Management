from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="End-to-End MLOps for Hotel Revenue Management",
    version="0.1",
    author="Renswick Delvar",
    packages=find_packages(),
    install_requires = requirements,
)