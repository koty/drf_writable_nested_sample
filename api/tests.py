# https://github.com/beda-software/drf-writable-nested/blob/master/tests/test_writable_nested_model_serializer.py

from rest_framework.test import APITestCase


def get_initial_data():
    return {
        'username': 'test',
        'profile': {
            'access_key': {
                'key': 'key',
            },
            'sites': [
                {
                    'url': 'http://google.com',
                },
                {
                    'url': 'http://yahoo.com',
                },
            ],
            'avatars': [
                {
                    'image': 'image-1.png',
                },
                {
                    'image': 'image-2.png',
                },
            ],
            'messages': [
                {
                    'message': 'Message 1'
                },
                {
                    'message': 'Message 2'
                },
                {
                    'message': 'Message 3'
                },
            ]
        },
    }


class MyTest(APITestCase):

    def test_create_user(self):
        data = get_initial_data()
        result = self.client.post('/api/users', data=data, format='json')
        self.assertEqual(201, result.status_code)

        # 取得できるか確認
        result = self.client.get('/api/users/1', data=data, format='json')
        self.assertEqual(200, result.status_code)
        self.assertEqual(3, len(result.data['profile']['messages']))
        self.assertEqual('Message 1', result.data['profile']['messages'][0]['message'])
        self.assertEqual('Message 3', result.data['profile']['messages'][2]['message'])
        message_2_pk = result.data['profile']['messages'][2]['pk']

        # パラメータをCRUD
        result.data['profile']['messages'].pop()  # 一件削除
        result.data['profile']['messages'][0]['message'] = 'Message 1 hoge'  # update
        result.data['profile']['messages'].append({'message': 'Message 4'})  # 一件追加

        # 更新
        result = self.client.put('/api/users/1', data=result.data, format='json')
        self.assertEqual(200, result.status_code)
        self.assertEqual(3, len(result.data['profile']['messages']))
        self.assertEqual('Message 1 hoge', result.data['profile']['messages'][0]['message'])
        self.assertEqual('Message 4', result.data['profile']['messages'][2]['message'])
        self.assertNotEqual(message_2_pk, result.data['profile']['messages'][2]['pk'])
