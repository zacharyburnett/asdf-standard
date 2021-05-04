# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Project information -----------------------------------------------------

project = 'ASDF Standard'

import datetime
copyright = f'{datetime.datetime.now().year}, Space Telescope Science Institute'

author = 'Michael Droettboom, Erik Bray, et al'

# The short X.Y version
version = '1.6.0'
# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax', 'sphinx.ext.ifconfig', 'sphinx.ext.graphviz',
    'sphinx_asdf'
]

mathjax_path = 'https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = "ref"

# The default language for highlighting
highlight_language = 'yaml'

# The encoding of source files.
source_encoding = 'utf-8'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'bootstrap'

import sphinx_bootstrap_theme
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'navbar_site_name': 'Document',
    'navbar_pagenav': False
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = '_static/logo.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
html_use_smartypants = True

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
html_use_index = True

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

html_context = {
    'bootswatch_css_custom': ['_static/asdfstandard.css']
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'ASDFStandard'


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
    % Use a more modern-looking monospace font
    \usepackage[medium]{cabin}
    \usepackage[bitstream-charter]{mathdesign}
    \usepackage{inconsolata}
    \usepackage{bbding}
    \usepackage{fixltx2e}
    \usepackage{microtype}
    \usepackage{changepage}
    \usepackage{enumitem}
    \usepackage{pmboxdraw}
    \MakeRobust\marginpar

    \DeclareUnicodeCharacter{2264}{$\leq$}
    \DeclareUnicodeCharacter{2265}{$\geq$}
    \DeclareUnicodeCharacter{2014}{$\textemdash\textemdash\textemdash$}

    \setlistdepth{10}

    \makeatletter
        \def\marginparright{\@mparswitchfalse}
        \def\marginparoutside{\@mparswitchtrue}
    \makeatother

    \renewenvironment{quote}{\begin{adjustwidth}{15pt}{}}{\end{adjustwidth}}

    ''',
    'fontpkg': '',
    'fncychap': '\\usepackage[Conny]{fncychap}'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, f'ASDFStandard-{version}.tex', 'ASDF Standard',
     author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = '_static/logo.pdf'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = 'inline'

# If false, no module index is generated.
latex_domain_indices = False

# Additional latex styles needed
latex_additional_files = ['eqparbox.sty', 'capt-of.sty']


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'asdf-standard', project,
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'ASDFStandard', project,
     author, 'ASDFStandard',
     'Advanced Scientific Data Format',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = 'Space Telescope Science Institute'
epub_copyright = copyright

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- sphinx_asdf configuration ---------------------------------------------

# Top-level directory containing ASDF schemas (relative to current directory)
asdf_schema_path = '../../schemas'
# This is the prefix common to all schema IDs in this repository
asdf_schema_standard_prefix = 'stsci.edu/asdf'
# This seems pretty redundant/unnecessary and should probably be fixed in the
# plugin.
asdf_schema_reference_mappings = [
    ('tag:stsci.edu:asdf',
     'http://asdf-standard.readthedocs.io/en/latest/generated/stsci.edu/asdf'),
    ('http://json-schema.org/draft-04/schema',
     'http://json-schema.org/draft-04/json-schema-validation'),
]
