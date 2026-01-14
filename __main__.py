import os
import pulumi

# Get the absolute path of the directory where __main__.py is located
base_dir = os.path.dirname(os.path.abspath(__file__))
sql_file_path = os.path.join(base_dir, 'Pulumidemo.sql')

# Debugging: Print exactly where the runner is looking
print(f"DEBUG: Looking for SQL file at: {sql_file_path}")

if os.path.exists(sql_file_path):
    with open(sql_file_path, 'r') as f:
        sql_query_content = f.read()
else:
    # This error message will tell us exactly what path was searched
    raise FileNotFoundError(f"❌ ERROR: Pulumi cannot find '{sql_file_path}'")
