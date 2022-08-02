import json

# json.load carrega do arquivo
# json.loads carrega de variavel

with open("data/video_games.json", "r") as file:
    video_games = json.load(file)


print(type(video_games))
