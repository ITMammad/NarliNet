import requests
import websockets
import ITCryption

def getThisNode(narli):
    nodes = narli.get("nodes")
    if len(nodes) == 1:
        return 0
    else:
        for i in range(len(nodes)):
            if nodes[i].get("passed") == False:
                return i - 1

def getNextNode(narli):
    return getThisNode(narli=narli) + 1

def amILastNode(narli):
    thisNode = getThisNode(narli=narli)
    nodes = narli.get("nodes")
    if thisNode == len(nodes) - 1:
        return True
    else:
        return False

async def iAmLastNode(narli):
    req = narli.get("req")
    method = req.get("method")
    uri = req.get("uri")
    headers = req.get("headers")
    data = req.get("data")
    if method == "GET":
        response = await requests.get(uri, headers=headers)
        return response
    elif method == "POST":
        response = await requests.post(uri, headers=headers, data=data)
        return response
    elif method == "PUT":
        response = await requests.put(uri, headers=headers, data=data)
        return response
    elif method == "DELETE":
        response = await requests.delete(uri, headers=headers)
        return response
    elif method == "PATCH":
        response = await requests.patch(uri, headers=headers, data=data)
        return response
    elif method == "HEAD":
        response = await requests.head(uri, headers=headers)
        return response
    elif method == "OPTIONS":
        response = await requests.options(uri, headers=headers)
        return response
    else:
        return "Unsupported Protocol/Method;"

def modifyNarli(narli):
    newNarli = narli
    newNarli.get("nodes")[getThisNode(narli=narli)].get("passed") == True
    return newNarli

async def forward(narli):
    nextNode = getNextNode(narli=narli)
    nextNode = narli.get("nodes")[nextNode]
    wsprtcl = nextNode.get("protocol")
    wsuri = nextNode.get("uri")
    wsport = nextNode.get("port")
    wspath = nextNode.get("path")

    async with websockets.connect(f"{wsprtcl}://{wsuri}:{wsport}/{wspath}") as ws:
        await ws.send(ITCryption.encode(modifyNarli(narli)))
        response = await ws.recv()
        return ITCryption.decode(response)