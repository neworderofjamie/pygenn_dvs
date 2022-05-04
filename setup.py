#!/usr/bin/env python
import numpy as np
import os
import sys

from copy import deepcopy
from platform import system, uname
from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext
from shutil import copytree, rmtree
from generate_swig_interfaces import generateConfigs

# Build dictionary of kwargs to apply to all modules
extension_kwargs = {
    "swig_opts": ["-c++", "-relativeimport", "-py3"],
    "extra_compile_args" : ["-std=c++11"],
    "extra_link_args": [],
    "runtime_library_dirs": ["$ORIGIN"]}


ext_module = Extension('_dvs', ["pygenn_dvs/dvs.i"], **extension_kwargs)

setup(name = "pygenn_dvs",
      version = "0.1",
      packages = find_packages(),
      #package_data={"pygenn": package_data},

      author="University of Sussex",
      description="Library for interfacing DVS cameras with PyGeNN",
      ext_package="pygenn_dvs",
      ext_modules=[ext_module],

      # Requirements
      install_requires=["numpy>=1.17"],
      zip_safe=False,  # Partly for performance reasons
)
