#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests

app_access_token = 'MLY|9759896194041849|3101803a1fcb7a7a8a63d2046b5186e6' 
image_id = '169979785061521'
url = 'https://graph.mapillary.com/{}/detections?fields=id,value,created_at&access_token={}'.format(image_id,app_access_token)

headers = { "Authorization" : "OAuth {}".format(app_access_token) }
response = requests.get(url, headers)
data = response.json()

print(data)


# In[6]:


import requests

app_access_token = 'MLY|9759896194041849|3101803a1fcb7a7a8a63d2046b5186e6'

bbox = "37.8690,40.9800,37.8820,40.9900"  

url = f"https://graph.mapillary.com/images?fields=id,geometry,captured_at&bbox={bbox}"

headers = {"Authorization": f"OAuth {app_access_token}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Görüntü Verileri:")
    print(data)
    
    images = data.get('data', [])
    for image in images:
        image_id = image['id']
        print(f"Görüntü ID: {image_id}, Koordinatlar: {image['geometry']}")

        detection_url = f"https://graph.mapillary.com/{image_id}/detections?fields=id,value,created_at"
        detection_response = requests.get(detection_url, headers=headers)
        if detection_response.status_code == 200:
            detections = detection_response.json()
            print(f"Algılamalar: {detections}")
        else:
            print(f"Algılamalar alınamadı: {detection_response.status_code}")
else:
    print(f"Hata: {response.status_code}, {response.text}")


# In[7]:


import datetime
import folium
from geopy.distance import geodesic

data = [
    {'id': '3035219850088354', 'geometry': {'type': 'Point', 'coordinates': [37.881252299972, 40.981579]}, 'captured_at': 1605801864000},
    {'id': '6113086658708809', 'geometry': {'type': 'Point', 'coordinates': [37.870834399972, 40.981985299972]}, 'captured_at': 1606231669000},
    
]

target_area_center = (40.985, 37.880)  # Lat, Lon
radius_km = 1  # 1 km yarıçap
start_date = datetime.datetime(2020, 11, 15)
end_date = datetime.datetime(2020, 12, 15)

filtered_data = []
for item in data:
    point = (item['geometry']['coordinates'][1], item['geometry']['coordinates'][0])
    distance = geodesic(target_area_center, point).km
    captured_time = datetime.datetime.fromtimestamp(item['captured_at'] / 1000)
    
    if distance <= radius_km and start_date <= captured_time <= end_date:
        filtered_data.append(item)

m = folium.Map(location=target_area_center, zoom_start=15)

for item in filtered_data:
    coords = item['geometry']['coordinates']
    folium.Marker(
        location=[coords[1], coords[0]],
        popup=f"ID: {item['id']}, Date: {datetime.datetime.fromtimestamp(item['captured_at'] / 1000)}",
    ).add_to(m)

m.save("filtered_map.html")
print("Filtrelenmiş veriler kaydedildi: filtered_map.html")


# In[8]:


import requests
import json

app_access_token = 'MLY|9759896194041849|3101803a1fcb7a7a8a63d2046b5186e6'

bbox = "37.8690,40.9800,37.8820,40.9900"  

url = f"https://graph.mapillary.com/images?fields=id,geometry,captured_at&bbox={bbox}"

