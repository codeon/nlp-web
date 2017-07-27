from __future__ import absolute_import, division, print_function

from django.conf.urls import url

from nlp_web.views import (TextParser)

urlpatterns = [
    url(r'^parse_text/?$', TextParser.as_view()),
]
