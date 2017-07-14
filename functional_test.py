from selenium import webdriver
import unittest

'''
    this is first time functional testing
'''
# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
# assert 'django' in browser.title
# browser.quit()

'''
    unit testing
'''


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Todo', self.browser.title)
        self.fail()

if __name__ == '__main__':
    unittest.main(warnings='ignore')
