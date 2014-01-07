# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.abspath('../..'))

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.ifconfig', 'sphinx.ext.viewcode']  # 'sphinx.ext.intersphinx']

templates_path = ['_templates']

source_suffix = '.rst'

#source_encoding = 'utf-8-sig'

master_doc = 'index'

project = u'Reconfigure'
copyright = u'2013, Eugeny Pankov'

version = '1.0'
release = '1.0a1'

exclude_patterns = []
add_function_parentheses = True

#pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------
#html_theme = 'air'
#html_theme_options = {}
#html_theme_path = ['../../../sphinx-themes']

html_title = 'Reconfigure documentation'
html_short_title = 'Reconfigure docs'

#html_logo = None

#html_favicon = None

html_static_path = ['_static']

htmlhelp_basename = 'Reconfiguredoc'


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

