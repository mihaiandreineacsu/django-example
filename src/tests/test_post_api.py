from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from core.models import Post

POST_API_URL = reverse("api:post-list")


def detail_url(post_id):
    """Create and return a post detail URL."""
    return reverse("api:post-detail", args=[post_id])


# Create your tests here.
class PostsAPITest(TestCase):

    client: APIClient

    def setUp(self) -> None:
        self.client = APIClient()

    def test_request_delete_post(self):
        user = User.objects.create(username="Mihai", password="pypassword")
        user2 = User.objects.create(username="Andrei", password="pypassword")

        new_post = Post.objects.create(author=user, title="Post from user Mihai", description="Some Post to test.")
        self.client.force_authenticate(user=user2)
        response = self.client.delete(detail_url(new_post.id))
        print(response.context)
        deleted_post = Post.objects.filter(author=user.id).first()
        self.assertNotEqual(deleted_post, None)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_on_get(self):
        user = User.objects.create(username="Mihai", password="pypassword")
        self.client.force_authenticate(user=user)

        response = self.client.get(POST_API_URL)

        print(response.context)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_request_create_post_forbidden(self):
    #     user = User.objects.create(username="Mihai", password="pypassword")
    #     user2 = User.objects.create(username="Andrei", password="pypassword")

    #     self.client.force_authenticate(user=user)

    #     payload = {"author": user2.id, "title": "Some Title", "description": "Some Description"}
    #     response = self.client.post(POST_API_URL, payload)
    #     print(f"response : {response.context}")

    #     self.assertIsNone(response.json().get("author"))
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_create_post_ok(self):
        user = User.objects.create(username="Mihai", password="pypassword")

        self.client.force_authenticate(user=user)

        payload = {
            "author": user.id,
            "title": "Some Title",
            "description": "Some Description",
        }
        response = self.client.post(POST_API_URL, payload)
        print(f"response : {response.context}")

        # self.assertIsNone(response.json().get("author"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_create_post_for_other_user(self):
        user = User.objects.create(username="Mihai", password="pypassword")
        user2 = User.objects.create(username="Andrei", password="pypassword")

        self.client.force_authenticate(user=user)

        payload = {
            "author": user2.id,  # ignored by the api and  replaced with the request.user
            "title": "Some Title",
            "description": "Some Description",
        }
        response = self.client.post(POST_API_URL, payload)
        with self.assertRaises(Post.DoesNotExist):
            _ = Post.objects.get(author=user2)
        self.assertTrue(Post.objects.filter(author=user).exists())
        print(f"response : {response.context}")

        # self.assertIsNone(response.json().get("author"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_request_update_forbidden(self):
        user = User.objects.create(username="Mihai", password="pypassword")
        user2 = User.objects.create(username="Andrei", password="pypassword")
        new_post = Post(author=user2, title="Some Title", description="Some Description")
        new_post.save()

        self.client.force_authenticate(user=user)

        payload = {
            "author": user2.id,
            "title": "Update Title",
            "description": "Update Description",
        }
        response = self.client.put(detail_url(new_post.id), payload)
        print(f"response : {response.context}")

        updated_post = Post.objects.get(id=new_post.id)

        self.assertEqual(updated_post.author, user2)
        self.assertEqual(updated_post.title, "Some Title")
        self.assertEqual(updated_post.description, "Some Description")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_update_ok(self):
        user = User.objects.create(username="Mihai", password="pypassword")
        new_post = Post(author=user, title="Some Title", description="Some Description")
        new_post.save()

        self.client.force_authenticate(user=user)

        payload = {
            "author": user.id,
            "title": "Update Title",
            "description": "Update Description",
        }
        response = self.client.put(detail_url(new_post.id), payload)
        print(f"response : {response.context}")

        updated_post = Post.objects.get(id=new_post.id)

        self.assertEqual(updated_post.author, user)
        self.assertEqual(updated_post.title, "Update Title")
        self.assertEqual(updated_post.description, "Update Description")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_request_patch_ok(self):
        user = User.objects.create(username="Mihai", password="pypassword")
        user2: User = User.objects.create(username="Andrei", password="pypassword")

        new_post = Post(author=user2, title="Some Title", description="Some Description")
        new_post.save()

        self.client.force_authenticate(user=user)

        payload = {
            "author": user2.id,  # this should be ignored by the api and replaced with the authenticated user
            "title": "Update Title",
            "description": "Update Description",
        }
        response = self.client.patch(detail_url(new_post.id), payload)

        updated_post = Post.objects.get(id=new_post.id)
        self.assertEqual(updated_post.id, new_post.id)
        self.assertEqual(updated_post.author.id, user2.id)
        self.assertEqual(updated_post.title, "Some Title")
        self.assertEqual(updated_post.description, "Some Description")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_request_delete_post_for_other_user_forbidden(self):
        user = User.objects.create(username="Mihai", password="pypassword")
        user2: User = User.objects.create(username="Andrei", password="pypassword")

        new_post = Post(author=user2, title="Some Title", description="Some Description")
        new_post.save()

        self.client.force_authenticate(user=user)

        response = self.client.delete(detail_url(new_post.id))

        to_delete_post = Post.objects.get(id=new_post.id)
        self.assertEqual(to_delete_post.id, new_post.id)
        self.assertEqual(to_delete_post.author.id, user2.id)
        self.assertEqual(to_delete_post.title, "Some Title")
        self.assertEqual(to_delete_post.description, "Some Description")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
