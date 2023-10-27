from scripts.osm.op_interpreter import op_interpreter
from scripts.osm.op_scraper import op_scraper
from scripts.osm.op_to_geojson import op_to_geojson
from scripts.logging import info
import json


def geojson(area_iso: str, target: str, tags: dict) -> dict:
    query = op_interpreter(area_iso, target, tags)
    op_data = op_scraper(query)
    return op_to_geojson(op_data)
