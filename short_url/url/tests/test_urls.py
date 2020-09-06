from django.test import SimpleTestCase
from django.urls import reverse, resolve
from url.views import UrlView, redirect_url


class TestUrls(SimpleTestCase):
    def test_form_url_is_resolved(self):
        url = reverse('form')
        self.assertEquals(resolve(url).func.view_class, UrlView)

    def test_s_code_url_is_resolved(self):
        url = reverse('s_code', args=['some_slug'])
        self.assertEquals(resolve(url).func, redirect_url)
