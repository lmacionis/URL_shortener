from django.test import TestCase
from django.urls import resolve
from url.views import UrlView


class HomePageTest(TestCase):

    def test_root_url_resolves_to_UrlView(self):
        found = resolve('/')
        self.assertEqual(found.func.view_class, UrlView)
