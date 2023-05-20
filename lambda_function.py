import boto3
import requests
from requests_aws4auth import AWS4Auth
import os
import json

host = os.getenv('HOST')
region = 'ap-northeast-2'
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

index = 'logs'
datatype = '_doc'
url = host + '/' + index + '/' + datatype

headers = { "Content-Type": "application/json" }

with open('sample.json') as f:
    datas = json.load(f)

for data in datas:
    r = requests.post(url, auth=awsauth, json=data, headers=headers)
    print(r.text)
