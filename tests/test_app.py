import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app import app

class TestFlaskRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        resposta = self.app.get('/')
        self.assertEqual(resposta.status_code, 200)

    def test_post_predicao(self):
        dados = {
            'temperatura': 23.0,
            'umidade': 50.0,
            'luz': 300.0,
            'co2': 500.0,
            'humidade_relativa': 0.0045
        }
        resposta = self.app.post('/form', data=dados, follow_redirects=True)
        self.assertEqual(resposta.status_code, 200)
        self.assertTrue(b'Ocupado' in resposta.data or b'Vazio' in resposta.data)

if __name__ == '__main__':
    unittest.main()
