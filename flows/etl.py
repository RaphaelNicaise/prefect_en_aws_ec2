from prefect import flow, task, get_run_logger
from prefect import get

import boto3
import json
from dotenv import load_dotenv 

load_dotenv()

s3 = boto3.client('s3')

BUCKET_NAME = 'etl-data-bucket-rapha'

@task
def search_data_s3(bucket_name,key):
    """
    Returns:
    """
    logger = get_run_logger()
    
    response = s3.get_object(Bucket=bucket_name,Key=key)
    content = json.loads(response['Body'].read().decode('utf-8'))
    
    logger.info('')
    
    return content

@task
def upload_file_s3(bucket_name,key,content):
    """
    Returns:
    """
    logger = get_run_logger()
    
    json_bytes = json.dumps(content).encode('utf-8')
    s3.put_object(Bucket=bucket_name,Key='processed/data.json',Body=json_bytes)

    logger.info('')
    
@flow
def etl_flow():
    logger = get_run_logger()
    
    data = search_data_s3(BUCKET_NAME,'landing/anscombe.json')
    upload_file_s3(BUCKET_NAME,'processed/data.json',data)


if __name__ == "__main__":
   etl_flow()
