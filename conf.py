# Configuration file for the Sphinx documentation builder.
# -- Project information -----------------------------------------------------

project = 'UnitedHealthcare Card Activation Guide'
copyright = '2025, UnitedHealthcare'
author = 'UnitedHealthcare Communications Team'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.todo',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'en'

# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Add custom CSS for UHC branding
html_css_files = [
    'uhc_custom.css',
]

# Custom theme options for Read the Docs theme
html_theme_options = {
    'logo_only': True,
    'display_version': True,
}

# -- Custom variables for UHC Brand Colors ----------------------------------

html_context = {
    'uhc_primary_color': '#002677',  # UHC official navy blue
    'uhc_secondary_color': '#6BA539',  # UHC green accent
    'uhc_text_color': '#333333',
}

# -- Setup function to include custom CSS -----------------------------------

def setup(app):
    app.add_css_file('uhc_custom.css')
