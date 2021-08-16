
from google.cloud import storage

import os
import pandas as pd
os.chdir("/Users/ashutoshgoyal/downloads/gcp")
storage_client=storage.Client.from_service_account_json("gcp-assignment-322710-5cfffd0e0e6d.json")


bucket_name='bucket_problem'
bucket=storage_client.get_bucket(bucket_name)
filename1="Customers.csv"
blob1=bucket.blob(filename1)
blob1.upload_from_filename(filename1)
filename2="Orders.csv"
blob2=bucket.blob(filename2)
blob2.upload_from_filename(filename2)




















