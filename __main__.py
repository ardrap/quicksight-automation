"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import os

# 1. READ YOUR SQL FILE
sql_file_path = os.path.join(os.path.dirname(__file__), 'pulumidemo.sql')
with open(sql_file_path, 'r') as f:
    sql_query_content = f.read()

# 2. DEFINE THE DATASET (This is the automation part)
# This connects your local SQL file to the existing AWS Dataset
dataset = aws.quicksight.DataSet("my-dataset",
    aws_account_id="261375936682",
    data_set_id="9beb65c3-c192-43b8-9b63-d543eef88159",
    name="Pulumi_Test_Dataset", # The display name in QuickSight
    import_mode="SPICE",
    physical_table_maps=[{
        "physical_table_map_id": "sql-table-01",
        "custom_sql": {
            "data_source_arn": "arn:aws:quicksight:ap-south-1:261375936682:datasource/9eefb60c-73ac-40f9-8431-f171776c9c02", # Get this from 'aws quicksight list-data-sources'
            "name": "Corporate_Brand_Query",
            "sql_query": sql_query_content, # <--- THIS makes the magic happen
            "columns": [
                { "name": "Corporate ID", "type": "INTEGER" },
                { "name": "Brand Name", "type": "STRING" },
                { "name": "Brand Code", "type": "STRING" }
            ],
        }
    }],
    # This tells Pulumi: "I already created this manually, please take control of it."
    opts=pulumi.ResourceOptions(import_="261375936682,9beb65c3-c192-43b8-9b63-d543eef88159")
)

pulumi.export("dataset_arn", dataset.arn)
