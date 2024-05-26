from setuptools import setup, find_packages

setup(
    name='cyberFortuneTelling',
    version='1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},

)