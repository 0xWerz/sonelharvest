from http.server import BaseHTTPRequestHandler
import os

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Serve the main HTML file
        html_content = """<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/style.css">
    <title>SonelHarvest</title>
</head>

<body>
    <div>
        <form action="#">
            <input type="text" placeholder="Country code: (Default: DZ)">
            <input type="text" placeholder="Target: (Default: power)">
            <input type="text" placeholder="Tags: (ex: towers, line, generator, station) (comma between tags)">
            <!-- <label for="select-menu">export data type:</label> -->
            <select>
                <option value="geojson" selected>GEOJSON</option>
                <option value="kml">KML</option>
                <option value="overpass">OVERPASS</option>
            </select>
            <span>
                <input type="checkbox" name="" id="db">
                <label for="db">Map data presentation</label>
            </span>
            <button type="submit">Submit</button>
            <p id="res"></p>
        </form>

        <textarea rows="35">
        </textarea>
    </div>
    <script src="/app.js"></script>
</body>

</html>"""

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html_content.encode('utf-8'))
        return