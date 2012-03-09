# -*- coding: utf-8 -*-
# welcome.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('welcome/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'welcome/index': 'welcome.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='welcome.views.index'),
  )
]

