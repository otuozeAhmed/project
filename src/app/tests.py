from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Data


class CardTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='testuser',
        email='test@email.com',
        password='secret'
        )
        self.data = Data.objects.create(
        superuser=self.user,
        uzer='uzzer',
        group='Group1',
        text='this is a text'
        )

    def test_card_content(self):
        self.assertEqual(f'{self.data.group}', 'Group1')
        self.assertEqual(f'{self.data.text}', 'this is a text')

    def test_card_list_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Welcome')
        self.assertTemplateUsed(response, 'index.html')

    def test_card_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get('/post/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Group')
        self.assertTemplateUsed(response, 'card_detail.html')