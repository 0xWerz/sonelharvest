def op_to_geojson(json_data: dict) -> dict:
    """
    Process overpass spatial data and return it in geojson format.
    """

    if not json_data:
        return
    json_data: list = json_data["elements"]
    geojson_data = {
        "type": "FeatureCollection",
        "features": []
    }
    for data in json_data:
        if data["type"] == "node":
            geojson_data["features"].append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [
                        data["lon"],
                        data["lat"]
                    ]
                },
                "properties": {
                    "id": data["id"],
                    "tags": data["tags"]
                }
            })
        elif data["type"] == "way":
            coordinates = []
            for node_id in data["nodes"]:
                node = next(
                    (node for node in json_data if node["id"] == node_id), None)
                if node:
                    coordinates.append([node["lon"], node["lat"]])
            geojson_data["features"].append({
                "type": "Feature",
                "geometry": {
                    "type": "LineString",
                    "coordinates": coordinates
                },
                "properties": {
                    "id": data["id"],
                    "tags": data["tags"]
                }
            })
    return geojson_data
