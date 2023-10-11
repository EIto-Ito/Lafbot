from http.server import BaseHTTPRequestHandler
import json
from urllib.parse import parse_qs, urlparse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.date_time_string())

        # リクエストURIを解析
        parsed_url = urlparse(self.path)

        # クエリストリングを解析
        query_parameters = parse_qs(parsed_url.query)
        print(query_parameters)
        # クエリストリングから特定のパラメータを取得
        if "q" in query_parameters:
            param_value = query_parameters["q"][0]
        print(param_value)

        self.send_response(200)
        self.send_header("Content-type", "application/json")

        self.end_headers()
        self.wfile.write("a".encode("utf-8"))
        return
