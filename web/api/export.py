from http.server import BaseHTTPRequestHandler
import json
import sys
import os

# Add the web directory to the Python path to import local modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from scripts.geojson import geojson
except ImportError as e:
    print(f"Import error: {e}")
    # Fallback if import fails
    def geojson(country, target, tags):
        return {"error": f"geojson module not available: {e}"}

class handler(BaseHTTPRequestHandler):

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            country, target, tags = data['country'], data['target'], data['tags']

            if not country:
                country = "DZ"
            if not target:
                target = "power"
            if tags[0] == '':
                error_response = json.dumps({
                    "error": "no tags to query recieved. Please enter the tags you want to query",
                })
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(error_response.encode('utf-8'))
                return

            geojson_data = geojson(country, target, tags)

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(geojson_data).encode('utf-8'))

        except Exception as e:
            print(e)
            error_response = json.dumps({"error": f'{e}'})
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(error_response.encode('utf-8'))

        return