import boto3

from entities import Friendship

dynamodb = boto3.client('dynamodb')

USERNAME = "haroldwatkins"


def find_following_for_user(username):
    resp = dynamodb.query(
        TableName='quick-photos',
        IndexName='InvertedIndex',
        KeyConditionExpression="SK = :sk",
        ExpressionAttributeValues={
            ":sk": { "S": "#FRIEND#{}".format(username) }
        },
        ScanIndexForward=True
    )

    return [Friendship(item) for item in resp['Items']]



follows = find_following_for_user(USERNAME)

print("Users followed by {}:".format(USERNAME))
for follow in follows:
    print(follow)
