import json


def op_interpreter(area_iso: str, target: str, tags: list) -> str:
    """
    High-level interpreter for Overpass API query language.

    Args:
        area_iso (str): ISO code of the area to query.
        target (str): OSM target to query (e.g. "power", "waterway").
        tags (list): List of OSM tags to query.

    Returns:
        str: Overpass API query string.
    """
    try:
        with open(f'assets/osm/{target}-structure.json', 'r') as f:
            STRUCTURE = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"{target} target not found.")

    mapped_tags = {}
    for tag in tags:
        for item in STRUCTURE:
            if tag == item['tag']:
                mapped_tags[tag] = item['type'][0]

    if not mapped_tags:
        raise ValueError(f"No tags found for {target} with {tags}")

    query = f"[out:json];\narea['ISO3166-1'~'{area_iso}']->.a;\n"

    query += "(\n"
    for tag, type_ in mapped_tags.items():
        query += f"  {type_}['{target}'='{tag}'](area.a);\n"
    query += ");\n"

    query += "out body;\n>;"
    return query
