import unittest
from .app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        reponse = self.app.get('/')
        self.assertEqual(reponse.status_code, 200)
        
    def test_add_transaction(self):
        reponse = self.app.get('/transaction/add')
        self.assertEqual(reponse.status_code, 200)

    def test_edit_transaction(self):
        reponse = self.app.get('/transaction/edit/1')
        self.assertEqual(reponse.status_code, 200)

    def test_delete_transaction(self):
        reponse = self.app.get('/transaction/delete/1')
        self.assertEqual(reponse.status_code, 200)

    def test_search_transactions(self):
        reponse = self.app.get('/transaction/search')
        self.assertEqual(reponse.status_code, 200)

if __name__ == '__main__':
    unittest.main()
