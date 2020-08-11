# ConvertingParquet

![Python package](https://github.com/shu3-lab/ConvertingParquet/workflows/Python%20package/badge.svg)

This is the Python script which converts csv files to parquet files and updload created parquet to S3.

<img width="700" alt="スクリーンショット 2020-08-11 15 09 04" src="https://user-images.githubusercontent.com/56756975/89863212-9fe78c80-dbe4-11ea-8217-8690669656af.png">

## How to use it?

After `git clone`, do the steps below.

1. Construct virtualenv by running `virtualenv .`
2. Install dependencies by running `pip install -r requirements.txt`
3. Confirm dependencies by running `pip list`
4. Run `convparquet` to start functions
   - **TIPS:** This command requires two arguments, 1st is filename and 2nd is bucketname of S3 e.g. `convparquet hoge piyo`

## What's possible usecase?

1. Prepare to analys data by Athena
2. ETL for analytics of BI(e.g. Tableau, QuickSight)

