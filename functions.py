import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import json

chunk_size = 100

def fill():
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

def addElevation(file):
    elev = []
    for first_elem in range(0, len(file), chunk_size):
        locations = '|'.join([f"{file['latitude'][row + first_elem]},{file['longitude'][row + first_elem]}" for row in range(min(chunk_size, len(file) - first_elem))])
        url = f"https://api.opentopodata.org/v1/mapzen?locations={locations}"
        response = requests.get(url)
        result = json.loads(response.text)
        for res in result['results']:
            print(f"Latitude: {res['location']['lat']}, Longitude: {res['location']['lng']}, Elevation: {res['elevation']}")
        elev = elev + [res['elevation'] for res in result['results']]
    elevation_df = pd.DataFrame([{'elevation': el} for el in elev])
    merged_df = pd.concat([file, elevation_df], axis=1)
    merged_df.to_csv('Data.csv', index=False)
    file = merged_df
    return file

#url = "http://158.160.79.188:8000/GetAll"
#response = requests.get(url)
#answer = json.loads(response.text)
answer




exit(0);

#fill()

file = pd.read_csv("Data.csv")

if 'elevation' not in file.columns and 0:
    file = addElevation(file)

file['totalAcceleration'] = (file['linearAccelerationX'] ** 2 + file['linearAccelerationY'] ** 2 + file['linearAccelerationZ'] ** 2) ** 0.5
file['totalAngleSpeed'] = (file['angleSpeedX']**2 + file['angleSpeedY']**2 + file['angleSpeedZ']**2) ** 0.5
file['time'] = file['time'] - file['time'][0]



file.plot('time', ['elevation', 'totalAcceleration', 'totalAngleSpeed'], subplots=True)
plt.show()
