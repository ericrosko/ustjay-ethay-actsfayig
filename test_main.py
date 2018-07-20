#!/usr/bin/env python3

import unittest
import requests
from bs4 import BeautifulSoup

"""
python3 -m unittest -v
./test_main.py -v
"""

class Assignment05TextCase(unittest.TestCase):
    """test for meme generator mashup"""

    def setUp(self):
        self.maxDiff = None

    def tearDown(self):
        pass


    def test_post_from_first_page_no_redirect(self):
        """
        This 301 tells us that we must submit the form field to the
        /piglatinize/ url.  Subitting the form to the given root url
        will not accept the form and just give us a 405 status code.
        """
        url = "http://hidden-journey-62459.herokuapp.com/piglatinize"
        params = {'input_text': 'Hello World'}
        response = requests.post(url, data=params, allow_redirects=False)
        print("CONTENT:", response.content)
        print("Status Code:", response.status_code)
        print("Headers:", response.headers)
        self.assertEqual(301, response.status_code)

        expected = b'<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">\n<title>Redirecting...</title>\n<h1>Redirecting...</h1>\n<p>You should be redirected automatically to target URL: <a href="http://hidden-journey-62459.herokuapp.com/piglatinize/">http://hidden-journey-62459.herokuapp.com/piglatinize/</a>.  If not click the link.'
        self.assertEqual(expected, response.content)


    def test_post(self):
        """
        This is how we can get a response and also get needed url
        """
        import requests
        url = 'https://hidden-journey-62459.herokuapp.com/piglatinize/'
        params = {'input_text': 'Hello World'}

        response = requests.post(url, data=params)

        expected = b'<html>\n<head>\n<title>Pig Latin</title>\n</head>\n<body>\n\t<h1>Pig Latin</h1>\n\t<h2>Esultray</h2>\n\t\n    elloHay orldWay\n\n</body>\n</html>'
        # print("CONTENT:", response.content)
        self.assertEqual(200, response.status_code)
        # print("Headers:", response.headers)
        self.assertEqual(expected, response.content)

        expected_url = "http://hidden-journey-62459.herokuapp.com/esultray/b10a8db164e0754105b7a99be72e3fe5/"
        self.assertEqual(expected_url, response.url)


    def test_second(self):
        """
        This shows how we can parse the body to grab the piglatinized text
        """
        url = "http://hidden-journey-62459.herokuapp.com/esultray/b10a8db164e0754105b7a99be72e3fe5/"
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")
        quote = soup.find("body")

        print(quote)
        print()
        print(type(quote))
        body = str(soup.body)
        print()
        h2_tag = '/h2>'
        start_pos = body.find(h2_tag)
        start_pos += len(h2_tag)
        end_pos = body.find('</body')
        result = body[start_pos: end_pos].strip()

        self.assertEqual('elloHay orldWay', result)


if __name__ == '__main__':
    unittest.main()
