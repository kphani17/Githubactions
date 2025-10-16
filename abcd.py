import json

print('Hello all, this is Python script!')

with open('config.json') as f:
    data = json.load(f)

print(f"ENVIRONMENT={data['environment']}")
print(f"APP_NAME={data['app_name']}")
print(f"REGION={data['region']}")
