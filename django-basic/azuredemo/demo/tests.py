from django.test import TestCase, Client

class DemoTestCase(TestCase):
    def test_index_no_user(self):
        c = Client()
        response = c.post('/demo/', {'person': None})
        assert response.status_code == 404

    def test_index_ground_control(self):
        c = Client()
        response = c.post('/demo/', {'person': 'ground_control', 'message': 'Ground Control to Major Tom'})
        assert response.status_code == 200
        assert 'the stars look very different today' in response.content.decode('utf-8')
