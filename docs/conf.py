# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys

latex_engine = "xelatex"  # or "lualatex" if you prefer LuaLaTeX
# latex_engine = "lualatex"          # or "lualatex" if you prefer LuaLaTeX

latex_elements = {
    "preamble": r"\XeTeXgenerateactualtext=1",
    "fontpkg": r"""
    \setmainfont{Libertinus Serif}        % full OpenType with math companion
    \setsansfont{Libertinus Sans}
    \setmonofont{Fira Mono}
    \usepackage{unicode-math}
    \setmathfont{Libertinus Math}

    \usepackage{fontawesome5}
    % \faExclamationTriangle → ⚠, etc. (still not really text to copy though)
    """,
}

project = "reStructuredText cheat sheet"
copyright = "2025, MicroComp Nordic AB"
author = "Mats Gustafsson"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosectionlabel",
]

# Only create automatic section labels for top-level sections
autosectionlabel_maxdepth = 1

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# Allow user_guide/ and developer_guide/ subfolders to be included in the toctree
sys.path.insert(0, os.path.abspath("."))

# Optional: give each guide its own title prefix in the sidebar
html_title = "reStructuredText cheat sheet"
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 3,
    "titles_only": False,
}

# Prevent duplicate labels for top-level index pages
autosectionlabel_exclude_names = ["index"]
