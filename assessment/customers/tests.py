from django.test import TestCase
from assessment.fetch_users import parse_user_data
from assessment.customers.mock import mifos_users_response, excepted_user_list


class CustomerTests(TestCase):
    def test_filter_function(self):
        list_user = parse_user_data(mifos_users_response)
        self.assertEquals(list_user, excepted_user_list)
