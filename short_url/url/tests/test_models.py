from django.test import TestCase
from url.models import AllUrl


class AllUrlTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        AllUrl.objects.create(long_url="www.google.com", short_url="kirrgo")

    def test_long_url_label(self):
        url = AllUrl.objects.get(id=1)
        field_label = url._meta.get_field('long_url').verbose_name
        self.assertEquals(field_label, 'long url')

    def test_short_url_label(self):
        url = AllUrl.objects.get(id=1)
        field_label = url._meta.get_field('short_url').verbose_name
        self.assertEquals(field_label, 'short url')

    def test_long_url_max_length(self):
        url = AllUrl.objects.get(id=1)
        max_length = url._meta.get_field('long_url').max_length
        self.assertEquals(max_length, 200)

    def test_short_url_max_length(self):
        url = AllUrl.objects.get(id=1)
        max_length = url._meta.get_field('short_url').max_length
        self.assertEquals(max_length, 6)
