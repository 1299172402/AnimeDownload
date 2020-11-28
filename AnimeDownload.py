import requests
import os
import json

md = "0"
ss = "0"
qn = "80"
tw = ""
AnimeTitle = ""
ua = ""
cookies = ""

headers = {
    "Origin": "https://www.bilibili.com",
    "Referer": f"https://www.bilibili.com/bangmumi/play/ss{ss}",
    "User-Agent": ua,
}

headers_cookies = {
    "Origin": "https://www.bilibili.com",
    "Referer": f"https://www.bilibili.com/bangmumi/play/ss{ss}",
    "User-Agent": ua,
    "Cookies": cookies,
}

epsinfo = []
download_path = ""
animation_path = r""

currentdownload = "10" # 同时文件下载数
split = "20" # 单任务线程数
allocation = "falloc" # aria2c --help=file-allocation
serverconnection = "16" # 服务器连接数
aria2c_ua = ""

danmaku2ass_option = ""

is_xml_download = "y"
is_danmaku2ass = "y"
is_admination_download = "y"

epinfo_output = ""
remove_download_url = ""

workpath = os.path.dirname(os.path.abspath(__file__))
danmaku2ass_path = os.path.join(workpath, "danmaku2ass.py")
# danmaku2ass_path = os.path.join(workpath, "danmaku2ass.exe")
aria2c_path = os.path.join(workpath, "aria2c.exe")
cookies_path = os.path.join(workpath, "bilibili.cookies")


def init():
    with open(os.path.join(workpath, "AnimeDownloadConfig.json"), "r", encoding="utf-8") as f:
        config = json.loads(f.read())

    global download_path
    download_path = config["path"]["download_path"]

    global md, qn, ua
    # md = "0"
    qn = config["animation"]["qn"]
    ua = config["animation"]["ua"]

    global allocation, currentdownload, serverconnection, split, aria2c_ua
    allocation = config["aria2c"]["allocation"]
    currentdownload = config["aria2c"]["currentdownload"]
    serverconnection = config["aria2c"]["serverconnection"]
    split = config["aria2c"]["split"]
    aria2c_ua = config["aria2c"]["aria2c_ua"]

    global danmaku2ass_option
    danmaku2ass_option = config["danmaku2ass"]["danmaku2ass_option"]

    global is_xml_download, is_danmaku2ass, is_admination_download
    is_xml_download = config["work"]["is_xml_download"]
    is_danmaku2ass = config["work"]["is_danmaku2ass"]
    is_admination_download = config["work"]["is_admination_download"]

    global epinfo_output, remove_download_url
    epinfo_output = config["other"]["epinfo_output"]
    remove_download_url = config["other"]["remove_download_url"]

    with open(cookies_path, "r") as f:
        cookies = f.read()

def TitleRename(title):
    title = title.replace("/", " ")
    title = title.replace("\\", " ")
    title = title.replace(":", " ")
    title = title.replace("*", " ")
    title = title.replace("?", " ")
    title = title.replace("\"", " ")
    title = title.replace("<", " ")
    title = title.replace(">", " ")
    title = title.replace("|", " ")
    while title.replace("  "," ") != title:
        title = title.replace("  "," ")
    while title[-1] == " ":
        title = title[:-1]
    return title

def GetAnimeInfo():
    global md, ss, AnimeTitle
    url = f"https://api.bilibili.com/pgc/review/user?media_id={md}"
    info = json.loads(requests.get(url, headers=headers).text)
    md = info["result"]["media"]["media_id"]
    ss = info["result"]["media"]["season_id"]
    AnimeTitle = info["result"]["media"]["title"]
    AnimeTitle = TitleRename(AnimeTitle)

    global animation_path
    animation_path = os.path.join(download_path, f"s{ss}-{AnimeTitle}")
    if not os.path.exists(animation_path):
        os.makedirs(animation_path)


