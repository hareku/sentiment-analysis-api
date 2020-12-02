import json
import os
import pickle
import tokenizer

def predict(text):
    with open(os.path.join(os.getcwd(), 'models/vectorizer.pickle'), mode='rb') as vf, open(os.path.join(os.getcwd(), 'models/bayes.pickle'), mode='rb') as bf:
        vectorizer = pickle.load(vf)
        clf = pickle.load(bf)

        vec = vectorizer.transform([text])
        proba = clf.predict_proba(vec)
        return proba

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

    query = event['queryStringParameters']
    if query is None or 'sentence' not in query:
        return {
            'statusCode': 422,
            'headers': {
                'Content-Type': 'application/json',
            },
            'body': json.dumps({'message': 'please add "sentence" query'})
        }

    proba = predict(query['sentence'])[0]

    res_body = {
        'result': {
            'Positive': proba[0],
            'Negative': proba[1],
            'Neutral': proba[2],
        }
    }

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
        },
        'body': json.dumps(res_body)
    }
