import json
from lambda.handler import lambda_handler

def test_lambda_handler_success():
    event = {"body": json.dumps({"hello": "world"})}
    result = lambda_handler(event, None)
    assert result["statusCode"] == 200
    assert json.loads(result["body"]) == {"hello": "world"}