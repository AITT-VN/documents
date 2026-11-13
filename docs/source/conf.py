# Configuration file for the Sphinx documentation builder.

# -- Project information
project = 'OhStem Education Wiki'
copyright = '2022, OHSTEM'
author = 'OHSTEM EDUCATION'

release = '2.0'
version = '2.0.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'myst_parser',
]

language = 'vi'
myst_enable_extensions = ['colon_fence']
myst_heading_anchors = 3

templates_path = ['_templates']

html_theme = 'sphinx_rtd_theme'
html_logo = 'images/logo-ohstem-white.png'
html_favicon = 'images/favicon.ico'
html_theme_options = {
    'logo_only': True,
    'prev_next_buttons_location': 'bottom',
    'collapse_navigation': True,
    'sticky_navigation': True,
    'includehidden': True,
    'titles_only': False,
}
html_context = {'display_github': False}

# -- Options for EPUB output
epub_show_urls = 'footnote'
