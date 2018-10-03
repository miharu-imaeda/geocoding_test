
# coding: utf-8

# In[8]:


import requests
import xmltodict

full_adress = "芝浦工業大学"
url = 'http://www.geocoding.jp/api/'
payload = {'q': full_adress}
result = requests.get(url, params=payload)


resultdict = xmltodict.parse(result.text)
resultdict

print( full_adress )
print("緯度：" + resultdict["result"]["coordinate"]["lat"])
print("経度："+ resultdict["result"]["coordinate"]["lng"])

