# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../'))


# -- Project information -----------------------------------------------------

project = 'sknet'
copyright = '2021, Tiago Toledo'
author = 'Tiago Toledo'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon'
]

master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'
html_logo = "_static/logo.png"

html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/TNanukem/sknet",
            "icon": "fab fa-github-square",
        },
        {
            "name": "Twitter",
            "url": "https://twitter.com/TiagoJToledoJr",
            "icon": "fab fa-twitter-square",
        },
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

############################
# SETUP THE RTD LOWER-LEFT #
############################
try:
   html_context
except NameError:
   html_context = dict()
html_context['display_lower_left'] = True
 
if 'REPO_NAME' in os.environ:
   REPO_NAME = os.environ['REPO_NAME']
else:
   REPO_NAME = ''
 
# SET CURRENT_VERSION
from git import Repo
repo = Repo( search_parent_directories=True )
 
if 'current_version' in os.environ:
   # get the current_version env var set by buildDocs.sh
   current_version = os.environ['current_version']
else:
   # the user is probably doing `make html`
   # set this build's current version by looking at the branch
   current_version = repo.active_branch.name
 
# tell the theme which version we're currently on ('current_version' affects
# the lower-left rtd menu and 'version' affects the logo-area version)
html_context['current_version'] = current_version
html_context['version'] = current_version
 
# POPULATE LINKS TO OTHER VERSIONS
html_context['versions'] = list()
 
versions = [branch.name for branch in repo.branches]
for version in versions:
   html_context['versions'].append((version, '/' + REPO_NAME + '/'  + version + '/'))
 
# POPULATE LINKS TO OTHER FORMATS/DOWNLOADS
 
# settings for creating PDF with rinoh
rinoh_documents = [(
 master_doc,
 'target',
 project+ ' Documentation',
 '© ' +copyright,
)]
today_fmt = "%B %d, %Y"
 
# settings for EPUB
epub_basename = 'target'
 
html_context['downloads'] = list()
html_context['downloads'].append( ('pdf', '/' +REPO_NAME+ '/' +current_version+ '/' +project+ '-docs_' + '_' +current_version+ '.pdf') )
 
html_context['downloads'].append( ('epub', '/' +REPO_NAME+ '/' +current_version+ '/' +project+ '-docs_' + '_' +current_version+ '.epub') )

##########################
# "EDIT ON GITHUB" LINKS #
##########################
 
html_context['display_github'] = True
html_context['github_user'] = 'maltfield'
html_context['github_repo'] = 'rtd-github-pages'
html_context['github_version'] = 'master/docs/'