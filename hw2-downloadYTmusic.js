let YoutubeMp3Downloader = require("youtube-mp3-downloader");

let YD = new YoutubeMp3Downloader({
   "ffmpegPath": "/usr/local/bin/ffmpeg", //ffmpeg的安裝位置
   "outputPath": "./", //存入資料夾./代表本資料夾
   "youtubeVideoQuality": "highest",      」
   "queueParallelism": 2,                
   "progressTimeout": 2000        
});

//https://www.youtube.com/watch?v=ACOqcaKoy7o，把網址的v=後面放入第一個參數，把存入名稱放入第二個參數
YD.download("Vhd6Kc4TZls", "Cold Funk - Funkorama.mp3");

YD.on("finished", function(err, data) {
   console.log(JSON.stringify(data));
});

YD.on("error", function(error) {
   console.log(error);
});

YD.on("progress", function(progress) {
   console.log(JSON.stringify(progress));
});