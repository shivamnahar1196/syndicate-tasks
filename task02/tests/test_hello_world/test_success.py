import unittest
import json
from unittest.mock import Mock
from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        # Prepare a mock event with a valid path and method
        event = {
            'requestContext': {
                'http': {
                    'path': '/hello',
                    'method': 'GET'
                }
            }
        }
        context = Mock()  # You can mock the context as needed

        # Call the handle_request method with the valid event and context
        response = self.HANDLER.handle_request(event, context)

        # Assert that the response has statusCode 200
        self.assertEqual(response["statusCode"], 200)

        # Assert that the message is correct for the valid request
        response_body = json.loads(response["body"])
        self.assertEqual(response_body["message"], "Hello from Lambda")

    def test_bad_request(self):
        # Prepare a mock event with an invalid path and method
        event = {
            'requestContext': {
                'http': {
                    'path': '/invalid-path',
                    'method': 'POST'
                }
            }
        }
        context = Mock()  # Mock the context for testing

        # Call the handle_request method with the invalid event and context
        response = self.HANDLER.handle_request(event, context)

        # Assert that the response has statusCode 400
        self.assertEqual(response["statusCode"], 400)

        # Assert that the message contains details about the invalid request
        response_body = json.loads(response["body"])
        self.assertIn("Bad request syntax or unsupported method", response_body["message"])
        self.assertIn("Request path: /invalid-path", response_body["message"])
        self.assertIn("HTTP method: POST", response_body["message"])