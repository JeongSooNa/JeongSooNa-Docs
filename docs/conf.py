# docs/conf.py

import os
import sys

project = 'JeongSooNa Docs'
author = 'JeongSooNa'
release = '0.1'

extensions = ['sphinx.ext.autodoc']
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

extensions = [
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}