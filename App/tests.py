from django.test import TestCase, Client
from .models import *
# Create your tests here.

User = get_user_model()
class Test_post(TestCase):

	def setUp(self):
		user = User.objects.create_user(username="jack", email="jack@gmail.com", password="12345")
		user.is_active = True
		Entry.objects.create(user=user, entry="How are you it is 1-dec")
		Entry.objects.create(user=user, entry="How are you it -dec")
		Entry.objects.create(user=user, entry="How are you-dec")

	def test_post(self):
		user = User.objects.get(username="jack")
		self.assertEqual(user.entry.count(),3)

	def test_home(self):
		c = Client()
		response = c.get("")
		self.assertEqual(response.status_code, 200)
		#self.assertTrue(response.context["User"].is_authenticated)
