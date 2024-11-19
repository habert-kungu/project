import http.client
import json

conn = http.client.HTTPSConnection("library-api.postmanlabs.com")
payload = json.dumps(
    {
        "title": "Adventures of margot ",
        "author": "Robert Nalla",
        "genre": "fiction ",
        "yearPublished": 1960,
        "checkedOut": True,
    }
)
headers = {"Content-Type": "application/json", "api-key": "postmanrulz"}
conn.request("DELETE", "/books/null", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
