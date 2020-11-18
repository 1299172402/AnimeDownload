import requests
import os
import json

md = "0"
ss = "0"
AnimeTitle = ""

ua = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
cookies = "_uuid=xxx; buvid3=xxx; CURRENT_FNVAL=80; blackside_state=1; sid=5phw8t6f; bsource=search_bing; DedeUserID=498766638; DedeUserID__ckMd5=axxx; SESSDATA=xxx; bili_jct=e8340d45xxxxxx907; LIVE_BUVID=AUxxxxx822; CURRENT_QUALITY=80; rpdid=|(k|mmJlY||m0J'uY|lY~)kYk; PVID=3; bfe_id=1xxxxa6"
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
workpath = r"D:\HHT\哔哩哔哩动画\AnimeDownload"
danmaku2ass_path = r"D:\HHT\coooooding\AnimationDownload\danmaku2ass.py"
animation_path = r""

qn = "80"

aria2c_path = r"D:\HHT\coooooding\AnimationDownload\aria2c.exe"
currentdownload = "10" # 同时文件下载数
split = "20" # 单任务线程数
allocation = "falloc" # aria2c --help=file-allocation
serverconnection = "16" # 服务器连接数
cookies_path = r"D:\HHT\coooooding\AnimationDownload\bilibili.cookies"

is_xml_download = "y"
is_danmaku2ass = "y"
is_admination_download = "y"

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
    animation_path = os.path.join(workpath, f"s{ss}-{AnimeTitle}")
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
    os.system(f"python {danmaku2ass_path} {animation_path}")

def AnimationDownloadList():
    global epsinfo, ss
    f = open(os.path.join(workpath, f"s{ss}.txt"), "w", encoding="utf-8")
    for ep in epsinfo:
        cid = ep["cid"]
        aid = ep["aid"]
        blv = ep["title"] + ".flv"
        url = f"https://api.bilibili.com/pgc/player/web/playurl?cid={cid}&qn={qn}&fourk=1&avid={aid}"
        res = json.loads(requests.get(url, headers=headers_cookies).text)
        if res["code"] != 0:
            print(res)
            continue
        downloadurl = res["result"]["durl"][0]["backup_url"][1]
        f.write(downloadurl + "\n")
        f.write(f""" out={blv} \n""")

def AnimationDownload():
    global ss, aria2c_path, currentdownload, split, allocation, serverconnection, cookies_path, ua
    file = os.path.join(workpath, f"s{ss}.txt")
    command = f"""{aria2c_path} --referer="https://www.bilibili.com/" --input-file="{file}" --file-allocation={allocation} --dir="{animation_path}" -c --max-concurrent-downloads={currentdownload} --split={split} --load-cookies={cookies_path} --max-connection-per-server={serverconnection}"""
    print(command)
    os.system(command)

def main():
    print("Welcome to Bilibili Animation Download")

    global md
    md = input("md: ")
    GetAnimeInfo()
    GetEpInfo()
    for ep in epsinfo:
        print(ep)

    if is_xml_download == "y":
        DanmakuDownload()
    if is_danmaku2ass == "y":
        Danmaku2ass()

    if is_admination_download == "y":
        AnimationDownloadList()
        AnimationDownload()

if __name__ == '__main__':
    main()
