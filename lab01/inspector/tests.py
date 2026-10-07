from django.test import TestCase

# Create your tests here.


class HelloViewTests(TestCase):
    def test_default_message(self):
        response = self.client.get('/hello/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello world!')

    def test_custom_message(self):
        response = self.client.get('/hello/?message=Hey!')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hey!')

    def test_header_custom_message_overwrites_query_params(self):
        response = self.client.get('/hello/?message=hahah', None, None, None, headers={'Lab-Message': 'How are you?'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'How are you?')

    def test_hello_redirect_path(self):
        response = self.client.get('/hello')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.headers.get('Location'), '/hello/')