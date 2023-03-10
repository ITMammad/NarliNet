# NarliNet
NarliNet is A Web Proxy And Virtual Private Network Building System That Developed In Python And It Works With NarliNet Client Applications in All Popular OSs(Like Windows, MacOS, Linux, Android & IOS)

# NarliNet Standard
NarliNet Standards Are Some Rules And Definitions:
1. Narli:
    Narli Is The Electric Message That Transfers Between Client And Nodes And When The Last Node Gets Response, Narli Will Be Back By All Nodes To Client.
2. Node:
    Node(NarliNode) Is A Server That Runs NarliNet And Can Be Used As A Middleware Narli Transfer Layer.
3. NarliNet:
    NarliNet Isn't All Server That They Run NarliNet Project, NarliNet Is Only A Server That Have These Specifications:
    1. NarliWS(Narli WebSocket) Shouldn't Run On Port 80;
    2. It Should Can Forward Narli To Next Node;
    3. That's Owner Should Accepts Our ToS;
4. NarliConfig:
    Narli Config Is A Configuration Object That Sent In Narli.
    It Likes This Example:
    ```json
    {
        "nodes": [
            {
                "protocol": "ws",
                "uri": "10.10.10.10",
                "port": "4900",
                "path": "/",
                "passed": true
            }
        ],
        "req": {
            "method": "GET",
            "uri": "https://google.com/",
            "headers": {
                ":authority": "www.google.com",
                ":method": "GET",
                ":path": "/",
                ":scheme": "https",
                "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "accept-encoding": "gzip, deflate, br",
                "cache-control": "max-age=0",
                "upgrade-insecure-requests": "1",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
            }
        }
    }
    ```
    Narli Config Just Is That `Nodes` Key Of Narli
    And This JSON Text Is Full Narli Data, That Encrypts And Sent To NarliNet.

# How To RUN
Here Is How to run This Project In Python Interface.
```
Note: If You Want To Run NarliNet In Docker Interface, You Should Build Your Own Image But We Have A Docker Interface And Dockerfile In Another Repository(Named: NarliNet-Docker), Then Clone This Repository In Path: "{Path To Cloned Project}/NarliNet" And Build It.
```
1. Install Requirements:
    Run Command Below To Install Required Libraies:
    ```
    pip install -r requirements.txt
    ```
2. Run NarliNet(Project):
    Run This Command To Run NarliNet Project:
    ```
    py main.py
    ```
3. Congratulation, You Have Runned Your NarliNet;
# Developers
Developed By ❤ From ITMammad;
# Last Say
Nothing, Just Use It Correctly...
