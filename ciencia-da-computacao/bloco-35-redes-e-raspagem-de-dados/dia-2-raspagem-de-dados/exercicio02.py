import requests


def main():
    data = requests.get("https://api.github.com/users")
    if data.status_code == 200:
        items = data.json()
        for u in items:
            print(f"{u['login']} {u['url']}")


if __name__ == "__main__":
    main()
