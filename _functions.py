import json
import numpy as np
import pandas as pd
import matplotlib as plt
import requests

chunk_size = 100


def fill_random():
    sz = 100
    df = pd.DataFrame({
        'id': range(1, sz+1),
        'sessionId': np.random.randint(1, sz, size=(sz)),
        'previousFrameId': np.random.randint(1, sz, size=(sz)),
        'time':  range(1, sz+1),
        'speed': np.random.random(size=(sz)),
        'latitude': np.random.uniform(-90, 90, size=(sz)),
        'longitude': np.random.uniform(-180, 180, size=(sz)),
        'linearAccelerationX': np.random.random(size=(sz)),
        'linearAccelerationY': np.random.random(size=(sz)),
        'linearAccelerationZ': np.random.random(size=(sz)),
        'gravityAccelerationX': np.random.random(size=(sz)),
        'gravityAccelerationY': np.random.random(size=(sz)),
        'gravityAccelerationZ': np.random.random(size=(sz)),
        'rotationDeltaMatrixField0': np.random.random(size=(sz)),
        'rotationDeltaMatrixField1': np.random.random(size=(sz)),
        'rotationDeltaMatrixField2': np.random.random(size=(sz)),
        'rotationDeltaMatrixField3': np.random.random(size=(sz)),
        'rotationDeltaMatrixField4': np.random.random(size=(sz)),
        'rotationDeltaMatrixField5': np.random.random(size=(sz)),
        'rotationDeltaMatrixField6': np.random.random(size=(sz)),
        'rotationDeltaMatrixField7': np.random.random(size=(sz)),
        'rotationDeltaMatrixField8': np.random.random(size=(sz)),
        'angleSpeedX': np.random.random(size=(sz)),
        'angleSpeedY': np.random.random(size=(sz)),
        'angleSpeedZ': np.random.random(size=(sz))
    })

    df.to_csv('data.csv', index=False)


def add_elevation(data):
    elev = []
    for first_elem in range(0, len(data), chunk_size):
        locations = '|'.join([f"{data['latitude'][row + first_elem]},{data['longitude'][row + first_elem]}" for row in range(min(chunk_size, len(data) - first_elem))])
        url = f"https://api.opentopodata.org/v1/mapzen?locations={locations}"
        response = requests.get(url)
        result = json.loads(response.text)
        for res in result['results']:
            print(f"Latitude: {res['location']['lat']}, Longitude: {res['location']['lng']}, Elevation: {res['elevation']}")
        elev = elev + [res['elevation'] for res in result['results']]
    elevation_df = pd.DataFrame([{'elevation': el} for el in elev])
    merged_df = pd.concat([data, elevation_df], axis=1)
    merged_df.to_csv('Data.csv', index=False)
    data = merged_df
    return data


url = "http://158.160.79.188:8000/GetAll"
#response = requests.get(url)
#answer = json.loads(response.text)
#answer

#fill()

data = pd.read_csv("Data.csv")

if 'elevation' not in data.columns and 0:
    data = add_elevation(data)

data['totalAcceleration'] = (data['linearAccelerationX'] ** 2 + data['linearAccelerationY'] ** 2 + data['linearAccelerationZ'] ** 2) ** 0.5
data['totalAngleSpeed'] = (data['angleSpeedX']**2 + data['angleSpeedY']**2 + data['angleSpeedZ']**2) ** 0.5
data['time'] = data['time'] - data['time'][0]



data.plot('time', ['elevation', 'totalAcceleration', 'totalAngleSpeed'], subplots=True)
plt.show()
