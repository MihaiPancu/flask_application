from flask import Flask, redirect, url_for, render_template, request, session
import boto3

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
	s3 = boto3.resource('s3')
	bucket = s3.Bucket('mihai-bucket')
	for obj in bucket.objects.all():
		print(obj.key)

	s3 = boto3.client('s3')
	bucket = 'mihai-bucket'
	key = 'ceva.txt'
	response = s3.get_object(Bucket=bucket, Key=key)
	content = response["Body"]
	cont = content.read()
	return f'Am citit -> {cont}'
	return render_template("home.html")

@app.route("/upload", methods=["GET"])
def upload():	
	string = "Am si scris"
	encoded_string = string.encode("utf-8")

	bucket_name = 'mihai-bucket'

	file_name = "hello.txt"
	lambda_path = "/tmp/" + file_name
	s3_path = "/" + file_name


	s3 = boto3.resource("s3")
	s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
	print('Done')
	return 'Am scris'


if __name__ == "__main__":

   app.run('0.0.0.0', debug=True)
