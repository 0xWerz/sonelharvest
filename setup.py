
import setuptools


setuptools.setup(
    name="sonelharvest",
    description="Sonelharvest is a opensource scraping tool to collect and handle spatial GIS data",
    author="Werz - Musa",
    author_email="contact@werz.info",
    keywords=["sonelmap", "GIS", "OSM", "spatial data",
              "power" "infrastructure", "power GIS data"],
    version="0.1",
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "sonelharvest=sonelharvest.cli:main"
        ]
    },
    project_urls={
        "Source": "https://github.com/sonelmap/sonelharvest",
        "Documentation": "https://github.com/sonelmap/sonelharvest/blob/master/README.md",
    },
    install_requires=[
        "requests",
        "json"
    ],
)
