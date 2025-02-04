# from tests.test_hello_world import HelloWorldLambdaTestCase
#
#
# class TestSuccess(HelloWorldLambdaTestCase):
#
#     def test_success(self):
#         self.assertEqual(self.HANDLER.handle_request(dict(), dict()), 200)


from tests.test_hello_world import HelloWorldLambdaTestCase


class TestSuccess(HelloWorldLambdaTestCase):

    def test_success(self):
        # Call the handle_request method with dummy event and context
        response = self.HANDLER.handle_request(dict(), dict())

        # Assert that the response has statusCode 200
        self.assertEqual(response["statusCode"], 200)

        # Optionally, you can also check the message if you want
        self.assertEqual(response["message"], "Hello from Lambda")
