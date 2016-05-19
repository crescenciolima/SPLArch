from django.core.urlresolvers import reverse
from django.test import TestCase
from SPLArch.requirement.models import *


class RequirementTypeTestCase(TestCase):
    def setUp(self):
        self.requirement_type1 = RequirementType.objects.create(name='Functional Requirements',)
        self.requirement_type1.save()
        self.model = self.requirement_type1

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


class RequirementTestCase(TestCase):
    def setUp(self):
        self.requirement1 = Requirement.objects.create(
            name='Add Contact',
            requirement_type=RequirementType.objects.create(name='Functional Requirements'),
            priority=PriorityRequirement.objects.create(name='low', level=1),
            status_requirement_choices='proposed'
        )
        self.requirement1.save()
        self.model = self.requirement1

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


class UseCaseTestCase(TestCase):
    def setUp(self):
        self.use_case1 = UseCase.objects.create(
            title='Send a SMS rescue message',
        )
        self.use_case1.save()
        self.model = self.use_case1

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
