from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Serve the main HTML file
        html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/style.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <title>SonelHarvest - OpenStreetMap Data Extractor</title>
</head>
<body>
    <div class="container">
        <header class="header">
            <h1>🌍 SonelHarvest</h1>
            <p class="subtitle">Extract OpenStreetMap infrastructure data with ease</p>
        </header>

        <main class="main-content">
            <div class="form-container">
                <form class="data-form" action="#">
                    <div class="form-group">
                        <label for="country">Country Code</label>
                        <input type="text" id="country" placeholder="DZ" maxlength="2">
                        <small>ISO 3166-1 alpha-2 code (e.g., DZ for Algeria)</small>
                    </div>

                    <div class="form-group">
                        <label for="target">Target Infrastructure</label>
                        <input type="text" id="target" placeholder="power">
                        <small>Infrastructure type (e.g., power, water, transport)</small>
                    </div>

                    <div class="form-group">
                        <label for="tags">Tags</label>
                        <input type="text" id="tags" placeholder="towers, line, generator, station">
                        <small>Comma-separated OSM tags to search for</small>
                    </div>

                    <div class="form-row">
                        <div class="form-group">
                            <label for="format">Export Format</label>
                            <select id="format">
                                <option value="geojson" selected>GeoJSON</option>
                                <option value="kml">KML</option>
                                <option value="overpass">Overpass</option>
                            </select>
                        </div>

                        <div class="form-group checkbox-group">
                            <label class="checkbox-label">
                                <input type="checkbox" id="map-presentation">
                                <span class="checkmark"></span>
                                Map data presentation
                            </label>
                        </div>
                    </div>

                    <button type="submit" class="submit-btn">
                        <span class="btn-text">Extract Data</span>
                        <span class="btn-loading">⏳ Processing...</span>
                    </button>

                    <div id="status" class="status-message"></div>
                </form>
            </div>

            <div class="results-container">
                <div class="results-header">
                    <h3>📊 Results</h3>
                    <button id="copy-btn" class="copy-btn" style="display: none;">📋 Copy</button>
                </div>
                <textarea id="results" placeholder="Your extracted data will appear here..." readonly></textarea>
            </div>
        </main>
    </div>
    <script src="/app.js"></script>
</body>
</html>"""

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
        return