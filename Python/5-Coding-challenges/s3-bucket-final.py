import boto3
from botocore.client import Config

aws_access_key = ""
aws_secret_key = ""
aws_bucket = "bucket-name"

# aws s3 bucket information, please change accordingly
signature_version = ""
region_name = ""

def aws_getFileURL(aws_filename, access_key=aws_access_key, secret_key=aws_secret_key, bucket_name=aws_bucket):
    s3 = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key= secret_key,
                     config=Config(signature_version=signature_version), region_name=region_name)

    # Generate the URL to get 'key-name' from 'bucket-name'
    url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={
            'Bucket': bucket_name,
            'Key': aws_filename,
        }
    )
    return url





# importing the boto3 library 
import boto3
# connect to S3 using boto3 client
s3_client = boto3.client(service_name='s3')
# get S3 object
result = s3_client.get_object(Bucket='<bucket-name>', Key='<file-name-to-read') 
#Read a text file line by line using splitlines object
for line in result["Body"].read().splitlines():
  each_line = line.decode('utf-8')
  print(each_line)