
import requests
# bgg only sends back XML ( grrrr), so we are using
# https://github.com/martinblech/xmltodict
# to comvert XML to a Python dictionary (that is a crazy mess. Log it out and see. Eek)
import xmltodict

class ApiService():
  # Do we have to use the decorator for static and class methods?
  @staticmethod
  def get_collection(username="lucegoose100"):
    result = {}
    response = requests.get(
        "https://www.boardgamegeek.com/xmlapi2/collection?username=" + username + "&own=1")
    if response.status_code == 200:
      # use the xmltodict module to deserialize the json to a Python dictionary, and strip the '@' and '#' symbols from attributes and text keys
      converted_data = xmltodict.parse(
          response.content, attr_prefix='', cdata_key='text')
      result['list'] = converted_data['items']['item']
      # And we can add a property to it, since it's friendly old python now
      result["success"] = True
      return result
    else:
      print("HTTP FAILED", response.status_code)

    return result



