import requests

resp = requests.get(
    "https://scrapethissite.com/pages/advanced/?gotcha=headers")
print(resp.text)
assert "bot detected" not in resp.text
