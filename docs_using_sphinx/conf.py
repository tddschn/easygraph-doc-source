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
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages")
sys.path.append(os.path.abspath('sphinxext'))
print(sys.path)

# -- Project information -----------------------------------------------------

project = 'EasyGraph'
copyright = '2020-2023, Mobile Systems and Networking Group, Fudan University'
author = 'Mobile Systems and Networking Group, Fudan University'

# The full version, including alpha/beta/rc tags
release = '0.2a40'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    # 'sphinx_gallery.gen_gallery'
    "numpydoc",
]


# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'friendly'
pygments_style = "sphinx"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*test*.rst']

# Options for LaTeX output
# ------------------------
# Use a latex engine that allows for unicode characters in docstrings
latex_engine = "xelatex"
# The paper size ('letter' or 'a4').
latex_paper_size = "letter"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
# Themes trying right now: sphinx_rtd_theme, yummy_sphinx_theme, bootstrap - cosmo, flatly, cyborg, furo
html_theme = 'furo'

# html_theme_options in conf.py is used for customisations that affect the entire documentation. This is for stuff like fonts and colors.
html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# add your project’s logo in the documentation
html_logo = "logo.png"

# change the sidebar title
html_title = "EasyGraph 0.2a40"

# Add the 'copybutton' javascript, to hide/show the prompt in code examples
def setup(app):
    app.add_js_file("copybutton.js")
    app.add_css_file('my_theme.css')
