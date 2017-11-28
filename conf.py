#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# General information about the project.

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from misc.cyverse_sphinx_conf import *  # noqa

project = 'SciApps Guide'
copyright = '2017, CyVerse'
author = 'CyVerse'
version = '1.0'
release = '1.0'

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright
html_static_path = ['_static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
        ],
     }
exclude_patterns = ['README.md', 'License.md', 'Contributors_maintainers.md']
