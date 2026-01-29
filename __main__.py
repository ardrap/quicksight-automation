import pulumi
import pulumi_aws as aws
import os

# Create the provider
mumbai_provider = aws.Provider("mumbai", region="ap-south-1")

# Read SQL
sql_file_path = os.path.join(os.path.dirname(__file__), 'Pulumidemo.sql')
with open(sql_file_path, 'r') as f:
    sql_query_content = f.read()

# Define Dataset
dataset = aws.quicksight.DataSet("qs-production-dataset",
    aws_account_id="261375936682",
    data_set_id="9beb65c3-c192-43b8-9b63-d543eef88159",
    name="Pulumi_Test_Dataset",
    import_mode="SPICE",
    physical_table_maps=[{
        "physical_table_map_id": "sql-table-01",
        "custom_sql": {
            "data_source_arn": "arn:aws:quicksight:ap-south-1:261375936682:datasource/9eefb60c-73ac-40f9-8431-f171776c9c02",
            "name": "Corporate_Brand_Query",
            "sql_query": sql_query_content,
            "columns": [
                { "name": "Corporate ID", "type": "INTEGER" },
                { "name": "Brand Name", "type": "STRING" },
                { "name": "Brand Code", "type": "STRING" }
            ],
        }
    }],
    logical_table_maps=[{
        "logical_table_map_id": "sql-table-01",
        "alias": "Corporate_Brand_Query",
        "source": {
            "physical_table_id": "sql-table-01",
        },
    }],
    opts=pulumi.ResourceOptions(
        provider=mumbai_provider,
        import_="261375936682,9beb65c3-c192-43b8-9b63-d543eef88159",
        ignore_changes=["permissions"]
    )
)

pulumi.export("dataset_arn", dataset.arn)
