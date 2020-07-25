from setuptools import setup

setup(
    install_requires=["pandas","pyarrow","boto3"],
    entry_points={
        "console_scripts":[
            "convparquet = main:main"
        ]
    }
)