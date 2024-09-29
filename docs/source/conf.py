# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Bluetooth App'
copyright = '2024, TC'
author = 'TC'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_js"]

templates_path = ['_templates']
exclude_patterns = []

import sys, os
sys.path.insert(0, os.path.abspath('../../src'))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

# -- Options for sphinx-js ---------------------------------------------------
js_language = 'typescript'
js_source_path = "../../"
jsdoc_config_path = "../../tsconfig.json"
primary_domain = 'js'