import datetime

import boto3

dynamodb = boto3.client("dynamodb")

REACTING_USER = "kennedyheather"
REACTION_TYPE = "sunglasses"
PHOTO_USER = "ppierce"
PHOTO_TIMESTAMP = "2019-04-14T08:09:34"


def add_reaction_to_photo(reacting_user, reaction_type, photo_user, photo_timestamp):
    reaction = "REACTION#{}#{}".format(reacting_user, reaction_type)
    photo = "PHOTO#{}#{}".format(photo_user, photo_timestamp)
    user = "USER#{}".format(photo_user)
    try:
        resp = dynamodb.transact_write_items(
            TransactItems=[
                {
                    "Put": {
                        "TableName": "quick-photos",
                        "Item": {
                            "PK": {"S": reaction},
                            "SK": {"S": photo},
                            "reactingUser": {"S": reacting_user},
                            "reactionType": {"S": reaction_type},
                            "photo": {"S": photo},
                            "timestamp": {"S": datetime.datetime.now().isoformat()},
                        },
                        "ConditionExpression": "attribute_not_exists(SK)",
                        "ReturnValuesOnConditionCheckFailure": "ALL_OLD",
                    }
                },
                {
                    "Update": {
                        "TableName": "quick-photos",
                        "Key": {"PK": {"S": user}, "SK": {"S": photo}},
                        "UpdateExpression": "SET reactions.#t = reactions.#t + :i",
                        "ExpressionAttributeNames": {"#t": reaction_type},
                        "ExpressionAttributeValues": {":i": {"N": "1"}},
                        "ReturnValuesOnConditionCheckFailure": "ALL_OLD",
                    }
                },
            ]
        )
        print("Added {} reaction from {}".format(reaction_type, reacting_user))
        return True
    except Exception as e:
        print("Could not add reaction to photo")


add_reaction_to_photo(REACTING_USER, REACTION_TYPE, PHOTO_USER, PHOTO_TIMESTAMP)
