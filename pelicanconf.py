#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'multivac'
SITENAME = '仿生人梦见电子羊'
SITEURL = ''

# DIR for content
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = [
    ('About', 'pages/about.html')
    # ('文章', '/index.html'),
    # ('归档', '/archives.html'),
    # ('标签', '/tags.html'),
]

# For simple-bootstrap template use.
MENUITEMS_DICT = {title: link for title, link in MENUITEMS}

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Customized confs.
THEME = 'simple-bootstrap'

# easy hack for getting the current time in jinja
# NOW = datetime.now()
LOAD_CONTENT_CACHE = False

STATIC_PATHS = ['images', 'extra/CNAME', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

SUMMARY_MAX_LENGTH = 15

## plugins #########################
# PLUGIN_PATHS = ['plugins']
# PLUGINS = ["render_math"]
