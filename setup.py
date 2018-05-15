##############################################################################
#
# Written by Brandon Owen, May 2016, brandon.owen@hotmail.com
# Adapted from original work by Mark Adler - orginal copyright notice below
#
# Copyright (C) 2014, 2015 Mark Adler
# This software is provided 'as-is', without any express or implied
# warranty.  In no event will the authors be held liable for any damages
# arising from the use of this software.
# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:
# 1. The origin of this software must not be misrepresented; you must not
# claim that you wrote the original software. If you use this software
# in a product, an acknowledgment in the product documentation would be
# appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
# misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.
# Mark Adler
# madler@alumni.caltech.edu
#
##############################################################################

import io
import os
import re
from setuptools import setup, find_packages


def get_package_version():
    """get version from top-level package init"""
    version_file = read('unlzw/__init__.py')
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


def read(filename, encoding='utf-8'):
    """read file contents"""

    full_path = os.path.join(os.path.dirname(__file__), filename)

    with io.open(full_path, encoding=encoding) as fh:
        contents = fh.read().strip()
        return contents


setup(
    name='unlzw',
    version=get_package_version(),
    author='Brandon Owen',
    author_email='brandon.owen@hotmail.com',
    maintainer='Tom Kralidis',
    maintainer_email='tomkralidis@gmail.com',
    description=('Python decompression module for .Z files compressed '
                 'using Unix compress utility'),
    license='MIT',
    keywords='lzw',
    url='https://github.com/umeat/unlzw',
    packages=find_packages(),
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
)