headers = {"Authorization": f"OAuth {app_access_token}"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    # Veriyi JSON dosyasına kaydediyoruz
    with open('mapillary_images_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)


# In[9]:


import matplotlib.pyplot as plt

coordinates = [
    [37.881252299972, 40.981579], [37.870834399972, 40.981985299972],
    [37.8794881, 40.986379999972], [37.8798156, 40.9819055],
    [37.8721326, 40.982333199972], [37.8793726, 40.981264799972],
    [37.879401799972, 40.9864018], [37.8789707, 40.9843978],
    [37.8755334, 40.980326599972], [37.8801927, 40.986105299972],
    [37.8795554, 40.981111099972], [37.876659099972, 40.9845279],
    [37.8714972, 40.9827719], [37.8792715, 40.982615299972],
    [37.880314499972, 40.986040799972], [37.881661525921, 40.985456058315],
    [37.8748584, 40.989395999972], [37.8759115, 40.982204799972],
    [37.878697699972, 40.9851511], [37.880066070407, 40.985537384028],
    [37.877924899972, 40.983748599972], [37.881300214995, 40.983859790455],
    [37.871654599972, 40.9818142], [37.8756113, 40.989473599972],
    [37.8789445, 40.984826099972], [37.8790928, 40.9831341],
    [37.879274799972, 40.9826277], [37.881153599972, 40.9854363],
    [37.879353199972, 40.98516], [37.8712066, 40.9847699],
    [37.8800706, 40.9855352], [37.8807266, 40.9831871],
    [37.880676999972, 40.985701699972], [37.8816689, 40.980485199972],
    [37.878186999972, 40.9848214], [37.880720199972, 40.985857299972],
    [37.880620933495, 40.98494564839], [37.871476399972, 40.984299399972],
    [37.8807988, 40.981450999972], [37.8793622, 40.981406999972],
    [37.879379374137, 40.986344528735], [37.874974899972, 40.988302699972],
    [37.8794582, 40.986302199972], [37.880239199972, 40.9861816],
    [37.8705086, 40.982597599972], [37.880818699972, 40.983263499972],
    [37.880133920046, 40.9854951129], [37.8743144, 40.985740999972],
    [37.8811236, 40.985460099972], [37.8741411, 40.9870041],
    [37.881053399972, 40.9853491], [37.8797694, 40.9801609],
    [37.874344969124, 40.986631414343], [37.8806062, 40.9810281],
    [37.879503999972, 40.9816482], [37.872847, 40.989403],
    [37.8778008, 40.984725799972], [37.876035299972, 40.982275],
    [37.876867691168, 40.987461058173], [37.879418, 40.981674699972],
    [37.874979188133, 40.986591525151], [37.879083999972, 40.986512699972],
    [37.878137999972, 40.9815515], [37.880055599972, 40.986241599972],
    [37.88103, 40.9852749], [37.874881399972, 40.981468599972],
    [37.8810112, 40.985330199972], [37.875994099972, 40.9885079],
    [37.8756204, 40.9899501], [37.8745953, 40.9851377],
    [37.873292999972, 40.989213499972], [37.879382599972, 40.986358699972],
    [37.880491499972, 40.9858247], [37.8806014, 40.981349399972],
    [37.872823599972, 40.989401499972], [37.875226499972, 40.9888594],
    [37.872959, 40.983087199972], [37.8771714, 40.986810599972],
    [37.881149899972, 40.985592699972], [37.880888699972, 40.985264499972],
    [37.881163399972, 40.9855394], [37.8805612, 40.985035299972],
    [37.8813934, 40.984815699972], [37.8787451, 40.981627799972]
]

latitudes = [coord[1] for coord in coordinates]
longitudes = [coord[0] for coord in coordinates]

plt.figure(figsize=(10, 8))
plt.scatter(longitudes, latitudes, color='blue', s=10)
plt.title("Geospatial Visualization of Points")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()


# In[13]:


import folium
from folium import IFrame
import base64

m = folium.Map(location=[39.9334, 32.8597], zoom_start=12) 

def encode_image(image_path):
    with open(image_path, "rb") as img_file:
        img_base64 = base64.b64encode(img_file.read()).decode("utf-8")
    return img_base64

image_path = r"C:\Users\ASUS\Desktop\altindag.jpg" 
encoded_image = encode_image(image_path)

data = [
    {
        "location": [39.9334, 32.8597], 
        "title": "Altındağ Fotoğrafı",
        "description": "Altındağ'dan bir görünüm.",
        "image_base64": encoded_image
    }
]

for item in data:
    location = item["location"]
    title = item["title"]
    description = item["description"]
    image_base64 = item["image_base64"]

    iframe = IFrame(f"""
        <b>{title}</b><br>
        <p>{description}</p><br>
        <img src="data:image/jpeg;base64,{image_base64}" width="300" height="200"><br>
    """, width=400, height=350)

    popup = folium.Popup(iframe, max_width=500)

    folium.Marker(location, popup=popup).add_to(m)

m.save("map_with_local_image.html")


# In[17]:


import pandas as pd
import matplotlib.pyplot as plt

data = [
    {'id': '3035219850088354', 'geometry': {'type': 'Point', 'coordinates': [37.881252299972, 40.981579]}, 'captured_at': 1605801864000},
    {'id': '6113086658708809', 'geometry': {'type': 'Point', 'coordinates': [37.870834399972, 40.981985299972]}, 'captured_at': 1606231669000},
    {'id': '309391234057713', 'geometry': {'type': 'Point', 'coordinates': [37.8794881, 40.986379999972]}, 'captured_at': 1605798660000},
    {'id': '493293635128471', 'geometry': {'type': 'Point', 'coordinates': [37.8798156, 40.9819055]}, 'captured_at': 1605802438000},
    {'id': '789088138646851', 'geometry': {'type': 'Point', 'coordinates': [37.8721326, 40.982333199972]}, 'captured_at': 1606230973000},
    {'id': '1420307031661622', 'geometry': {'type': 'Point', 'coordinates': [37.8793726, 40.981264799972]}, 'captured_at': 1606219955000},
    {'id': '310891847545594', 'geometry': {'type': 'Point', 'coordinates': [37.879401799972, 40.9864018]}, 'captured_at': 1636474335000},
    {'id': '760426761503098', 'geometry': {'type': 'Point', 'coordinates': [37.8789707, 40.9843978]}, 'captured_at': 1605802260000},
    {'id': '3969043473181728', 'geometry': {'type': 'Point', 'coordinates': [37.8755334, 40.980326599972]}, 'captured_at': 1605783102000},
    {'id': '313116477306156', 'geometry': {'type': 'Point', 'coordinates': [37.8801927, 40.986105299972]}, 'captured_at': 1636474297000},
    {'id': '583510673039067', 'geometry': {'type': 'Point', 'coordinates': [37.8795554, 40.981111099972]}, 'captured_at': 1606219947000},
    {'id': '759306438071322', 'geometry': {'type': 'Point', 'coordinates': [37.876659099972, 40.9845279]}, 'captured_at': 1605532269000},
    {'id': '875951249627173', 'geometry': {'type': 'Point', 'coordinates': [37.8714972, 40.9827719]}, 'captured_at': 1606231705000},
    {'id': '1417692038774922', 'geometry': {'type': 'Point', 'coordinates': [37.8792715, 40.982615299972]}, 'captured_at': 1689176188000},
    {'id': '1431316083874684', 'geometry': {'type': 'Point', 'coordinates': [37.880314499972, 40.986040799972]}, 'captured_at': 1607101927000},
    {'id': '1802154263288029', 'geometry': {'type': 'Point', 'coordinates': [37.881661525921, 40.985456058315]}, 'captured_at': 1580823369608},
    {'id': '3945832785502322', 'geometry': {'type': 'Point', 'coordinates': [37.8748584, 40.989395999972]}, 'captured_at': 1605524588000},
    {'id': '320287679613150', 'geometry': {'type': 'Point', 'coordinates': [37.8759115, 40.982204799972]}, 'captured_at': 1606230195000},
    {'id': '1685420368573534', 'geometry': {'type': 'Point', 'coordinates': [37.878697699972, 40.9851511]}, 'captured_at': 1689266713000},
    {'id': '4256262041070841', 'geometry': {'type': 'Point', 'coordinates': [37.880066070407, 40.985537384028]}, 'captured_at': 1605270206724},
    {'id': '602213558784188', 'geometry': {'type': 'Point', 'coordinates': [37.877924899972, 40.983748599972]}, 'captured_at': 1689266641000},
    {'id': '791584188228123', 'geometry': {'type': 'Point', 'coordinates': [37.881300214995, 40.983859790455]}, 'captured_at': 1605282651570},
    {'id': '838056683470373', 'geometry': {'type': 'Point', 'coordinates': [37.871654599972, 40.9818142]}, 'captured_at': 1606231655000},
    {'id': '841908463203195', 'geometry': {'type': 'Point', 'coordinates': [37.8756113, 40.989473599972]}, 'captured_at': 1605521968000},
    {'id': '937423697336504', 'geometry': {'type': 'Point', 'coordinates': [37.8789445, 40.984826099972]}, 'captured_at': 1689176328000},
    {'id': '977377146719492', 'geometry': {'type': 'Point', 'coordinates': [37.8790928, 40.9831341]}, 'captured_at': 1689266613000},
    {'id': '3533316046905743', 'geometry': {'type': 'Point', 'coordinates': [37.879274799972, 40.9826277]}, 'captured_at': 1689176194000},
    {'id': '3793952034064475', 'geometry': {'type': 'Point', 'coordinates': [37.881153599972, 40.9854363]}, 'captured_at': 1605866175000},
    {'id': '513847396694933', 'geometry': {'type': 'Point', 'coordinates': [37.879353199972, 40.98516]}, 'captured_at': 1605532199000},
    {'id': '771487706841566', 'geometry': {'type': 'Point', 'coordinates': [37.8712066, 40.9847699]}, 'captured_at': 1606231811000},
    {'id': '2849707748602541', 'geometry': {'type': 'Point', 'coordinates': [37.8800706, 40.9855352]}, 'captured_at': 1605544655000},
    {'id': '4774846385864658', 'geometry': {'type': 'Point', 'coordinates': [37.8807266, 40.9831871]}, 'captured_at': 1605801964000},
    {'id': '475426690182556', 'geometry': {'type': 'Point', 'coordinates': [37.880676999972, 40.985701699972]}, 'captured_at': 1605535083000},
    {'id': '919003785616842', 'geometry': {'type': 'Point', 'coordinates': [37.8816689, 40.980485199972]}, 'captured_at': 1606219621000},
    {'id': '1830227567379288', 'geometry': {'type': 'Point', 'coordinates': [37.878186999972, 40.9848214]}, 'captured_at': 1689266687000},
    {'id': '258601149390754', 'geometry': {'type': 'Point', 'coordinates': [37.880720199972, 40.985857299972]}, 'captured_at': 1605544425000},
    {'id': '796317724581591', 'geometry': {'type': 'Point', 'coordinates': [37.880620933495, 40.98494564839]}, 'captured_at': 1605269209165},
    {'id': '816991235587573', 'geometry': {'type': 'Point', 'coordinates': [37.871476399972, 40.984299399972]}, 'captured_at': 1606231781000},
    {'id': '984689102302118', 'geometry': {'type': 'Point', 'coordinates': [37.8807988, 40.981450999972]}, 'captured_at': 1605535384000},
    {'id': '1656968594135032', 'geometry': {'type': 'Point', 'coordinates': [37.874749299972, 40.9803589]}, 'captured_at': 1689176142000},
    {'id': '1280775106807887', 'geometry': {'type': 'Point', 'coordinates': [37.8775914, 40.982998099972]}, 'captured_at': 1689176167000}
]

df = pd.DataFrame(data)

df['captured_at'] = pd.to_datetime(df['captured_at'], unit='ms')

plt.figure(figsize=(10,6))
df['captured_at'].hist(bins=30, edgecolor='black')
plt.title("Fotoğraf Çekilme Zamanları", fontsize=14)
plt.xlabel("Zaman", fontsize=12)
plt.ylabel("Çekim Sayısı", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# In[19]:


import pandas as pd
import folium
from IPython.display import display

data = [
    {'id': '3035219850088354', 'geometry': {'type': 'Point', 'coordinates': [37.881252299972, 40.981579]}, 'captured_at': 1605801864000},
    {'id': '6113086658708809', 'geometry': {'type': 'Point', 'coordinates': [37.870834399972, 40.981985299972]}, 'captured_at': 1606231669000},
    {'id': '309391234057713', 'geometry': {'type': 'Point', 'coordinates': [37.8794881, 40.986379999972]}, 'captured_at': 1605798660000},
    {'id': '493293635128471', 'geometry': {'type': 'Point', 'coordinates': [37.8798156, 40.9819055]}, 'captured_at': 1605802438000},
    {'id': '789088138646851', 'geometry': {'type': 'Point', 'coordinates': [37.8721326, 40.982333199972]}, 'captured_at': 1606230973000},
    {'id': '1420307031661622', 'geometry': {'type': 'Point', 'coordinates': [37.8793726, 40.981264799972]}, 'captured_at': 1606219955000},
    {'id': '310891847545594', 'geometry': {'type': 'Point', 'coordinates': [37.879401799972, 40.9864018]}, 'captured_at': 1636474335000},
    {'id': '760426761503098', 'geometry': {'type': 'Point', 'coordinates': [37.8789707, 40.9843978]}, 'captured_at': 1605802260000},
    {'id': '3969043473181728', 'geometry': {'type': 'Point', 'coordinates': [37.8755334, 40.980326599972]}, 'captured_at': 1605783102000},
    {'id': '313116477306156', 'geometry': {'type': 'Point', 'coordinates': [37.8801927, 40.986105299972]}, 'captured_at': 1636474297000},
    {'id': '583510673039067', 'geometry': {'type': 'Point', 'coordinates': [37.8795554, 40.981111099972]}, 'captured_at': 1606219947000},
    {'id': '759306438071322', 'geometry': {'type': 'Point', 'coordinates': [37.876659099972, 40.9845279]}, 'captured_at': 1605532269000},
    {'id': '875951249627173', 'geometry': {'type': 'Point', 'coordinates': [37.8714972, 40.9827719]}, 'captured_at': 1606231705000},
    {'id': '1417692038774922', 'geometry': {'type': 'Point', 'coordinates': [37.8792715, 40.982615299972]}, 'captured_at': 1689176188000},
    {'id': '1431316083874684', 'geometry': {'type': 'Point', 'coordinates': [37.880314499972, 40.986040799972]}, 'captured_at': 1607101927000},
    {'id': '1802154263288029', 'geometry': {'type': 'Point', 'coordinates': [37.881661525921, 40.985456058315]}, 'captured_at': 1580823369608},
    {'id': '3945832785502322', 'geometry': {'type': 'Point', 'coordinates': [37.8748584, 40.989395999972]}, 'captured_at': 1605524588000},
    {'id': '320287679613150', 'geometry': {'type': 'Point', 'coordinates': [37.8759115, 40.982204799972]}, 'captured_at': 1606230195000},
    {'id': '1685420368573534', 'geometry': {'type': 'Point', 'coordinates': [37.878697699972, 40.9851511]}, 'captured_at': 1689266713000},
    {'id': '4256262041070841', 'geometry': {'type': 'Point', 'coordinates': [37.880066070407, 40.985537384028]}, 'captured_at': 1605270206724},
    {'id': '602213558784188', 'geometry': {'type': 'Point', 'coordinates': [37.877924899972, 40.983748599972]}, 'captured_at': 1689266641000},
    {'id': '791584188228123', 'geometry': {'type': 'Point', 'coordinates': [37.881300214995, 40.983859790455]}, 'captured_at': 1605282651570},
    {'id': '838056683470373', 'geometry': {'type': 'Point', 'coordinates': [37.871654599972, 40.9818142]}, 'captured_at': 1606231655000},
    {'id': '841908463203195', 'geometry': {'type': 'Point', 'coordinates': [37.8756113, 40.989473599972]}, 'captured_at': 1605521968000},
    {'id': '937423697336504', 'geometry': {'type': 'Point', 'coordinates': [37.8789445, 40.984826099972]}, 'captured_at': 1689176328000},
    {'id': '977377146719492', 'geometry': {'type': 'Point', 'coordinates': [37.8790928, 40.9831341]}, 'captured_at': 1689266613000},
    {'id': '3533316046905743', 'geometry': {'type': 'Point', 'coordinates': [37.879274799972, 40.9826277]}, 'captured_at': 1689176194000},
    {'id': '3793952034064475', 'geometry': {'type': 'Point', 'coordinates': [37.881153599972, 40.9854363]}, 'captured_at': 1605866175000},
    {'id': '513847396694933', 'geometry': {'type': 'Point', 'coordinates': [37.879353199972, 40.98516]}, 'captured_at': 1605532199000},
    {'id': '771487706841566', 'geometry': {'type': 'Point', 'coordinates': [37.8712066, 40.9847699]}, 'captured_at': 1606231811000},
    {'id': '2849707748602541', 'geometry': {'type': 'Point', 'coordinates': [37.8800706, 40.9855352]}, 'captured_at': 1605544655000},
    {'id': '4774846385864658', 'geometry': {'type': 'Point', 'coordinates': [37.8807266, 40.9831871]}, 'captured_at': 1605801964000},
    {'id': '475426690182556', 'geometry': {'type': 'Point', 'coordinates': [37.880676999972, 40.985701699972]}, 'captured_at': 1605535083000},
    {'id': '919003785616842', 'geometry': {'type': 'Point', 'coordinates': [37.8816689, 40.980485199972]}, 'captured_at': 1606219621000},
    {'id': '1830227567379288', 'geometry': {'type': 'Point', 'coordinates': [37.878186999972, 40.9848214]}, 'captured_at': 1689266687000},
    {'id': '258601149390754', 'geometry': {'type': 'Point', 'coordinates': [37.880720199972, 40.985857299972]}, 'captured_at': 1605544425000},
    {'id': '796317724581591', 'geometry': {'type': 'Point', 'coordinates': [37.880620933495, 40.98494564839]}, 'captured_at': 1605269209165},
    {'id': '816991235587573', 'geometry': {'type': 'Point', 'coordinates': [37.871476399972, 40.984299399972]}, 'captured_at': 1606231781000},
    {'id': '984689102302118', 'geometry': {'type': 'Point', 'coordinates': [37.8767083, 40.986107799972]}, 'captured_at': 1606231867000},
    {'id': '1656968594135032', 'geometry': {'type': 'Point', 'coordinates': [37.874749299972, 40.9803589]}, 'captured_at': 1689176142000},
    {'id': '1280775106807887', 'geometry': {'type': 'Point', 'coordinates': [37.8775914, 40.982998099972]}, 'captured_at': 1689176167000}
]

m = folium.Map(location=[40.9815, 37.8750], zoom_start=15)

for item in data:
    coordinates = item['geometry']['coordinates']
    folium.Marker(
        location=[coordinates[1], coordinates[0]], 
        popup=f"ID: {item['id']}\nZaman: {pd.to_datetime(item['captured_at'], unit='ms')}",
        icon=folium.Icon(color='blue')
    ).add_to(m)

m


# In[ ]:




