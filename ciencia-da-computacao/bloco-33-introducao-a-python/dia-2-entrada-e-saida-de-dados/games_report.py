import json

# json.load carrega do arquivo
# json.loads carrega de variavel

file = open("data/video_games.json", "r")
video_games = json.load(file)
file.close()

print(type(video_games))
