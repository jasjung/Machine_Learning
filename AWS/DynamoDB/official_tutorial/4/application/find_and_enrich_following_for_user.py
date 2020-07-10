import boto3

from entities import User

dynamodb = boto3.client("dynamodb")

USERNAME = "haroldwatkins"


def find_and_enrich_following_for_user(username):
    friend_value = "#FRIEND#{}".format(username)
    resp = dynamodb.query(
        TableName="quick-photos",
        IndexName="InvertedIndex",
        KeyConditionExpression="SK = :sk",
        ExpressionAttributeValues={":sk": {"S": friend_value}},
        ScanIndexForward=True,
    )

    keys = [
        {
            "PK": {"S": "USER#{}".format(item["followedUser"]["S"])},
            "SK": {"S": "#METADATA#{}".format(item["followedUser"]["S"])},
        }
        for item in resp["Items"]
    ]

    friends = dynamodb.batch_get_item(RequestItems={"quick-photos": {"Keys": keys}})

    enriched_friends = [User(item) for item in friends["Responses"]["quick-photos"]]

    return enriched_friends


follows = find_and_enrich_following_for_user(USERNAME)

print("Users followed by {}:".format(USERNAME))
for follow in follows:
    print(follow)
