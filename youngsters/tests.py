from django.core.urlresolvers import reverse
from django.test import TestCase


class YoungTests(TestCase):
    def test_youngsters(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "hello")
        self.assertTemplateUsed(response, 'base.html')
