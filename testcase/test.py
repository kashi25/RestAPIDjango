# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import unittest

# class GoogleTestCase(unittest.TestCase):
    
#     def setUp(self):
#         self.driver = webdriver.Edge()
#         self.driver.maximize_window()
#         self.driver.get("http://127.0.0.1:8000/admin/")
#         time.sleep(5)
    
#     def test_google_images(self):
#         image_link = self.driver.find_element(By.LINK_TEXT, 'Images')
#         image_link.click()
#         assert 'Google Images' in self.driver.title
#         time.sleep(5)
    
#     def test_google_search(self):
#         search_box = self.driver.find_element(By.NAME, 'q')
#         search_box.send_keys('Selenium with python')
#         search_box.submit()
#         time.sleep(5)
    
#     def tearDown(self):
#         self.driver.quit()

# if __name__ == '__main__':
#     unittest.main()


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class DjangoAdminLoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("http://127.0.0.1:8000/admin/")
        time.sleep(2)

    def test_login_to_django_admin(self):
        # Find the username and password input fields by their IDs
        username_input = self.driver.find_element(By.ID, 'id_username')
        password_input = self.driver.find_element(By.ID, 'id_password')

        # Enter the login details
        username_input.send_keys('kashi')
        password_input.send_keys('kashi123')

        # Find and click the login button
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]')
        login_button.click()

        # Add a delay to see the result, you might want to remove this in a real test
        time.sleep(5)

        # Assuming you want to check if the login was successful
        # You can check if a specific element is present on the page after login
        # For example, the CSS selector of the "Site administration" link
        site_admin_link = self.driver.find_element(By.LINK_TEXT, 'Site administration')
        self.assertIsNotNone(site_admin_link)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
