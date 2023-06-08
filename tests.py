import unittest
import requests


class TestAPI(unittest.TestCase):
    URL = 'http://127.0.0.1:5000/api/task'

    data = {
        'title': 'Test',
        'description': 'Testing',
    }
    ident: int

    def test_get_all_tasks(self):
        resp = requests.get(self.URL)
        self.assertEqual(resp.status_code, 200)
        print("Test get all completed")

    def test_post_task(self):
        resp = requests.post(self.URL, json=self.data)
        self.assertEqual(resp.status_code, 200)
        self.ident = resp.json()['id']
        print('Test post completed')

    def test_get_single_task(self):
        resp = requests.get(self.URL + f'/{self.ident}')
        self.assertEqual(resp.status_code, 200)
        print("Test get single completed")

    def test_put_task(self):
        resp = requests.put(self.URL + f'/{self.ident}', json=self.data)
        self.assertEqual(resp.status_code, 200)
        print('Test put completed')

    def test_delete_task(self):
        resp = requests.delete(self.URL + f'/{self.ident}')
        self.assertEqual(resp.status_code, 204)
        print('Test delete completed')


if __name__ == '__main__':
    tester = TestAPI()
    tester.test_get_all_tasks()
    tester.test_post_task()
    tester.test_get_single_task()
    tester.test_put_task()
    tester.test_delete_task()