def GetEpInfo():
    global season_id
    url = f"https://api.bilibili.com/pgc/web/season/section?season_id={ss}"
    res = requests.get(url, headers=headers)
    info = json.loads(res.text)
    info = info["result"]["main_section"]["episodes"]
    global epsinfo
    for ep in info:
        title = ep["title"] if len(ep["title"])>=2 else "0"+ep["title"]
        title = title + " " + ep["long_title"]
        title = TitleRename(title)
        epinfo = {
            "aid": ep["aid"],
            "cid": ep["cid"],
            "title": title
        }
        epsinfo.append(epinfo)

def DanmakuDownload():
    for ep in epsinfo:
        cid = ep["cid"]
        xml = ep["title"] + ".xml"
        url = f"https://api.bilibili.com/x/v1/dm/list.so?oid={cid}"
        res = requests.get(url, headers=headers)
        global animation_path
        with open(os.path.join(animation_path, xml), "wb") as f:
            f.write(res.content)
            print(f"[xml download SUCCEED] {xml}")

def Danmaku2ass():
    command = f"""python "{danmaku2ass_path}" "{animation_path}" {danmaku2ass_option} """
    # print(command)
    os.system(command)

def AnimationDownloadList():
    global epsinfo, ss
    f = open(os.path.join(download_path, f"s{ss}.txt"), "w", encoding="utf-8")
    for ep in epsinfo:
        cid = ep["cid"]
        aid = ep["aid"]
        blv = ep["title"] + ".flv"

        if tw != "y":
            url = f"https://api.bilibili.com/pgc/player/web/playurl?cid={cid}&qn={qn}&fourk=1&avid={aid}"
        else:
            url = f"https://bilibili-tw-api.kghost.info/pgc/player/web/playurl?cid={cid}&qn={qn}&fourk=1&avid={aid}"
        
        res = json.loads(requests.get(url, headers=headers_cookies).text)
        if res["code"] != 0:
            print(f"[{blv}] {res}")
            print(res["code"])

        if tw != "y":
            downloadurl = res["result"]["durl"][0]["backup_url"][1]
        else:
            downloadurl = res["result"]["durl"][0]["url"]
        
        f.write(downloadurl + "\n")
        f.write(f""" out={blv} \n""")

def AnimationDownload():
    global ss, aria2c_path, currentdownload, split, allocation, serverconnection, cookies_path, aria2c_ua
    file = os.path.join(download_path, f"s{ss}.txt")
    command = f"""{aria2c_path} --referer="https://www.bilibili.com/" --input-file="{file}" --file-allocation={allocation} --dir="{animation_path}" -c --max-concurrent-downloads={currentdownload} --split={split} --load-cookies={cookies_path} --max-connection-per-server={serverconnection} --user-agent={aria2c_ua} """
    print(command)
    os.system(command)

def main():
    print("Welcome to Bilibili Animation Download")
    print("Creative By ZhiyuShang With LOVE")
    print("[Referer](https://github.com/1299172402/AnimeDownload)")

    init()

    global md
    md = input("md: ")
    GetAnimeInfo()
    GetEpInfo()
    for ep in epsinfo:
        print(ep)
    if epinfo_output == "y":
        with open(os.path.join(download_path, f"ss{ss}.json"), "w", encoding="utf-8") as f:
            f.write(json.dumps(epsinfo, ensure_ascii=False, indent=4))
            # ensure_ascii=False 不转码中文
            # indent=4 对齐宽度为4

    global tw
    tw = input("tw[y/n]: ")

    if is_xml_download == "y":
        DanmakuDownload()
    if is_danmaku2ass == "y":
        Danmaku2ass()

    if is_admination_download == "y":
        AnimationDownloadList()
        AnimationDownload()

    if remove_download_url == "y":
        if os.path.exists(os.path.join(download_path, f"s{ss}.txt")):
            os.remove(os.path.join(download_path, f"s{ss}.txt"))

if __name__ == '__main__':
    main()
    author = {
        "name": "ZhiyuShang",
        "referer": "https://github.com/1299172402/AnimeDownload",
        "license": "Please let me know if you intend to release revised program."
    }