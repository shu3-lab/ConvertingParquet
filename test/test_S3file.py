import pytest
import os
from infra.S3file import S3_control

path = os.path.isdir('./parquet')

@pytest.fixture
def S3():
    s3c = S3_control()
    return s3c

def test_1():
    s3c = S3_control()
    assert s3c is not None

def test_2(S3):
    expect = 'TEST'
    bucket = S3.make_bucket(S3.s3, expect)
    assert expect == bucket.name

@pytest.mark.skipif(path==False, reason='localonly')
def test_3(S3):
    bucket_name = 'test-parquet-convertion'
    file_name = 'TEST'
    S3.from_S3(bucket_name, file_name)
    expect_path = './csv/'+file_name+'.csv'
    result = os.path.isfile(expect_path)
    assert True == result

@pytest.mark.skipif(path==False, reason='localonly')
def test_4(S3):
    bucket_name = 'test-parquet-convertion'
    file_name = 'TEST'
    bucket = S3.make_bucket(S3.s3, bucket_name)
    pre_count = len(list(bucket.objects.all()))
    S3.to_S3(bucket_name, file_name)
    post_count = len(list(bucket.objects.all()))
    result = post_count - pre_count
    assert 1 == result

    
