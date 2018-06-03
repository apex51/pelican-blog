#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'mult1vac'
SITENAME = '数据之下'
SITEURL = 'mult1vac.me'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'cn'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

MENUITEMS = [
    ('文章', '/index.html'),
    # ('归档', '/archives.html'),
    # ('标签', '/tags.html'),
    ('关于', '/pages/about.html')
]

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Customized confs.
THEME = 'theme'

# easy hack for getting the current time in jinja
NOW = datetime.now()
LOAD_CONTENT_CACHE = False

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}