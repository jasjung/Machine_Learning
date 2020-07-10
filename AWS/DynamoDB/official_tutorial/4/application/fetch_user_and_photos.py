import boto3

from entities import User, Photo

dynamodb = boto3.client('dynamodb')

USER = "jacksonjason"


def fetch_user_and_photos(username):
    resp = dynamodb.query(
        TableName='quick-photos',
        KeyConditionExpression="PK = :pk AND SK BETWEEN :metadata AND :photos",
        ExpressionAttributeValues={
            ":pk": { "S": "USER#{}".format(username) },
            ":metadata": { "S": "#METADATA#{}".format(username) },
            ":photos": { "S": "PHOTO$" },
        },
        ScanIndexForward=True
    )

    user = User(resp['Items'][0])
    user.photos = [Photo(item) for item in resp['Items'][1:]]

    return user


user = fetch_user_and_photos(USER)

print(user)
for photo in user.photos:
    print(photo)

