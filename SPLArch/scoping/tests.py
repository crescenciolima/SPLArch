from django.core.urlresolvers import reverse
from django.test import TestCase
from SPLArch.scoping.models import *
from django.core.urlresolvers import resolve


class LoginTestCase(TestCase):
    def test_response(self):
        response = self.client.get('/admin/login/')
        self.assertEqual(response.status_code, 200)




class ProductTestCase(TestCase):
    def setUp(self):
        self.product1 = Product.objects.create(
            name='RescueMe Ultimate',
            description='The most complete RescueMe product',
        )
        self.product1.save()

        self.model = self.product1

    def test_string_representation(self):
        self.assertEqual(str(self.product1), self.product1.name)

    def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)


class ProjectTestCase(TestCase):
    def setUp(self):
        self.project1 = Project.objects.create(name="RescueMe")
        self.project1.save()
        self.model = self.project1

    def test_string_representation(self):
        self.assertEqual(str(self.project1), self.project1.name)

    def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)


class GlossaryTestCase(TestCase):
    def setUp(self):
        self.glossary1 = Glossary.objects.create(
            term='Global Positioning System (GPS)',
            definition='The Global Positioning System (GPS) is a space-based satellite navigation'
        )
        self.glossary1.save()
        self.model = self.glossary1

    def test_string_representation(self):
        self.assertEqual(str(self.model), self.model.term)

    def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)


class FeatureTestCase(TestCase):
    def setUp(self):
        self.feature1 = Feature.objects.create(
            name='How To Use',
            description='The application shows its functionalities in a "step-by-step" way. a',
            variability='optional',
            type='concrete',
            binding_time=BindingTime.objects.create(
                name='Compile time'
            ),
        )
        self.feature1.save()
        self.model = self.feature1

    def test_string_representation(self):
        self.assertEqual(str(self.model), "#" + str(self.feature1.id) + " " + self.feature1.name)

    def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)


class BindingTimeTestCase(TestCase):
    def setUp(self):
        self.binding_time1 = BindingTime.objects.create(name='Compile time')
        self.binding_time1.save()
        self.model = self.binding_time1

    def test_string_representation(self):
        self.assertEqual(str(self.model), self.model.name)

    def test_response(self):
        url = reverse("admin:%s_%s_add" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_change" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_delete" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_history" % (self.model._meta.app_label, self.model._meta.module_name),
                      args=[self.model.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)

        url = reverse("admin:%s_%s_changelist" % (self.model._meta.app_label, self.model._meta.module_name))
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)


