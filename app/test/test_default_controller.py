# coding: utf-8

from __future__ import absolute_import

from app.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_blog_get(self):
        """Test case for blog_get

        
        """
        response = self.client.open(
            '/lylswqr/MobileMonitor/1/blog',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
