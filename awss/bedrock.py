import boto3
import json

def prompt_bedrock(prompt_text, model_id):
    payload = {
        "inputText": prompt_text,
        "textGenerationConfig": {
            "temperature": 0.5,
            "topP": 0.9,
            "maxTokenCount": 64,
            "stopSequences": []
        }
    }

    client = boto3.client('bedrock-runtime')

    response = client.invoke_model(
        modelId=model_id,
        body=json.dumps(payload),
        contentType='application/json',
        accept='application/json'
    )

    response_body = json.loads(response['body'].read().decode('utf-8'))
    return response_body

if __name__ == "__main__":
    prompt_text = "tell a crazy story."
    model_id = "amazon.titan-text-premier-v1:0"
    result = prompt_bedrock(prompt_text, model_id)
    print(result)