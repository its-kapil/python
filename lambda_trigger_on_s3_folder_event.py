import boto3
import json

s3 = boto3.resource('s3')

print('Loading function')


def lambda_handler(event, context):
	dest_bucket = s3.Bucket('test12lamb')
	message = event['Records'][0]['Sns']['Message']
	message_to_dict = json.loads(message)
	
	src_bucket = str(message_to_dict['Records'][0]["s3"]['bucket']['name'])
	src_file_key = str(message_to_dict['Records'][0]["s3"]['object']['key'])
	print(src_bucket)
	print(src_file_key)
	print(dest_bucket.name)
	
	
	
	dest_key = src_file_key
	

	s3.Object(dest_bucket.name, dest_key).copy_from(CopySource = {'Bucket': src_bucket, 'Key': src_file_key})
	
	output = "file {} has been copied to {} bucket".format(src_file_key,dest_bucket)
	return output
