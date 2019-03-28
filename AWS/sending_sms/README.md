# SNS - send text msg 

```py 
def send_msg(msg,number): 
    print('sending sns')
    # Create an SNS client
    client = boto3.client(
        "sns",
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name="us-west-2"
    )
    # Send your sms message.
    client.publish(
        PhoneNumber=number,
        Message=msg
    )

send_msg('hello','+13103339999')
```
