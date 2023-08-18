import boto3
import json

s3_client = boto3.client('s3')
ses_client = boto3.client('ses')

BUCKET_NAME = 'leavemanagement'
LEAVES_FOLDER = 'leaves/'

def handle_approval(event, context):
    try:
        leave_id = event['queryStringParameters']['leave_id']
        status = event['queryStringParameters']['status']
        
        
        # leave_id = event['queryStringParameters']['leave_id']
        # # Update the status of the leave request in S3 with the leave_id
        update_leave_status(leave_id, status)
        
        # Get the user's email based on the leave_id
        leave_data = get_leave_data(leave_id)
        user_email = leave_data['email']
        
        # Send a notification email to the user about the approval
        send_notification_email(user_email, 'approved')

        return {
            'statusCode': 200,
            'body': 'Approval processed successfully'
        }
    except Exception as e:
        print(f"Error processing approval: {e}")
        raise


def update_leave_status(leave_id, status):
    # Retrieve the leave data from S3 based on the leave_id
    leave_key = f"{LEAVES_FOLDER}{leave_id}.json"
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=leave_key)
    leave_data = json.loads(response['Body'].read())
    
    # Update the status field with the provided status value
    leave_data['status'] = status
    
    # Save the updated leave data back to S3
    s3_client.put_object(
        Bucket=BUCKET_NAME,
        Key=leave_key,
        Body=json.dumps(leave_data)
    )


def get_leave_data(leave_id):
    # Retrieve the leave data from S3 based on the leave_id
    leave_key = f"{LEAVES_FOLDER}{leave_id}.json"
    response = s3_client.get_object(Bucket=BUCKET_NAME, Key=leave_key)
    leave_data = json.loads(response['Body'].read())
    
    return leave_data


def send_notification_email(email, status):
    # Create the email content
    subject = f'Leave Request {status.capitalize()}'
    message = f"Your leave request has been {status}."
    
    # Send the notification email using SES
    ses_client.send_email(
        Source='shreyaspuranik008@gmail.com',
        Destination={
            'ToAddresses': [email]
        },
        Message={
            'Subject': {
                'Data': subject
            },
            'Body': {
                'Text': {
                    'Data': message
                }
            }
        }
    )
