# bgg only sends back XML ( grrrr), so we are using  Requests-HTML package: http://xml.python-requests.org/
import requests
# https://github.com/martinblech/xmltodict
import xmltodict

class ApiService():
  # Do we have to use the decorator for static and class methods?
  @staticmethod
  def get_collection(username="lucegoose100"):
    result = {}
    response = requests.get(
        "https://www.boardgamegeek.com/xmlapi2/collection?username=" + username + "&own=1")
    if response.status_code == 200:
      # Search the XML results for the 'items' element
      converted_data = xmltodict.parse(response.content)
      # NOW we use the xmltodict module to deserialize the json to a Python dictionary
      result['list'] = converted_data['items']['item']
      # And we can add a property to it, since it's friendly old python now
      result["success"] = True
      for game in result["list"]:
        game["name"]["text"] = game["name"]["#text"]
      return result
    else:
      print("HTTP FAILED", response.status_code)

    return result



