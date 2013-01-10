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

pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------
html_theme = 'air'
#html_theme_options = {}
html_theme_path = ['../../../sphinx-themes']

#html_title = None
#html_short_title = None

#html_logo = None

#html_favicon = None

html_static_path = ['_static']

#html_use_opensearch = ''
htmlhelp_basename = 'Reconfiguredoc'


#latex_paper_size = 'letter'
#latex_font_size = '10pt'
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Reconfigure.tex', u'Reconfigure Documentation',
   u'Eugeny Pankov', 'manual'),
]

#latex_logo = None
#latex_use_parts = False
#latex_show_pagerefs = False
#latex_show_urls = False
#latex_preamble = ''
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'reconfigure', u'Reconfigure Documentation',
     [u'Eugeny Pankov'], 1)
]


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Reconfigure'
epub_author = u'Eugeny Pankov'
epub_publisher = u'Eugeny Pankov'
epub_copyright = u'2011, Eugeny Pankov'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True


# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {'http://docs.python.org/': None}

