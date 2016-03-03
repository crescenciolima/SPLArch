from django.core.urlresolvers import reverse
from django.test import TestCase
from SPLArch.scoping.models import *
from SPLArch.architecture.models import *
from django.test import TestCase


class ReferencesTestCase(TestCase):
    def setUp(self):
        self.references1 = References.objects.create(
            title='Professional Android 4 Application Development',
            author='Reto Meier',
            description='',
            number=345,
            year=2012,
            volume=2
        )
        self.references1.save()
        self.model = self.references1

    def test_string_representation(self):
        self.assertEqual(str(self.references1), self.references1.title)

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


class DDSATestCase(TestCase):
    def setUp(self):
        self.ddsa1 = DDSA.objects.create()
        self.ddsa1.save()
        self.model = self.ddsa1

    def test_string_representation(self):
        self.assertEqual(str(self.ddsa1), self.ddsa1.name)

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


class ScenariosTestCase(TestCase):
    def setUp(self):
        self.scenarios1 = Scenarios.objects.create(name='')
        self.scenarios1.save()
        self.model = self.scenarios1

    def test_string_representation(self):
        self.assertEqual(str(self.scenarios1), self.scenarios1.name)

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

class APITestCase(TestCase):
    def setUp(self):
        self.api1 = API.objects.create(name='')
        self.api1.save()
        self.model = self.api1

    def test_string_representation(self):
        self.assertEqual(str(self.api1), self.api1.name)

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

