# {
#   "traits": ["Craftsman", "Pragmatic", "Curious", "Methodical", "Driven", "Collaborator"],
#   "key": "Close-a78aa988",
#   "meta": {
#     "description": "Enclosed are some traits that [Joe](https://www.linkedin.com/in/jkemp101/) believes great engineers exhibit.
#     Using the included UTF-8 `key`, construct a JSON array using the lowercase hex digest of the blake2b hash for each trait (digest size=64).
#     POST this bare array back to this endpoint.
#     Example array: [\"1f9ec19c7...57fd27e5\", \"79c72b47088...bf13026c\", ...]
#     If the hashes are correct you will get a Verification ID you should include in your application.
#     400 responses indicate a problem with the hashes in your array.
#     Note, the key rotates each day around midnight EST."
#   }
# }

import hashlib
import json
import requests

url = 'https://api.close.com/buildwithus/'
traits = ["Craftsman", "Pragmatic", "Curious", "Methodical", "Driven", "Collaborator"]
key = b"Close-a78aa988"

hashes = [
    hashlib.blake2b(trait.encode("utf-8"), key=key, digest_size=64).hexdigest()
    for trait in traits
]

print(json.dumps(hashes, indent=2))

response = requests.post(url, json=hashes)
print(response.status_code)
print(response.text)