# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Learning summary document'
copyright = '2023, Hejinxin'
author = 'Hejinxin'
release = 'v1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
   # 'recommonmark',
   # 'sphinx_markdown_tables',
    'myst_parser',
]

myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

extensions.append('sphinx.ext.todo')
extensions.append('sphinx.ext.autodoc')
extensions.append('sphinx.ext.autosummary')
extensions.append('sphinx.ext.intersphinx')
extensions.append('sphinx.ext.mathjax')
extensions.append('sphinx.ext.viewcode')
extensions.append('sphinx.ext.graphviz')
#mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

'''
html_static_path = ['_static']
html_css_files = [
    'css/custom.css',
]
'''
#html_theme = 'sphinx_rtd_theme'
#html_theme = 'sphinx-book-theme'
html_theme = 'pydata_sphinx_theme'

html_theme_options = {
    # 导航栏
    # "navbar_start": ["navbar-logo"],
    # "navbar_center": ["navbar-nav"],
    # "navbar_end": ["navbar-icon-links", "navbar-icon-links"],
    "navbar_persistent": ["search-field"],
    "icon_links": [
    {
        "name": "GitHub",
        "url": "https://github.com/hejinxin0/sphinx_docs.git",
        "icon": "fa-brands fa-square-github",
        "type": "fontawesome",
    },],
    
    # 主侧边栏
    "navigation_depth": 2,
    "show_nav_level": 1, 

    # 辅助侧边栏
    "show_toc_level": 2,
    #"use_edit_page_button": False,
   
   # 代码块主题样式
   "pygment_light_style": "default",
   "pygment_dark_style": "default"
}

