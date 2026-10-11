from django.test import TestCase
from django.urls import reverse


class TemplatePageTests(TestCase):
	def test_home_renders_project_template(self):
		response = self.client.get(reverse('tenant:home'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'home.html')
		self.assertTemplateUsed(response, 'base.html')
		self.assertContains(response, 'Tenant portal')

	def test_tenant_list_renders_app_template(self):
		response = self.client.get(reverse('tenant:list'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'tenant/index.html')
		self.assertTemplateUsed(response, 'base.html')
		self.assertContains(response, 'Tenant directory')
