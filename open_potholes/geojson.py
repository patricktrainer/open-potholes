import json

# open the json file
def get_data():
    with open("potholes.json") as f:
        data = json.load(f, parse_int=int)
    return data


# convert the json file to geojson
def to_geojson(json_array):
    geojson = {
        "type": "FeatureCollection", 
        "features": []
    }

    for item in json_array:
        feature = {
            "type": "Feature",
            "properties": {
                "service_request": item["service_request"],
                "request_type": item["request_type"],
                "request_reason": item["request_reason"],
                "date_created": item["date_created"],
                "date_modified": item["date_modified"],
                "request_status": item["request_status"],
                "final_address": item["final_address"],
            },
            "geometry": {
                "type": "Point",
                "coordinates": [float(item["longitude"]), float(item["latitude"])],
            },
        }

        geojson["features"].append(feature)
    return geojson


# run the functions
data = get_data()
geojson = to_geojson(data)

with open("potholes.geojson", "w") as f:
    json.dump(geojson, f, indent=2)

