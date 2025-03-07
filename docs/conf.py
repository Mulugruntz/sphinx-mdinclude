# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

import datetime
import pathlib
import sys

project = "sphinx-mdinclude"
copyright = f"{datetime.date.today().year}, Hiroyuki Takagi, CrossNox, Amethyst Reese"
author = "Amethyst Reese"

root = pathlib.Path(__file__).parent.parent
print(f"root = {repr(root)}")
sys.path.insert(0, root.as_posix())

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    "sphinx.ext.intersphinx",
    "sphinx_mdinclude",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

autodoc_default_options = {
    "show-inheritance": True,
    "members": True,
    "undoc-members": True,
}
autodoc_member_order = "groupwise"
autodoc_typehints = "description"

highlight_language = "python3"
intersphinx_mapping = {"python": ("https://docs.python.org/3", None)}
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "alabaster"
html_theme_options = {
    "description": "Markdown extension for Sphinx",
    "fixed_sidebar": True,
    "badge_branch": "main",
    "github_button": False,
    "github_user": "amyreese",
    "github_repo": "sphinx-mdinclude",
    "show_powered_by": False,
    "sidebar_collapse": False,
    "extra_nav_links": {
        "Report Issues": "https://github.com/amyreese/sphinx-mdinclude/issues",
    },
}

html_sidebars = {
    "**": [
        "about.html",
        "badges.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        # "omnilib.html",
    ],
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
