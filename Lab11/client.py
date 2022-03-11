import requests



requests.post(url="http://127.0.0.1:8080?a=1",
              headers ={"header1" : "value1", "header2" : "value2"},
              data = {"key1": "value1", "key2": "value2"})
