import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import csv

class ConvertParquet:
    @staticmethod
    def convert_to_parquet(filename):
        csv_path = './csv/'+filename+'.csv'

        parquet_path = './parquet/'+filename+'.parquet'


        df = pd.read_csv(csv_path,encoding='Shift_JISx0213',header=0)
        table = pa.Table.from_pandas(df)
        pq.write_table(table, parquet_path)
        print(filename+'.parquet is created at '+parquet_path)