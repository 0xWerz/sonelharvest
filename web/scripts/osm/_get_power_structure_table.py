import requests
from bs4 import BeautifulSoup as bs
import json


def scrape_table_tag_to_dict() -> dict:
    """
    load the html table of tags from the OSM wiki and return it as a structured dict.
    """
    with open("assets/osm/power-structure.html", "r") as f:
        html = f.read()
    soup = bs(html, 'html.parser')
    table = soup.find('table', {'class': 'wikitable taginfo-taglist'})
    rows = table.find_all("tr")

    structure_dict = []
    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 0:
            tag = cells[1].text.strip()
            type = cells[2].find_all("img")
            # get type from image src file name
            if len(type) > 0:
                type = [t["src"].split("/")[-1].split(".")[0] for t in type]
            description = cells[3].text.strip()
            image = cells[5].find("img")["src"].replace(
                "100px", "1080px") if cells[5].find("img") else None
            structure_dict.append({
                "tag": tag,
                "description": description,
                "type": type,
                "image": image
            })
    with open("assets/osm/power-structure.json", "w") as f:
        json.dump(structure_dict, f)
    print(structure_dict)
    return structure_dict


scrape_table_tag_to_dict()
