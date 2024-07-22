import unittest
from app import create_app
import json

class TestEndpoints(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_insert_sensor_data_success(self):
        response = self.client.post('/radix-eng/api/sensor_data/insert-sensor-data', json={
            "equipmentId": "EQ-12495",
            "timestamp": "2023-02-15T01:30:00.000-05:00",
            "value": 78.42
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], "Sucesso")
        self.assertEqual(data['message'], "dados carregados com sucesso")

    def test_insert_sensor_data_failure(self):
        response = self.client.post('/radix-eng/api/sensor_data/insert-sensor-data', json={})
        self.assertEqual(response.status_code, 400)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], "Erro")

    def test_upload_sensor_data_csv_success(self):
        data = {
            "equipmentId": "EQ-12495",
            "timestamp": "2023-02-15T01:30:00.000-05:00",
            "value": 78.42
        }
        response = self.client.post('/radix-eng/api/sensor_data/upload-csv', data=data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], "Sucesso")
        self.assertEqual(data['message'], "dados carregados com sucesso")

    def test_get_avg_sensor_data_day_success(self):
        response = self.client.get('/radix-eng/api/sensor_data/get-avg-sensor-data-day')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], "Sucesso")
        self.assertEqual(data['message'], "dados retornados com sucesso")

    def test_get_avg_sensor_data_two_days_success(self):
        response = self.client.get('/radix-eng/api/sensor_data/get-avg-sensor-data-two-days')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], "Sucesso")
        self.assertEqual(data['message'], "dados retornados com sucesso")

    def test_get_avg_sensor_data_week_success(self):
        response = self.client.get('/radix-eng/api/sensor_data/get-avg-sensor-data-week')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], "Sucesso")
        self.assertEqual(data['message'], "dados retornados com sucesso")

    def test_get_avg_sensor_data_month_success(self):
        response = self.client.get('/radix-eng/api/sensor_data/get-avg-sensor-data-month')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['status'], "Sucesso")
        self.assertEqual(data['message'], "dados retornados com sucesso")

if __name__ == '__main__':
    unittest.main()
