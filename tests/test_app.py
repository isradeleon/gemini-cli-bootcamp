import unittest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Course Explainer', response.data)

    def test_course_page(self):
        # Existing test for course page
        response = self.app.get('/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Introduction to Python', response.data)

    def test_get_course_api(self):
        # New test for the API endpoint
        response = self.app.get('/api/course/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        data = response.get_json()
        self.assertEqual(data['title'], 'Introduction to Python')
        self.assertEqual(data['instructor'], 'John Doe')

    def test_contact_page(self):
        # Test for the contact page
        response = self.app.get('/contact')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Contact Us', response.data)
        self.assertIn(b'Send us a message', response.data)
        self.assertIn(b'Twitter', response.data)

if __name__ == '__main__':
    unittest.main()