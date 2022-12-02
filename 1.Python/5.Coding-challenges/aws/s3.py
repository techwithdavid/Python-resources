import boto3
s3 = boto3.resource('s3')
obj = s3.Object(bucketname, itemname)
body = obj.get()['Body'].read()

#download file
import boto3
s3 = boto3.resource("s3")
srcFileName="abc.txt"
destFileName="s3_abc.txt"
bucketName="mybucket001"
k = Key(bucket,srcFileName)
k.get_contents_to_filename(destFileName)

data.Body.toString('ascii') # get the contents of the text file, assuming that the text file was encoded used ascii format.

#read the file from S3 bucket using lambda function
def lambda_handler(event, context):
    # TODO implement
    import boto3

    s3 = boto3.client('s3')
    data = s3.get_object(Bucket='my_s3_bucket', Key='main.txt')
    contents = data['Body'].read()
    print(contents)

#read file  from S3 bucket 
    exports.handler = (event, context, callback) => {
     var bucketName = process.env.bucketName;
     var keyName = event.Records[0].s3.object.key;
     readFile(bucketName, keyName, readFileContent, onError);
};