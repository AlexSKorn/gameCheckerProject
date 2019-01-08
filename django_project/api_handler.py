import urllib3
import json


api_key = "D5668492339DD5B4362442F46F1710B8"

def main():
    http = urllib3.PoolManager()

    api_key = "D5668492339DD5B4362442F46F1710B8"
    steam_id = 76561198018662845

    urlData = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=" \
    + api_key + "&steamid=" + str(steam_id) + "&include_played_free_games&format=json"
    
    req = http.request('GET', urlData)

    JSON_object = json.loads(req.data.decode("utf-8"))
    print(str(JSON_object))


if __name__ == '__main__':
    main()