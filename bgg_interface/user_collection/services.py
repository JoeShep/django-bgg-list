# bgg only sends back XML ( grrrr), so we are using  Requests-HTML package: http://xml.python-requests.org/
import requests
# https://github.com/martinblech/xmltodict
import xmltodict

class ApiService():
  # Do we have to use the decorator for static and class methods?
  @staticmethod
  def get_collection():
    result = {}
    response = requests.get(
        "https://www.boardgamegeek.com/xmlapi2/thing?id=220877")
    if response.status_code == 200:
      # Search the XML results for the 'items' element
      converted_data = xmltodict.parse(response.content)
      # NOW we use the xmltodict module to deserialize the json to a Python dictionary
      result['title'] = converted_data['items']['item']['name'][0]['@value']
      # And we can add a property to it, since it's friendly old python now
      result["success"] = True
    else:
      print("HTTP FAILED", response.status_code)

    return result
