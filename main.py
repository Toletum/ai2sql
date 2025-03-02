"""

"""
import time
import sqlite3
import json
import configparser

from ollama import Client
from pydantic import BaseModel

class Query(BaseModel):
  description: str
  sql: str
  database: str
  tables: list[str]
  fields: list[str]


config = configparser.ConfigParser()
config.read("config.ini")

host = config["OLLAMA"]["HOST"]
model = config["OLLAMA"]["MODEL"]
system_content = config["SYSTEM"]["CONTENT"]


client = Client(host=host)

ini = time.time()

response = client.chat(model=model,
                       stream=False,
                       format=Query.model_json_schema(),
                       messages=[
    {
        'role': 'system',
        'content':system_content
    },
    {
        'role': 'user',
        'content': "query with all clients from city is 'CiudadA'",
    },
])

end = time.time()

query = Query.model_validate_json(response.message.content)
print(json.dumps(query.model_dump(), indent=2))

db = sqlite3.connect(query.database)
cursor = db.cursor()
cursor.execute(query.sql)
for fila in cursor.fetchall():
    print(fila)
db.close()

print(f" total:  {(end - ini)}")
