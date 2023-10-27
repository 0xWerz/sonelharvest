# sonelharvest

Sonelharvest is a opensource scraping tool to collect and handle spatial GIS data, built **specially** for [sonelmap](https://sonelmap.com)

## Installation

    git clone https://github.com/sonelmap/sonelharvest && cd sonelharvest

## Usage

For the web interface pass the `web` argument

    python3 sonelharvest.py web

For the CLI interface pass the `cli` argument

    python .\sonelharvest.py cli 
    Country code: (Default: DZ) MA 
    Target: (Deafult: power) power
    Query Tags: (exp: tower, generator, line) generator
    Export type: 
    1. GeoJSON   
    2. CSV       
    3. KML       
    (Default: 1) 1
    GeoJSON data saved to data/geojson/power-2023-10-27-14-54-05.geojson
