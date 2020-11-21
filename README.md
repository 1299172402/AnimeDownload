# AnimeDownload
哔哩哔哩视频下载


最大带宽批量下载B站flv格式视频（目前仅番剧），使用aria2c，多线程，自动重命名，批量下载弹幕（xml），可转换为ass，视频flv清晰度可选

## exe打包下载：https://zhiyuyu.lanzoui.com/iMy47imr0if 【2020.11.21】

首次使用：

1. 打开哔哩哔哩，登录B站账号。用谷歌内核的浏览器，按F12到Network选项卡获取你的cookies，保存cookies到本地的文件中例如 bilibili.cookies
注意：直接将cookies以文本形式保存即可

2. 配置AnimeDownloadConfig.json 文件
 直接以记事本打开
 ```
 {
    "animation": {
        "md": [],
        "qn": "80",
        "ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    },
    "aria2c": {
        "allocation": "falloc",
        "aria2c_path": "D:\\AnimeDownload\\aria2c.exe",
        "cookies_path": "D:\\AnimeDownload\\bilibili.cookies",
        "currentdownload": "10", 同时文件下载数
        "serverconnection": "16", 服务器连接数
        "split": "20", 单任务线程数
        "aria2c_ua": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    },
    "danmaku2ass": {
        "danmaku2ass_path": "D:\\AnimeDownload\\danmaku2ass.exe",
        "danmaku2ass_option": "" （可选）-fs 50 指xml2ass是字幕字号为50
    },
    "work": {
        "is_xml_download": "y", 下载弹幕吗？是:仅输入小写的y。不是：删除小写的y
        "is_danmaku2ass": "y", 要把xml弹幕转换为ass字幕吗吗？是:仅输入小写的y。不是：删除小写的y
        "is_admination_download": "y" 下载动漫吗？是:仅输入小写的y。不是：删除小写的y
    },
    "path": {
        "workpath": "D:\\AnimeDownloadDir" 番剧的下载目录
    },
    "other":{
        "epinfo_output": ""
    }
}
 ```
 
 qn：下载的画质
```
4K ：120
1080p60：116
720p60：74
1080p+：112
1080p：80
720p：64
480p：32
360p：16
```

aria2c 的 allocation：文件分配方式
 ```
 --file-allocation=METHOD     Specify file allocation method.
                              'none' doesn't pre-allocate file space. 'prealloc'
                              pre-allocates file space before download begins.
                              This may take some time depending on the size of
                              the file.
                              If you are using newer file systems such as ext4
                              (with extents support), btrfs, xfs or NTFS
                              (MinGW build only), 'falloc' is your best
                              choice. It allocates large(few GiB) files
                              almost instantly. Don't use 'falloc' with legacy
                              file systems such as ext3 and FAT32 because it
                              takes almost same time as 'prealloc' and it
                              blocks aria2 entirely until allocation finishes.
                              'falloc' may not be available if your system
                              doesn't have posix_fallocate() function.
                              'trunc' uses ftruncate() system call or
                              platform-specific counterpart to truncate a file
                              to a specified length.
```

### 注意！！！
**aria2c_path** 输入aria2c.exe 的位置（绝对路径）

**cookies_path** 输入保存cookies的文件位置（绝对路径）

**danmaku2ass_path** 输入danmaku2ass.exe的绝对路径

**workpath** 输入番剧的下载目录（绝对路径）

输入路径时一定一定要***注意路径的反斜杠要打两次***

以后打开AnimeDownload.exe输入番剧的md号就可以了

---

如何获取md号？

https://www.bilibili.com/bangumi/media/md28229899/?spm_id_from=666.25.b_6d656469615f6d6f64756c65.2

如上面网址md后面的28229899就是md号
