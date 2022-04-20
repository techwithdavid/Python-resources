import boto3

s3 = boto3.resource('s3')  # creating a connection with s3 bucket

objects = s3.get_objects(Bucket='coderbytechallengesandbox')

response = client.list_buckets()


for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)