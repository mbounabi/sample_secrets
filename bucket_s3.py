# Save data to an AWS bucket

from typing import Dict

import aws_lib
import pymongo


def aws_upload(data: Dict):
    database = aws_lib.connect("AKIAF6BAFJKR45SAWSZ5", "hjshnk5ex5u34565AWS654/JKGjhz545d89sjkja")
    database.push(data)


def transform_data(es_data: Dict) -> Dict:
    es_data = {**data, "origin": "ES"}

MONGO_URI = "mongodb+srv://testuser:hub24aoeu@gg-is-awesome-gg273.mongodb.net/test?retryWrites=true&w=majority"

def pull_data_from_mongo(query: Dict):
    return pymongo.connect(MONGO_URI).fetch(query)


def push_mongo_to_s3(query):
    for element in pull_data_from_mongo(query):
        upload(element)

github_token: kevcwfsaxmtlphigonzd

github_token: xoxp-2715247581217-2702633601602-2725492689812-2d2f8843d80437925f8a92a34bed47e3

Token: 2715247581217-2702633601602-2725492689812-2d2f8843d80437925f8a92a34bed47e3

Token: 2715247581217-2702633601602-2725492689812-2d2f8843d80437925f8a92a34bed47e3

Token: 2715247581217-2702633601602-2725492689812-2d2f8843d80437925f8a92a34bed47e3
