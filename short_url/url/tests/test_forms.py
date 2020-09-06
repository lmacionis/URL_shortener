from django.test import SimpleTestCase
from url.forms import CreateNewURL


class TestForms(SimpleTestCase):

    def test_create_new_url_form_valid_data(self):
        long_url = 'www.google.com'
        form = CreateNewURL(data={
            'original_url': long_url
        })
        self.assertTrue(form.is_valid())
