
from utils import create_bucket, upload_file, download_file, list_buckets

class S3Client():
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        
    def create_bucket(self):
        create_bucket(self.bucket_name)

    def upload_file(self, file_name, object_name=None):
        upload_file(file_name, self.bucket_name, object_name)

    def download_file(self, file_path, file_name, bucket_name, object_name=None):
        download_file(file_path, file_name, self.bucket_name, object_name)
        
    def list_buckets(self):
        list_buckets()