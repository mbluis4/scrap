import logging
import boto3
from botocore.exceptions import ClientError
import os

s3 = boto3.client('s3')
s3.upload_file('test.txt', 'faucetsprices2023', 'hello.txt')
