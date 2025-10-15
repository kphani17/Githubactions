import json
print('Hello! all, This is python script')
data = json.load(open('config.json'))
print(f'ENVIRONMENT={data[\"environment\"]}\\nAPP_NAME={data[\"app_name\"]}\\nREGION={data[\"region\"]}')
