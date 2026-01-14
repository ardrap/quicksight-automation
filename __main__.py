import pulumi
import pulumi_aws as aws
import os

# 1. THE SQL PART: Locate and read the SQL file
sql_file_path = os.path.join(os.path.dirname(__file__), 'pulumidemo.sql')

if os.path.exists(sql_file_path):
    with open(sql_file_path, 'r') as f:
        sql_query_content = f.read()
else:
    # This keeps the automation from crashing if the file is missing
    raise FileNotFoundError(f"❌ ERROR: Pulumi cannot find '{sql_file_path}'")

# 2. THE AWS PART: Fixed for Pulumi & QuickSight
# Use the correct properties to avoid "Missing required property" errors
dataset = aws.quicksight.DataSet("my-dataset",
    aws_account_id="261375936682",
    data_set_id="9beb65c3-c192-43b8-9b63-d543eef88159",
    name="QuickSight Automation Dataset",
    import_mode="SPICE",  # <--- FIXES YOUR ERROR
    physical_table_map={
        "sql-query-01": { # A unique ID for this table within the dataset
            "custom_sql": {
                "data_source_arn": "arn:aws:quicksight:ap-south-1:261375936682:datasource/YOUR_DATA_SOURCE_ID",
                "name": "CustomSQLTable",
                "sql_query": sql_query_content, # Uses the SQL we read above
                "columns": [
                    {"name": "Corporate ID", "type": "INTEGER"},
                    {"name": "Brand Name", "type": "STRING"},
                    {"name": "Brand Code", "type": "STRING"}
                ],
            },
        },
    },
    # Note: Keep the import option commented until permissions are granted
    # opts=pulumi.ResourceOptions(import_="261375936682/9beb65c3-c192-43b8-9b63-d543eef88159")
)
