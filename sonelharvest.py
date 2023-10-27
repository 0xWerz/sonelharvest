from scripts.geojson import geojson
from web import start_web_interface
import sys
from datetime import datetime
import json


def main():
    country = input("Country code: (Default: DZ) ")
    target = input("Target: (Deafult: power) ")
    tags = input("Query Tags: (exp: tower, generator, line) ")
    export_type = input(
        f"Export type:\n1. GeoJSON\n2. CSV\n3. KML\n(Default: 1) ")
    if not country:
        country: str = "DZ"
    if not target:
        target: str = "power"
    if not tags:
        print("INFO: No tags to query were passed")
        sys.exit()
    if export_type not in ["1", "2", "3"]:
        export_type = "1"

    tags = tags.replace(" ", "").split(",")
    if export_type == "1":
        gj = geojson(country, target, tags)
        time = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        with open(f"data/geojson{time}.geojson", "w") as f:
            json.dump(gj, f, indent=4)
            print(
                f"GeoJSON data saved to data/geojson/{target}-{time}.geojson")
        return


if __name__ == "__main__":
    action = sys.argv[1] if len(sys.argv) > 1 else "cli"
    start_web_interface() if action == "web" else main()
