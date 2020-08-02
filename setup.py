from setuptools import setup

setup(
    name="converting-parquet",
    version="1.0.0",
    install_requires=["pandas","pyarrow","boto3","s3fs"],
    entry_points={
        "console_scripts":[
            "convparquet = main:main"
        ]
    }
)