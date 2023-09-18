from setuptools import setup, find_packages

setup(name='proteinmpnn',
      version='1.0.0',
      description='Custom install of ProteinMPNN',
      author='Rosetta Commons',
      url='https://github.com/BigHat-Biosciences/ProteinMPNN',
      packages=find_packages(),
      install_requires=['torch'])
