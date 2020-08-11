from logic.convertion import convert_parquet as cp
from infra.S3file import S3_control
from exceptions.ArgumentError import ArgumentError
from exceptions.ArgTypeError import ArgTypeError
import sys

s3c = S3_control()

def main():
    try:        
        filename = sys.argv[1]
        bucket = sys.argv[2]
    except IndexError as e:
        raise ArgumentError('Arguments are not entried.Two arguments, a file name and a bucket name of your S3, are required.')

    #Validation of arguments
    if type(filename) is not str:
        raise ArgTypeError('The name of file must be string.')
    elif type(bucket) is not str:
        raise ArgTypeError('The name of bucket must be string.')

    #At fist, download csv file from s3
    s3c.from_S3(bucket,filename)
    #convert csv to parquet
    cp.convert_to_parquet(filename)
    #Upload created parquet to s3 
    s3c.to_S3(bucket,filename)