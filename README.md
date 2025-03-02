# mitmproxy-for-threadfin
## Referer proxy server injector for Threadfin

### Requirements
Threadfin version 1.2.0 or higher <br>
python version 3 with pip (tested on 3.12.3)

### Install
```
git clone https://github.com/purplescorpion1/mitmproxy-for-threadfin.git
``` 
```
pip install mitmproxy
```

### Usage
Open mitmproxyserver.py with notepad++ or any text code editor <br>
Change https://yourrerfer.com to the url of the referer you want to use <br>
Open cmd/terminal window at the location of mitmproxyserver.py <br>
Enter the following command changing IP to machine running script and what ever port you want to use
```
mitmproxy -s mitmproxyserver.py --listen-host 192.168.1.123 --listen-port 6088
```

### Intergrate with Threadfin

Download the latest version of threadfin from https://github.com/Threadfin/Threadfin - Min version required is 1.2.0 <br>
Make sure the buffer in settings is ffmpeg (maybe a 4mb buffer) and you have pointed to your ffmepeg binary file <br>
<br>
Note latest version of threadfin you set buffer type in playlist settings <br>
<br>
Set tuners in settings to at least 2 (you need to do above first before you can set number of tuners) <br>
<br>
Assuming you have already loaded your EPG urls ready for your playlist <br>
<br>
Load your m3u into threadfin <br>
Give it at least 2 tuners <br>
Under HTTP Proxy IP: put the IP that mitmproxy is on eg 192.168.1.123 <br>
Under HTTP Proxy Port: put the port that mitmproxy is on eg 6088 <br>
Save the playlist <br>
<br>
Double check everything should be automatically mapped assuming the id tags in your EPG match your Playlist. If not you will need to map all your channels <br>
<br>
Add the threadfin m3u/epg address into your player

### Multiple Instances
Just copy and rename mitmproxyserver.py to something else <br>
Make any changes to the referer in the file <br>
Enter the command to start mitmproxy changing the file name and port number <br>

