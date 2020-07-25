# ConvertingParquet

This is the Python script which converts csv files to parquet files and updload created parquet to S3.

**NOTE:**  It's under developing!

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

