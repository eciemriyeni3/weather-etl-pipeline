# from google.cloud import bigquery

# def load_to_bigquery(data, table_id):
#     client = bigquery.Client()
#     errors = client.insert_rows_json(table_id, [data])
#     if errors:
#         print("Encountered errors:", errors)
#     else:
#         print("Data inserted successfully.")

import json
import os
from google.cloud import bigquery

def load_to_bigquery(data, table_id):
    client = bigquery.Client()
    
    # Simpan ke file JSON sementara
    tmp_file = '/tmp/tmp_data.json'
    with open(tmp_file, 'w') as f:
        # json.dump([data], f)
        f.write(json.dumps(data) + '\n')
    
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        autodetect=True,  # atau bisa custom schema
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND
    )

    with open(tmp_file, "rb") as source_file:
        load_job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    
    load_job.result()  # Tunggu sampai selesai
    print(f"Loaded data to {table_id}")
    
    os.remove(tmp_file)  # Hapus file sementara
