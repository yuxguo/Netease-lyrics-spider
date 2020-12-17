import json
import utils
import requests
import multiprocessing
import random
import re

service_url = "127.0.0.1:3000"
song_list = utils.get_song_list(fname="../configs/song_list.json")
proxy_list = utils.get_proxy_list(fname="../configs/proxy_list.json")


def worker(song_id):

    request_url = "http://%s/lyric?id=%s" % (service_url, song_id)
    if proxy_list != []:
        request_url += "&proxy=%s" % random.choice(proxy_list)

    # request api
    # TODO: use try ... expect ...
    try:
        data = requests.get(request_url).text
    except requests.ConnectionError:
        return 
    print(data)

    # decode json
    data = json.loads(data).get("lrc", None)
    if data is None:
        return
    data = data["lyric"]

    # filter out timestamp
    data = re.sub(r"\[.*\]", "", data)

    # write file
    with open("../data/%s.txt" % song_id, "w") as f:
        f.write(data)


def main():
    # multiporcessing
    with multiprocessing.Pool(8) as p:
        p.map(worker, song_list)


if __name__ == "__main__":
    main()
