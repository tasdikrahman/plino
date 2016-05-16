# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-05-15 05:26:34
# @Last Modified by:   Tasdik Rahman
# @Last Modified time: 2016-05-16 11:50:36

import json
import unittest

import requests

from constants import HAM_TEXT, SPAM_TEXT


class PlinoAppTestCase(unittest.TestCase):

    api_url = "http://localhost:8000/api/v1/classify/"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_api_no_email_text(self):
        """
        Unit test to verify the 400 response code when no email_text is present
        in the request to API endpoint
        """
        payload = {}
        headers = {'content-type': 'application/json'}
        response = \
            requests.post(self.api_url, data=json.dumps(payload), headers=headers)
        assert response.status_code == 400


    def test_api_spam_email_text(self):
        """
        Unit test to verify the 200 response code and the correct email_class
        returned by API when a spam email text is passed
        """
        payload = {
            'email_text': SPAM_TEXT
        }
        headers = {'content-type': 'application/json'}
        response = \
            requests.post(self.api_url, data=json.dumps(payload), headers=headers)
        r = json.loads(response.content)
        assert response.status_code == 200
        assert r['email_class'] == 'spam'


    def test_api_ham_email_text(self):
        """
        Unit test to verify the 200 response code and the correct email_class
        returned by API when a non-spam email text is passed
        """
        payload = {
            'email_text': HAM_TEXT
        }
        headers = {'content-type': 'application/json'}
        response = \
            requests.post(self.api_url, data=json.dumps(payload), headers=headers)
        assert response.status_code == 200
        r = json.loads(response.content)
        assert r['email_class'] == 'ham'


if __name__ == '__main__':
    unittest.main()
