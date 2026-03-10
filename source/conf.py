# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Manual das Varas Criminais'
copyright = '2026, TJAM'
author = 'Tribunal de Justiça do Estado do Amazonas'
release = '1.1'



# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_rtd_theme',
    'rst2pdf.pdfbuilder'
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'
source_encoding = 'utf-8'


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

pdf_documents = [('index', u'guiacriminal', u'Guia das Varas Criminais', u'TJAM'),]
  # index - master document
  # rst2pdf - name of the generated pdf
  # Sample rst2pdf doc - title of the pdf
  # Your Name - author name in the pdf

pdf_stylesheets = [
    'sphinx',
    '_static/styles/livro.yml',
]

pdf_font_path = ['_static/fonts']
pdf_language = 'pt_BR'
pdf_break_level = 1
pdf_toc_depth = 5
pdf_use_index = True
