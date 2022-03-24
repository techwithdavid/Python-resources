import io
import boto3

AWS_REGION = "us-east-2"
S3_BUCKET_NAME = "hands-on-cloud-demo-bucket"

s3_resource = boto3.resource("s3", region_name=AWS_REGION)

s3_bucket = s3_resource.Bucket(S3_BUCKET_NAME)

print('Listing Amazon S3 Bucket objects/files:')

for obj in s3_bucket.objects.filter(Prefix='demo'):
    print(f'-- {obj.key}')