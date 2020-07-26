from logic.convertion import convert_parquet as cp
import os
import pytest

path = os.path.isdir('./parquet')

@pytest.mark.skipif(path==False, reason='localonly')
def test_1():
    test_filename = 'TEST'
    expect_path = './parquet/'+test_filename+'.parquet'
    cp.convert_to_parquet(test_filename)
    result = os.path.isfile(expect_path)
    assert True == result