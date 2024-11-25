import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "DCI-Lab"
url = "http://192.168.0.151:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

query_api = client.query_api()

query = """from(bucket: "DCI-Lab")
 |> range(start: -10m)
 |> filter(fn: (r) => r._measurement == "measurement1")"""
tables = query_api.query(query, org="DCI-Lab")

for table in tables:
  for record in table.records:
    print(record)