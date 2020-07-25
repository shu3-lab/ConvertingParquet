from convertion import convert_parquet as cp
from S3file import S3_control as s3c
import sys

def main():
    filename = sys.argv[1]
    bucket = sys.argv[2]

    #At fist, download csv file from s3
    #s3c.from_S3(bucket,filename)
    #convert csv to parquet
    cp.convert_to_parquet(filename)
    #Upload created parquet to s3 
    s3c.to_S3(bucket,filename)