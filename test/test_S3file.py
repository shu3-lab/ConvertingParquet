import pytest
from infra.S3file import S3_control

def test_1():
    s3c = S3_control()
    assert s3c is not None

def test_2():
    s3c = S3_control()
    expect = 'TEST'
    bucket = s3c.make_bucket(s3c.s3, expect)
    assert expect == bucket.name