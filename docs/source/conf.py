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
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

html_theme = 'sphinx_rtd_theme' # pip3 install sphinx_rtd_theme

html_logo = 'images/logo-ohstem-white.png'


html_favicon = 'images/favicon.ico'

html_theme_options = {
    #'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    'logo_only': True,
    # 'display_version': True,
    'prev_next_buttons_location': 'bottom',
   #  'style_external_links': True,
   #  'vcs_pageview_mode': '',
    #'style_nav_header_background': 'white',
    # Toc options

    'collapse_navigation': True,
    'sticky_navigation': True,
   #  'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False,

    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
   #  'navigation_depth': 4,
    # 'includehidden': True,
}

html_context  = {
   'display_github' : True ,
   'github_user' : 'username' ,
   'github_repo' : 'reponame' ,
   'github_version' : 'master' 
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
