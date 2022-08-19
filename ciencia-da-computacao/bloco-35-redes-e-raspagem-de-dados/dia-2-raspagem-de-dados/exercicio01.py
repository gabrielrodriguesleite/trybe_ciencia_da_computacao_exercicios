import requests


def main():
    data = requests.get("https://httpbin.org/encoding/utf8")
    print(data.text)


if __name__ == "__main__":
    main()
