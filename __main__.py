import pulumi
import pulumi_aws as aws
import os

# 1. FIX THE FILE PATH
# This ensures GitHub can find the SQL file no matter where it is running
sql_file_path = os.path.join(os.path.dirname(__file__), 'pulumidemo.sql')

try:
    with open(sql_file_path, 'r') as f:
        sql_query = f.read()
except FileNotFoundError:
    # This helps you debug if the file is truly missing on GitHub
    print(f"❌ ERROR: Pulumi cannot find '{sql_file_path}'. Check the file name!")
    raise

# 2. FIX THE DATASET CODE
dataset = aws.quicksight.DataSet("my-dataset",
    aws_account_id="YOUR_AWS_ACCOUNT_ID",
    data_set_id="quicksight-automation-dataset",
    name="Automation Dataset",
    import_mode="SPICE",  # <--- THIS WAS THE MISSING PROPERTY
    physical_table_map={
        "sql-table": {
            "custom_sql": {
                "data_source_arn": "YOUR_DATA_SOURCE_ARN",
                "name": "CustomSQL",
                "sql_query": sql_query,
                "columns": [
                    {"name": "column1", "type": "STRING"},
                    # Add your other columns here
                ],
            },
        },
    },
    # REMEMBER: Add your import line here once you have permissions
    # opts=pulumi.ResourceOptions(import_="YOUR_ACCOUNT_ID/DATASET_ID")
)
