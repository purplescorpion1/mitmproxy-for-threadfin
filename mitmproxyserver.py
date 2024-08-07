from mitmproxy import http

def request(flow: http.HTTPFlow) -> None:
    # Add headers for requests
    flow.request.headers["Referer"] = "https://yourrerfer.com"
    flow.request.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:126.0) Gecko/20100101 Firefox/126.0"

def response(flow: http.HTTPFlow) -> None:
    # Optionally modify response headers here if needed
    pass
