from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in desk_navbar_extended/__init__.py
from desk_navbar_extended import __version__ as version

setup(
	name="desk_navbar_extended",
	version=version,
	description="Tweaks in Desk\'s Navbar to boost Productivity",
	author="Gavin D\'souza",
	author_email="gavin18d@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
