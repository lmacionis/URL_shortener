from django.test import TestCase
from url.models import AllUrl


class AllUrlTest(TestCase):

    def setUp(self):
        first_url = AllUrl()
        first_url.long_url = 'www.google.com'
        first_url.short_url = '123456'
        first_url.save()

        second_url = AllUrl()
        second_url.long_url = 'www.yahoo.com'
        second_url.short_url = '789456'
        second_url.save()

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

    def test_saving_and_retrieving_url_items(self):
        saved_urls = AllUrl.objects.all()
        self.assertEqual(saved_urls.count(), 2)

        first_saved_url = saved_urls[0]
        second_saved_url = saved_urls[1]
        self.assertEqual(first_saved_url.short_url, '123456')
        self.assertEqual(first_saved_url.long_url, 'www.google.com')
        self.assertEqual(second_saved_url.short_url, '789456')
        self.assertEqual(second_saved_url.long_url, 'www.yahoo.com')
