#!/usr/bin/env python
import numpy as np
import os

from setuptools import setup, find_packages, Extension

numpy_path = os.path.join(os.path.dirname(np.__file__))

# Build dictionary of kwargs to apply to all modules
extension_kwargs = {
    "swig_opts": ["-c++", "-relativeimport", "-py3"],
    "extra_compile_args": ["-std=c++11"],
    "libraries": ["caer"],
    "extra_link_args": [],
    "include_dirs": [os.path.join(numpy_path, "core", "include")],
    "runtime_library_dirs": ["$ORIGIN"]}


ext_module = Extension('_dvs', ["pygenn_dvs/dvs.i"], **extension_kwargs)

setup(name = "pygenn_dvs",
      version = "0.1",
      packages = find_packages(),
  
      author="University of Sussex",
      description="Library for interfacing DVS cameras with PyGeNN",
      ext_package="pygenn_dvs",
      ext_modules=[ext_module],

      # Requirements
      install_requires=["numpy>=1.17"],
      zip_safe=False,  # Partly for performance reasons
)
