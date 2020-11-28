# AnimeDownload
哔哩哔哩视频下载


最大带宽批量下载B站flv格式视频（目前仅番剧），使用aria2c，多线程，自动重命名，批量下载弹幕（xml），可转换为ass，视频flv清晰度可选

## 下载地址：https://zhiyuyu.lanzoui.com/is8vgiuqcof 【2020.11.28】

### 如何使用？

打开AnimeDownload.exe输入`番剧的md号`和`是否为区域限定(仅小写y)`即可以开始下载

### 首次使用：

打开有谷歌内核的浏览器，登录哔哩哔哩，按F12，到network选项卡，点一个抓到的链接，到Request Headers里找cookie，把他的值替换bilibili.cookies文件中的内容

配置 AnimeDownloadConfig.json 文件
直接以记事本打开，修改你想要的设置，注释均在文中
 ```
{
    "animation": {
        "md": [],
        "qn": "112",
        "qn_?": " 画质:qn 4K   :120    1080p60:116    1080p+:112    720p60:74",
        "qn_??": "画质:qn 1080p:80     720p   :64     480p  :32     360p  :16",
        "ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    },
    "aria2c": {
        "allocation": "falloc",
        "allocation_?": "none:不预先分配空间",
        "allocation_??": "falloc:预先分配空间",
        "currentdownload": "10",
        "currentdownload_?": "同时文件下载数",
        "serverconnection": "16",
        "serverconnection_?": "服务器连接数，最大16",
        "split": "20",
        "split_?": "单任务线程数",
        "aria2c_ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    },
    "danmaku2ass": {
        "danmaku2ass_option": "",
        "danmaku2ass_option_?": "来自 https://github.com/m13253/danmaku2ass",
        "danmaku2ass_option_??": "-fs 50 -a 30",
        "danmaku2ass_option_???": "像命令行参数一样可以控制产生的弹幕",
        "danmaku2ass_option_????": "如_??示例可调整弹幕大小为50，不透明度为30",
        "danmaku2ass_option_?????": "其他详细命令可到_?处地址查看",
        "danmaku2ass_option_??????": "再次谢谢原作者"
    },
    "work": {
        "is_xml_download": "",
        "is_xml_download_?": "是否下载弹幕（仅小写y）",
        "is_danmaku2ass": "",
        "is_danmaku2ass_?": "是否把弹幕转换为字幕（仅小写y）",
        "is_admination_download": "y",
        "is_admination_download_?": "是否下载番剧视频（仅小写y）"
    },
    "path": {
        "download_path": "D:/HHT/哔哩哔哩动画/AnimeDownload",
        "download_path_?": "番剧保存目录，路径中如果有“反斜杠”请改为“斜杠”，目录不存在将自动创建"
    },
    "other":{
        "epinfo_output": "",
        "remove_download_url": "y"
    },
    "author":{
        "name": "ZhiyuShang",
        "referer": "https://github.com/1299172402/AnimeDownload",
        "license": "Please let me know if you intend to release revised program."
    }
}
 ```

---

### 如何获取md号？

https://www.bilibili.com/bangumi/media/md28229899/?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2

如上面网址md后面的28229899就是md号

### 使用py直接运行的话请先安装aria2c
### 如何获取aria2c？

https://aria2.github.io/ 
