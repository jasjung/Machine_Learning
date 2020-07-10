import boto3

from entities import Photo, Reaction

dynamodb = boto3.client('dynamodb')

USER = "david25"
TIMESTAMP = '2019-03-02T09:11:30'


def fetch_photo_and_reactions(username, timestamp):
    try:
        resp = dynamodb.query(
            TableName='quick-photos',
            IndexName='InvertedIndex',
            KeyConditionExpression="SK = :sk AND PK BETWEEN :reactions AND :user",
            ExpressionAttributeValues={
                ":sk": { "S": "PHOTO#{}#{}".format(username, timestamp) },
                ":user": { "S": "USER$" },
                ":reactions": { "S": "REACTION#" },
            },
            ScanIndexForward=True
        )
    except Exception as e:
        print("Index is still backfilling. Please try again in a moment.")
        return False

    items = resp['Items']
    items.reverse()

    photo = Photo(items[0])
    photo.reactions = [Reaction(item) for item in items[1:]]

    return photo


photo = fetch_photo_and_reactions(USER, TIMESTAMP)

if photo:
    print(photo)
    for reaction in photo.reactions:
        print(reaction)

