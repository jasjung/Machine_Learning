import datetime

import boto3

dynamodb = boto3.client("dynamodb")

FOLLOWED_USER = "tmartinez"
FOLLOWING_USER = "john42"


def follow_user(followed_user, following_user):
    user = "USER#{}".format(followed_user)
    friend = "#FRIEND#{}".format(following_user)
    user_metadata = "#METADATA#{}".format(followed_user)
    try:
        resp = dynamodb.transact_write_items(
            TransactItems=[
                {
                    "Put": {
                        "TableName": "quick-photos",
                        "Item": {
                            "PK": {"S": user},
                            "SK": {"S": friend},
                            "followedUser": {"S": followed_user},
                            "followingUser": {"S": following_user},
                            "timestamp": {"S": datetime.datetime.now().isoformat()},
                        },
                        "ConditionExpression": "attribute_not_exists(SK)",
                        "ReturnValuesOnConditionCheckFailure": "ALL_OLD",
                    }
                },
                {
                    "Update": {
                        "TableName": "quick-photos",
                        "Key": {"PK": {"S": user}, "SK": {"S": user_metadata}},
                        "UpdateExpression": "SET followers = followers + :i",
                        "ExpressionAttributeValues": {":i": {"N": "1"}},
                        "ReturnValuesOnConditionCheckFailure": "ALL_OLD",
                    }
                },
                {
                    "Update": {
                        "TableName": "quick-photos",
                        "Key": {"PK": {"S": user}, "SK": {"S": user_metadata}},
                        "UpdateExpression": "SET following = following + :i",
                        "ExpressionAttributeValues": {":i": {"N": "1"}},
                        "ReturnValuesOnConditionCheckFailure": "ALL_OLD",
                    }
                },
            ]
        )
        print("User {} is now following user {}".format(following_user, followed_user))
        return True
    except Exception as e:
        print("Could not add follow relationship")


follow_user(FOLLOWED_USER, FOLLOWING_USER)
