import json

# json.load carrega do arquivo
# json.loads carrega de variavel

try:
    with open("data/video_games.json", "r") as file:
        video_games = json.load(file)
except json.decoder.JSONDecodeError:
    print("Arquivo inválido")
except FileNotFoundError:
    print("Arquivo inexistente")
finally:
    print("sempre executa finally")

print(type(video_games))
