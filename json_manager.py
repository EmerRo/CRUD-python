import json
import os
def read_json():
  #' si no encuentra el archivo entonces crealo y crea un array vacio
  if not os.path.isfile('data.json'):
    with open('data.json', 'w') as f:
      json.dump([],f)
  #' si lo encuentra entonces solo lee el archivo
  with open('data.json','r') as f:
    data = json.load(f)
  return data
    
  
def write_json(data):
  with open('data.json','w')as f:
    json.dump(data, f)