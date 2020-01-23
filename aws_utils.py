# awsutils

import boto3
import csv

def parse_aws_credentials(cred_key):
    with open("aws-rek-api-cred.csv", newline='') as csvfile:
        data = list(csv.reader(csvfile))

    if (cred_key == "Access key ID"):
        return data[1][2]
    if (cred_key == "Secret access key"):
        return data[1][3]
    else:
        return data

def init_aws_Session():
    client = boto3.client('rekognition', region_name="eu-west-1",
                          aws_access_key_id=parse_aws_credentials("Access key ID"),
                          aws_secret_access_key=parse_aws_credentials("Secret access key"))
    return client