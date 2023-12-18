import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

file = pd.read_csv("Data.csv")

if 'elevation' not in file.columns:
    locations = '|'.join([f"{file['latitude'][row]},{file['longitude'][row]}" for row in range(len(file))])
    url = f"https://api.opentopodata.org/v1/mapzen?locations={locations}"
    response = requests.get(url)
    result = json.loads(response.text)
    for res in result['results']:
        print(f"Latitude: {res['location']['lat']}, Longitude: {res['location']['lng']}, Elevation: {res['elevation']}")
    elevation_df = pd.DataFrame([{'elevation': res['elevation']} for res in result['results']])
    merged_df = pd.concat([file, elevation_df], axis=1)
    merged_df.to_csv('Data.csv', index=False)
    file = merged_df

file['totalAcceleration'] = (file['linearAccelerationX'] ** 2 + file['linearAccelerationY'] ** 2 + file['linearAccelerationZ'] ** 2) ** 0.5
file['totalangleSpeed'] = (file['angleSpeedX']**2 + file['angleSpeedY']**2 + file['angleSpeedZ']**2) ** 0.5
file['time'] = file['time'] - file['time'][0]



file.plot('time', 'elevation')
plt.show()
