import json
import boto3
import email_validator
from uuid import uuid4
import  os

# Initialize AWS DynamoDB client
dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('DB_TABLE', '')
table = dynamodb.Table(table_name)

def handler(event, context):
    body = json.loads(event['body'])
    print(body)

    validation_errors = validate_input(body)

    if validation_errors is not None:
        return validation_errors

    pk = str(uuid4())

    item = {
        'pk': pk,
        'type': 'leaveRequest',
        'from': body['applicantEmail'],
        'to': body['approverEmail'],
        'reason': body['reason'],
        'leaveDateFrom': body['leaveStartDate'],
        'leaveDateTo': body['leaveEndDate'],
        'status': 'pending'
    }

    try:
        table.put_item(Item=item)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Candidate created',
                'data': {
                    'id': pk
                }
            })
        }
    except Exception as e:
        print('Error:', str(e))

        return {
            'statusCode': 500,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Candidate creation failed',
                'error': str(e)
            })
        }


def validate_input(body):
    errors = []

    if not email_validator.validate_email(body['applicantEmail']):
        errors.append('Required field applicantEmail not found or invalid')

    if not email_validator.validate_email(body['approverEmail']):
        errors.append('Required field approverEmail not found or invalid')

    if 'leaveStartDate' not in body:
        errors.append('Required field leaveStartDate not found or invalid')

    if 'leaveEndDate' not in body:
        errors.append('Required field leaveEndDate not found or invalid')

    if 'reason' not in body:
        errors.append('Required field reason not found or invalid')

    if errors:
        return {
            'statusCode': 422,
            'headers': {
                'Content-Type': 'application/json'
            },
            'body': json.dumps({
                'message': 'Validation errors',
                'errors': errors
            })
        }

    return None
