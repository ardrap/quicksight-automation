"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws
import os

# 1. THE TEST: Locate and read the SQL file
sql_file_path = os.path.join(os.path.dirname(__file__), 'pulumidemo.sql')

# This part checks if the file actually exists before trying to read it
if os.path.exists(sql_file_path):
    with open(sql_file_path, 'r') as f:
        sql_query_content = f.read()
    print("✅ SUCCESS: Pulumi can find and read your SQL file!")
    print("-" * 30)
    print(f"SQL CONTENT:\n{sql_query_content}")
    print("-" * 30)
else:
    print("❌ ERROR: Pulumi cannot find 'pulumidemo.sql'. Check the file name!")

# 2. THE AWS PART (This will stay here until you get permissions)
# Even though we can't 'up' yet, we keep this here so the code is ready.
dataset = aws.quicksight.DataSet("my-dataset",
    aws_account_id="261375936682",
    data_set_id="9beb65c3-c192-43b8-9b63-d543eef88159",
    # ... other fields ...
)


