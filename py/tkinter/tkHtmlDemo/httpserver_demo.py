import tempfile
import webbrowser
import threading
import http.server
import socketserver
import os

# Step 1: Write HTML content to a temp file
html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Temporary HTML</title>
    <script>
        window.addEventListener('unload', function () {
            navigator.sendBeacon('http://localhost:8000/closed');
        });
    </script>
</head>
<body>
    <h1>Hello, this is a temporary HTML file!</h1>
    <p>Close this tab or window to delete the file.</p>
</body>
</html>
"""

temp_file = tempfile.NamedTemporaryFile(suffix=".html", delete=False)
temp_file.write(html_content.encode('utf-8'))
temp_file.close()

# Step 2: Simple handler to detect "unload" beacon
class CloseHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/closed":
            print("Browser closed the window.")
            # Stop the server
            threading.Thread(target=server.shutdown).start()
            self.send_response(200)
            self.end_headers()

# Step 3: Start local server in a separate thread
server = socketserver.TCPServer(("localhost", 8000), CloseHandler)
threading.Thread(target=server.serve_forever, daemon=True).start()

# Step 4: Open browser to temp file
webbrowser.open(f"file://{temp_file.name}")

# Step 5: Wait until server shutdown triggered
server.serve_forever()

# Step 6: Cleanup
os.remove(temp_file.name)
print("Temporary HTML file deleted.")
