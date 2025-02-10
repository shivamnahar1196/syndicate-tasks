from commons.log_helper import get_logger
from commons.abstract_lambda import AbstractLambda
import json

_LOG = get_logger(__name__)


class HelloWorld(AbstractLambda):

    def validate_request(self, event) -> dict:
        pass
        
    def handle_request(self, event, context):
        """
        Explain incoming event here
        """
        # todo implement business logic
        path = event['requestContext']['http']['path']
        method = event['requestContext']['http']['method']

        if '/hello' in path and method == 'GET':
            response = {
                "statusCode": 200,
                "message": "Hello from Lambda"
            }
        else:
            response = {
                "statusCode": 400,
                "message": f"Bad request syntax or unsupported method. Request path: {path}. HTTP method: {method}"
            }

        return {
            "statusCode": response["statusCode"],
            "body": json.dumps(response)
        }
    

HANDLER = HelloWorld()


def lambda_handler(event, context):
    return HANDLER.lambda_handler(event=event, context=context)
