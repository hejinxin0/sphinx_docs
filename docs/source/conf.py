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
numfig = True

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# https://github.com/executablebooks/markdown-it-py/blob/master/docs/conf.py
# https://github.com/executablebooks/mdit-py-plugins/blob/master/docs/conf.py
extensions = [
   # 'recommonmark',
   # 'sphinx_markdown_tables',
    'ablog',
    'myst_parser',
    'sphinx.ext.todo',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz',
    'sphinx_search.extension',
    'sphinx_tabs.tabs',
    'sphinx_thebe',
    'sphinx_togglebutton',
    #'sphinxcontrib.bibtex',
    #'sphinxext.opengraph',
    'sphinx.ext.todo',
    'sphinx_copybutton',
    'sphinx_design',
]
#mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

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
#html_theme = 'pydata_sphinx_theme'
html_theme = 'sphinx_book_theme'

#https://sphinx-book-theme.readthedocs.io/en/latest/?badge=latest
#https://github.com/executablebooks/sphinx-book-theme/blob/master/docs/conf.py
html_copy_source = True
html_theme_options = {
    # 导航栏
    # "navbar_start": ["navbar-logo"],
    # "navbar_center": ["navbar-nav"],
    # "navbar_end": ["navbar-icon-links"],
    # "navbar_persistent": ["search-field"],
    "icon_links": [
    {
        "name": "GitHub",
        "url": "https://github.com/hejinxin0/sphinx_docs.git",
        "icon": "fa-brands fa-square-github",
        "type": "fontawesome",
    },], 
    
    "use_edit_page_button": True,
    "use_source_button": True,
    "use_issues_button": True,
    "use_repository_button": True,
    "use_download_button": True,
    "use_sidenotes": True, 
    "home_page_in_toc": True,
    #"article_header_start": [],
    #"article_header_end": ["theme-switcher.html","toggle-secondary-sidebar.html"],

    # 主侧边栏
    "navigation_depth": 2,
    "show_nav_level": 1, 
    "repository_url": "https://github.com/hejinxin0/sphinx_docs",
    "repository_branch": "master",
    "path_to_docs": "docs/source",
    "launch_buttons": {
       # "binderhub_url": "https://mybinder.org",
       # "colab_url": "https://colab.research.google.com/",
       # "deepnote_url": "https://deepnote.com/",
        "notebook_interface": "jupyterlab",
        "thebe": True,
        "jupyterhub_url": "https://datahub.berkeley.edu",  # For testing
    },
    #"primary_sidebar_end": ["indices.html", "sidebar-ethical-ads.html"],

    # 辅助侧边栏
    "show_toc_level": 3,
    #"secondary_sidebar_items": ["page-toc", "edit-this-page", "sourcelink"],
    
    # 页脚
    "footer_content_items": ["author", "copyright", "sphinx-version", "theme-version"],
    #"extra_footer": ["last-updated","sphinx-version"],
    #"footer_content_end": ["theme-version"],
    #"footer_start": ["author", "copyright"],
    #"footer_end": ["sphinx-version", "theme-version"],

    # 代码块主题样式
    "pygment_light_style": "default",
    "pygment_dark_style": "default",  
} 

html_sidebars = {
    "**": [
        "navbar-logo",   
        "navbar-icon-links",
        "search-field",
       # "postcard.html",
       # "recentposts.html",
       # "tagcloud.html",
       # "categories.html",
       # "archives.html",
       "sbt-sidebar-nav",
       "sourcelink",
       "edit-this-page",
       "sidebar-ethical-ads.html",
    ]
}





