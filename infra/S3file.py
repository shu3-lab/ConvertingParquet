from infra.abstractS3 import abstract_S3
import boto3
import pandas as pd
import datetime

class S3_control(abstract_S3):
    def __init__(self):
        super().__init__()
        s3 = boto3.resource('s3')
        self.s3 = s3
    
    def from_S3(self, bucketname, filename):
        bucket = self.make_bucket(self.s3,bucketname)
        df = pd.read_csv('s3n://'+bucketname+'/'+filename+'.csv')
        df.to_csv('./csv/'+filename+'.csv', index=False, encoding='utf-8')
    
    def to_S3(self, bucketname, filename):
        bucket = self.make_bucket(self.s3,bucketname)
        now = datetime.datetime.now()
        timestamp = "{0:%Y%m%d%H%M%S}".format(now)
        bucket.upload_file('./parquet/'+filename+'.parquet',timestamp+filename+'.parquet')
    
    @staticmethod
    def make_bucket(s3,bucketname):
        bucket = s3.Bucket(bucketname)
        return bucket

    