import requests
import json
PINATA_API_KEY = "97b1cd86d9d3f54c999a"
PINATA_API_SECRET ="e61d02e22778665301611f2fe950e93485b337f4cc7341eb0b24b6f962f4713a"

def pin_to_ipfs(data):
  assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	
  pinata_url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"

  headers = {
    "pinata_api_key": PINATA_API_KEY,
    "pinata_secret_api_key": PINATA_API_SECRET
  }

  load = {
    "pinataContent": data
  }

  response = requests.post(
    pinata_url,
    headers = headers,
    json = load
  )

  response.raise_for_status()
  response_json = response.json()
  cid = response_json["IpfsHash"]

  return cid




def get_from_ipfs(cid,content_type="json"):
  assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	
  gateways = [
    "https://gateway.pinata.cloud/ipfs/",
    "https://gateway.pinata.cloud/ipfs/",
    "https://cloudflare-ipfs.com/ipfs/"
  ]
  
  error = None

  for gateway in gateways:
    url = gateway + cid

    try:
      response = requests.get(url)
      response.raise_for_status()
      
      data = response.json()

      assert isinstance(data,dict), f"get_from_ipfs should return a dict"
      return data
    
    except Exception as e:
      error = e

  raise error
