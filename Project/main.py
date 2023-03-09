import asyncio
import websockets
import ITCryption
import narlinet

async def handler(websocket, path):
    class response:
        class res:
            headers = ""
            body = ""

    encData = await websocket.recv()
    data = ITCryption.decode(encData)
    if narlinet.amILastNode(narli=data):
        response = await narlinet.iAmLastNode(narli=data)
    else:
        response = await narlinet.forward(narli=data)

    print(response)
    await websocket.send(ITCryption.encode(response))

start_server = websockets.serve(handler, "localhost", 4900)
print("Server Is Running On Port 4900;")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()