from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from django.test import TestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class YoungTests(TestCase):
    def test_youngsters(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "hello")
        self.assertTemplateUsed(response, 'base.html')


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("email")
        username_input.send_keys('am0z')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('1q2w3e')
        self.selenium.find_element_by_xpath('//button[contains(.,"Login")]').click()
