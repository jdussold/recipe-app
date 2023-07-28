from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages


class AuthViewsTest(TestCase):
    def setUp(self):
        self.username = "testuser"
        self.password = "testpassword123"
        self.user = User.objects.create_user(self.username, password=self.password)

    def test_login_get(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "auth/login.html")

    def test_valid_login_post(self):
        response = self.client.post(
            reverse("login"), {"username": self.username, "password": self.password}
        )

        self.assertRedirects(response, reverse("recipes:recipes_list"))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), f"You are now logged in as {self.username}.")

    def test_invalid_login_post(self):
        response = self.client.post(
            reverse("login"), {"username": self.username, "password": "wrongpassword"}
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Invalid username or password.")

    def test_logout(self):
        # First, login the user
        self.client.login(username=self.username, password=self.password)

        response = self.client.get(reverse("logout"))
        self.assertRedirects(response, reverse("success"))

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "You've successfully logged out.")
