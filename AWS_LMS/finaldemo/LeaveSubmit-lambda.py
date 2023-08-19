import boto3
import json
import uuid

s3_client = boto3.client('s3')
ses_client = boto3.client('ses')
sns_client = boto3.client('sns')

def parse_leave_data(body):
    try:
        # Implement your logic to parse the leave request data from the body
        # Assuming the body is a JSON string, you can use json.loads to parse it
        leave_data = json.loads(body)

        # Example parsing logic
        name = leave_data.get('employeeName')
        email = leave_data.get('employeeEmail')
        leave_type = leave_data.get('leaveType')
        start_date = leave_data.get('startDate')
        end_date = leave_data.get('endDate')
        reason = leave_data.get('reason')

        # Return the parsed leave request data as a dictionary
        return {
            'name': name,
            'email': email,
            'leaveType': leave_type,
            'startDate': start_date,
            'endDate': end_date,
            'reason': reason
        }
    except Exception as e:
        print(f"Error parsing leave data: {e}")
        raise

def validate_leave_data(leave_data):
    # Check if required fields are present
    required_fields = ['name', 'email', 'leaveType', 'startDate', 'endDate', 'reason']
    for field in required_fields:
        if field not in leave_data:
            return False
    
    # Perform additional validation if needed
    # For example, you can check if the start date is before the end date
    start_date = leave_data['startDate']
    end_date = leave_data['endDate']
    if start_date > end_date:
        return False
    
    # All validation checks passed, return True
    return True
    
def generate_leave_id():
    # Generate a unique leave ID using UUID
    return str(uuid.uuid4())    

def submit_leave_request(event, context):
    try:
        # Parse and validate leave request details from the event data
        leave_data = parse_leave_data(event['body'])
        if not validate_leave_data(leave_data):
            return {
                'statusCode': 400,
                'body': 'Invalid leave request data'
            }

        # Generate a unique leave ID
        leave_id = generate_leave_id()

        # Store the leave request data in S3
        s3_client.put_object(
            Bucket='leavemanagement',
            Key=f'leaves/{leave_id}.json',
            Body=json.dumps(leave_data)
        )

        
        sns_client.publish(
            TopicArn='arn:aws:sns:us-east-1:828082488998:leave-notifications',
            Message=json.dumps({
            'leave_id': leave_id,
            'leave_data': leave_data
    })
)

    
        # lambda_client = boto3.client('lambda')
        # # lambda_client.invoke(
        # #     FunctionName='NotifyLeave',
        # #     InvocationType='Event',
        # #     Payload=json.dumps({'leave_id': leave_id})
        # # )
        
        # Send confirmation email to the employee
        send_confirmation_email(leave_data['email'])

        return {
            'statusCode': 200,
            'body': 'Leave request submitted successfully'
        }
    except Exception as e:
        print(f"Error submitting leave request: {e}")
        raise


def send_confirmation_email(email):
    # Create and send the confirmation email using SES
    ses_client.send_email(
        Source='shreyaspuranik008@gmail.com',
        Destination={
            'ToAddresses': [email]
        },
        Message={
            'Subject': {
                'Data': 'Leave Request Confirmation'
            },
            'Body': {
                'Text': {
                    'Data': 'Hello , your Leave request is successfully submitted . Please wait for manager to review and approve your request.'
                }
            }
        }
    )
    
