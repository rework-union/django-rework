import unittest

from rework.core.management.handlers.urls import UrlsHandle


class UrsHandleTestCase(unittest.TestCase):
    def test_add_route_to_urlpatterns(self):
        content = """

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

"""
        except_content = """

from django.contrib import admin
from django.urls import path

from django.urls import re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^api/tests/', include('rework.contrib.tests.urls', namespace='tests')),
]

"""
        urls_handler = UrlsHandle()
        content = urls_handler._add_route(content, 'tests')
        self.assertEqual(content, except_content)
