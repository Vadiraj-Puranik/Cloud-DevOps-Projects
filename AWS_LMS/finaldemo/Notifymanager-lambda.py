import boto3
import json

ses_client = boto3.client('ses')
sns_client = boto3.client('sns')


def notify_manager(event, context):
    try:
        # Extract the leave data from the SNS event
        sns_message = event['Records'][0]['Sns']
        message = json.loads(sns_message['Message'])
        leave_data = message['leave_data']
        leave_id = message['leave_id']
        print(leave_data)


        # Send notification email to the manager
        send_notification_email(leave_data, leave_id)

        return {
            'statusCode': 200,
            'body': 'Manager notified successfully'
        }
    except Exception as e:
        print(f"Error notifying manager: {e}")
        raise

def send_notification_email(leave_data, leave_id):
    # Create the email content
    manager_email = 'puranikvadiraj12@gmail.com'  # Replace with the actual manager's email
    subject = 'Leave Request Approval'
    message = f"Leave request submitted by {leave_data['name']} from {leave_data['startDate']} to {leave_data['endDate']}\n\nPlease visit the following URLs to approve or reject the leave request:\n\nApproval: https://eyzsr82rsb.execute-api.us-east-1.amazonaws.com/hcmsgco/lambdatrigger?leave_id={leave_id}&status=approved\nRejection: https://g1fcdo2wul.execute-api.us-east-1.amazonaws.com/management/reject?leave_id={leave_id}"

    # Send the notification email using SES
    ses_client.send_email(
        Source='shreyaspuranik008@gmail.com',
        Destination={
            'ToAddresses': [manager_email]
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




















































# import json
# import boto3

# ses_client = boto3.client('ses')
# lambda_function_url = 'https://d53cish225aaoefwchlp443ufy0kiwvq.lambda-url.us-east-1.on.aws/'

# def send_approval_email(leave_id, manager_email):
#     # Compose the URLs with leave ID
#     approve_url = f"{lambda_function_url}approve/{leave_id}"
#     reject_url = f"{lambda_function_url}reject/{leave_id}"

#     # Compose the email body with the URLs
#     email_body = f"Dear manager,\n\nYou have a leave request that requires your approval. Please click on the appropriate link below:\n\nApprove: {approve_url}\nReject: {reject_url}\n\nBest regards,\nLeave Management System"

#     # Send the email to the manager
#     response = ses_client.send_email(
#         Source='shreyaspuranik008@gmail.com',
#         Destination={
#             'ToAddresses': [manager_email]
#         },
#         Message={
#             'Subject': {
#                 'Data': 'Leave Request Approval'
#             },
#             'Body': {
#                 'Text': {
#                     'Data': email_body
#                 }
#             }
#         }
#     )

#     return response

# def notify_manager(event, context):
#     # Retrieve the leave ID from the event
#     leave_id = event['leave_id']

#     # Retrieve the manager email from the event (replace with your own logic to fetch manager email)
#     manager_email = 'puranikvadiraj12@gmail.com'

#     # Send the approval email to the manager
#     response = send_approval_email(leave_id, manager_email)

#     # Return a response
#     response_body = {
#         'message': 'Approval email sent successfully'
#     }
#     return {
#         'statusCode': 200,
#         'headers': {
#             'Content-Type': 'application/json'
#         },
#         'body': json.dumps(response_body)
#     }






































# import json
# import boto3

# ses_client = boto3.client('ses')

# def send_approval_email(leave_id, manager_email):
#     # Compose the URLs with leave ID
#     approve_url = f"https://g1fcdo2wul.execute-api.us-east-1.amazonaws.com/Development/approve/{leave_id}"
#     reject_url = f"https://g1fcdo2wul.execute-api.us-east-1.amazonaws.com/Development/reject/{leave_id}"

#     # Compose the email body with the URLs
#     email_body = f"Dear Vadiraj,\n\nYou have a leave request that requires your approval. Please click on the appropriate link below:\n\nApprove: {approve_url}\nReject: {reject_url}\n\nBest regards,\nLeave Management System"

#     # Send the email to the manager
#     response = ses_client.send_email(
#         Source='shreyaspuranik008@gmail.com',
#         Destination={
#             'ToAddresses': [manager_email]
#         },
#         Message={
#             'Subject': {
#                 'Data': 'Leave Request Approval'
#             },
#             'Body': {
#                 'Text': {
#                     'Data': email_body
#                 }
#             }
#         }
#     )

#     return response

# def notify_manager(event, context):
#     # Retrieve the leave ID from the event
#     leave_id = event['leave_id']

#     # Retrieve the manager email from the event (replace with your own logic to fetch manager email)
#     manager_email = 'puranikvadiraj12@gmail.com'

#     # Send the approval email to the manager
#     response = send_approval_email(leave_id, manager_email)

#     # Return a response
#     response_body = {
#         'message': 'Approval email sent successfully'
#     }
#     return {
#         'statusCode': 200,
#         'headers': {
#             'Content-Type': 'application/json'
#         },
#         'body': json.dumps(response_body)
#     }


































import boto3
import json

ses_client = boto3.client('ses')
sns_client = boto3.client('sns')


def notify_manager(event, context):
    try:
        # Extract the leave data from the SNS event
        sns_message = event['Records'][0]['Sns']
        message = json.loads(sns_message['Message'])
        leave_data = message['leave_data']
        leave_id = message['leave_id']
        print(leave_data)


        # Send notification email to the manager
        send_notification_email(leave_data, leave_id)

        return {
            'statusCode': 200,
            'body': 'Manager notified successfully'
        }
    except Exception as e:
        print(f"Error notifying manager: {e}")
        raise

def send_notification_email(leave_data, leave_id):
    # Create the email content
    manager_email = 'puranikvadiraj12@gmail.com'  # Replace with the actual manager's email
    subject = 'Leave Request Approval'
    message = f"Leave request submitted by {leave_data['name']} from {leave_data['startDate']} to {leave_data['endDate']}\n\nPlease visit the following URLs to approve or reject the leave request:\n\nApproval: https://eyzsr82rsb.execute-api.us-east-1.amazonaws.com/hcmsgco/lambdatrigger?leave_id={leave_id}&status=approved\nRejection: https://g1fcdo2wul.execute-api.us-east-1.amazonaws.com/management/reject?leave_id={leave_id}"

    # Send the notification email using SES
    ses_client.send_email(
        Source='shreyaspuranik008@gmail.com',
        Destination={
            'ToAddresses': [manager_email]
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






























