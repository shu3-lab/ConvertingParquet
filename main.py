from logic.convertion import ConvertParquet as cp
from infra.S3file import S3Control
import sys

s3c = S3Control()

def main():
    try:        
        filename = sys.argv[1]
        bucket = sys.argv[2]
    except IndexError as e:
        raise IndexError('Arguments are not entried.Two arguments, a file name and a bucket name of your S3, are required.')

    #At fist, download csv file from s3
    s3c.from_S3(bucket,filename)
    #convert csv to parquet
    cp.convert_to_parquet(filename)
    #Upload created parquet to s3 
    s3c.to_S3(bucket,filename)