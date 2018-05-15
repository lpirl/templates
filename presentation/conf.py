#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date

extensions = ['sphinx.ext.graphviz', 'hieroglyph']

# required, so that serving the slides under "/" works in the browser
master_doc = 'index'

exclude_patterns = ['_*', 'Thumbs.db', '.DS_Store', 'README*']

# required, so that the HTML title does not get suffixed with
# "… documentation"
html_title = ""

html_scaled_image_link = False

slide_theme_path = ['_themes']
slide_theme = 'simple-slides-dark'
slide_footer = '　'.join((
    'lorem ipsum title',
    'lorem ipsum event',
    'lukas.pirl@hpi.de',
    'dd.mm.yyyy',
))
slide_numbers = True

pygments_style = 'monokai'

graphviz_output_format = 'svg'

rst_prolog = '.. include:: prolog.rst'
