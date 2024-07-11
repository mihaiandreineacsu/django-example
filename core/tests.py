from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User

POST_API_URL = reverse('core:post-list')


# Create your tests here.
class PostsAPITest(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_request_on_get(self):
        user = User.objects.create(username="Mihai", password="pypassword")
        self.client.force_authenticate(user=user)

        response = self.client.get(POST_API_URL)

        print(response.context)

        self.assertEqual(response.status_code, 200)

    def test_request_create_post_ok(self):
        user = User.objects.create(username="Mihai", password="pypassword")
        user2 = User.objects.create(username="Andrei", password="pypassword")

        self.client.force_authenticate(user=user)

        payload = {"author": user2.id, "title": "Some Title", "description": "Some Description"}
        response = self.client.post(POST_API_URL, payload)
        print(f"response : {response.context}")

        self.assertEqual(response.json().get("author"), user.id)
        self.assertEqual(response.status_code, 201)
