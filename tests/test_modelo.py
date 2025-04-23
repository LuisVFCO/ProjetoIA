import unittest
import pickle
import pandas as pd
import os

class TestModeloIA(unittest.TestCase):
    def setUp(self):
        modelo_path = os.path.join('models', 'arvore_from_pickle.pkl')
        with open(modelo_path, 'rb') as f:
            self.model = pickle.load(f)

    def test_modelo_carregado(self):
        self.assertIsNotNone(self.model, "O modelo não foi carregado corretamente")

    def test_predicao_valida(self):
        entrada = pd.DataFrame([{
            'Temperature': 23.0,
            'Humidity': 50.0,
            'Light': 300.0,
            'CO2': 500.0,
            'HumidityRatio': 0.0045
        }])
        pred = self.model.predict(entrada)
        self.assertIn(pred[0], [0, 1], "Predição fora do esperado (deve ser 0 ou 1)")

if __name__ == '__main__':
    unittest.main()
