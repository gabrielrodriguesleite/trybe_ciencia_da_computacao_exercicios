import requests

resp = requests.get(
    "https://scrapethissite.com/pages/advanced/?gotcha=headers",
    headers={"User-agent": "Mozilla", "Accept": "text/html"},
    )
print(resp.text)
assert "bot detected" not in resp.text
