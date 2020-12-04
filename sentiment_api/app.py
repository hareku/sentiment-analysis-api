import json
import os
import pickle
import tokenizer

vectorizer = pickle.load(open(os.path.join(os.getcwd(), 'models/vectorizer.pickle'), mode='rb'))
bayes = pickle.load(open(os.path.join(os.getcwd(), 'models/bayes.pickle'), mode='rb'))

def predict_proba(textList):
    return bayes.predict_proba(vectorizer.transform(textList))

def lambda_handler(event, context):
    """Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    body = json.loads(event['body'])
    if 'TextList' not in body or not isinstance(body['TextList'], list):
        return {
            'statusCode': 422,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps({'message': 'The request body must habe "TextList" to analyze.'})
        }

    proba = predict_proba(body['TextList'])
    result = []
    for p in proba:
        result.append({
            'Positive': p[0],
            'Negative': p[1],
            'Neutral': p[2],
        })

    res_body = {
        'result': result
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(res_body)
    }
