import json


def get_proxy_list(fname):
    with open(fname, "r") as f:
        j = json.load(f)
    
    return ["%s://%s:%d" % (item["type"], item["ip"], item["port"]) for item in j["proxy_list"]]

def get_song_list(fname):
    with open(fname, "r") as f:
        j = json.load(f)
    
    return j["song_list"]

