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

# print(type(video_games))
# print(video_games[2]["Metadata"]["Genres"].split(','))

# generos
game_genres = set()
for game in video_games:
    for genre in game["Metadata"]["Genres"].split(','):
        game_genres.add(genre)

print(game_genres)

# consoles
consoles = set()
for game in video_games:
    consoles.add(game["Release"]["Console"])

print(consoles)
