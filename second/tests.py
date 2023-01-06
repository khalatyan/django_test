from django.test import TestCase
from django.core.exceptions import ValidationError

from second.models import Lead, LeadState



class LeadTest(TestCase):

    def create_lead_object(self, name='first_lead_test_obj'):
        return Lead.objects.create(name=name)

    def create_lead_status_object(self, name='STATE_NEW'):
        return LeadState.objects.create(name=name)

    def test_create_lead_object(self):
        new_status = LeadState.objects.create(name='STATE_NEW')

        obj = self.create_lead_object()
        self.assertEqual(obj.state, new_status)

    def test_update_to_valid_statuses(self):
        new_status = self.create_lead_status_object(name='STATE_NEW')
        in_progress_status = self.create_lead_status_object(name='STATE_IN_PROGRESS')
        postponed_status = self.create_lead_status_object(name='STATE_POSTPONED')
        done_status = self.create_lead_status_object(name='STATE_DONE')

        obj = self.create_lead_object()

        obj.state = in_progress_status
        obj.save()
        self.assertEqual(obj.state, in_progress_status)

        obj.state = postponed_status
        obj.save()
        self.assertEqual(obj.state, postponed_status)

        obj.state = done_status
        obj.save()
        self.assertEqual(obj.state, done_status)

    def test_update_to_invalid_statuses(self):
        new_status = self.create_lead_status_object(name='STATE_NEW')
        in_progress_status = self.create_lead_status_object(name='STATE_IN_PROGRESS')
        postponed_status = self.create_lead_status_object(name='STATE_POSTPONED')
        done_status = self.create_lead_status_object(name='STATE_DONE')

        obj = self.create_lead_object()

        obj.state = done_status
        with self.assertRaises(ValidationError):
            obj.save()

        obj.state = postponed_status
        with self.assertRaises(ValidationError):
            obj.save()

        #Дальше другие тесты нужно написать
