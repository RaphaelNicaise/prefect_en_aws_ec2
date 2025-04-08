from prefect import flow, task
import boto3
import json
from dotenv import load_dotenv 

load_dotenv()

s3 = boto3.client('s3')

BUCKET_NAME = 'etl-data-bucket-rapha'

@task
def search_data_s3(bucket_name,key):
    response = s3.get_object(Bucket=bucket_name,Key=key)
    content = json.loads(response['Body'].read().decode('utf-8'))
    return content

@task
def upload_file_s3(bucket_name,key,content):
    json_bytes = json.dumps(content).encode('utf-8')
    s3.put_object(Bucket=bucket_name,Key='processed/data.json',Body=json_bytes)

@flow
def etl_flow():
    data = search_data_s3(BUCKET_NAME,'landing/anscombe.json')
    upload_file_s3(BUCKET_NAME,'processed/data.json',data)


if __name__ == "__main__":
   etl_flow()
