# -*- coding: utf-8 -*-
# @Author: sahildua2305
# @Date:   2016-05-15 05:26:34
# @Last Modified by:   Sahil Dua
# @Last Modified time: 2016-05-16 00:00:36

import os, json
import requests
import unittest
import tempfile

class PlinoAppTestCase(unittest.TestCase):

    api_url = "http://localhost:8000/api/v1/classify/"

    def setUp(self):
        pass

    def tearDown(self):
        pass

    """
    Unit test to verify the 400 response code when no email_text is present in the request to API endpoint
    """
    def test_api_no_email_text(self):
        payload = {}
        headers = {'content-type': 'application/json'}
        response = requests.post(self.api_url, data=json.dumps(payload), headers=headers)
        assert response.status_code == 400

    """
    Unit test to verify the 200 response code and the correct email_class returned by API when a spam email text is passed
    """
    def test_api_spam_email_text(self):
        payload = {
            'email_text': 'Dear Tasdik, I would like to immediately transfer 10000 thousand dollars to your account as my beloved husband has expired and I have nobody to ask for to transfer the money to your account. I come from the family of the royal prince of burkino fasa and I would be more than obliged to take your help on this matter. Would you care to share your bank account details with me in the next email conversation that we have? -regards -Liah herman'
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(self.api_url, data=json.dumps(payload), headers=headers)
        r = json.loads(response.content)
        assert response.status_code == 200
        assert r['email_class'] == 'spam'

    """
    Unit test to verify the 200 response code and the correct email_class returned by API when a non-spam email text is passed
    """
    def test_api_ham_email_text(self):
        payload = {
            'email_text': 'Dear Students PFA..The B.Tech IT Minor Project Final review is scheduled on 7/5/2016 and 9/5/2016.While coming for final review, students should complete the 100% project and need to show the full project demo.'
        }
        headers = {'content-type': 'application/json'}
        response = requests.post(self.api_url, data=json.dumps(payload), headers=headers)
        assert response.status_code == 200
        r = json.loads(response.content)
        assert r['email_class'] == 'ham'


if __name__ == '__main__':
    unittest.main()
