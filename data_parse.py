import asyncio
import json
import websockets

# Global State Variables
SOS_Status = []
CCTV_Status = []
Lighting_Status = []
VRI_Status = []
Barrier_Status = []
MSI_Status = []

# Send Request Command defitions in the form: Control_lfv

# parameter definitions
def Control_SOS():
    return 0


# parameter definitions
def Control_CCTV():
    return 0


# parameter definitions
def Control_Lighting():
    return 0
    

# command: on off   id: 0 1 2 3
def Control_VRI(command, id) :
    return {"action": "command", "lfv": "vri", "command" : command, "id": id}


# parameter definitions
def Control_Barrier():
    return 0

# parameter definitions
def Control_MSI():
    return 0


# Retrieving Status commando in the form: lfv
async def GetStatus_SOS(ws):
    command = {"action": "status", "lfv": "sos"}
    json_string = await send_command(ws, command)
    json_obj = json.loads(json_string)
    global SOS_Status
    #TODO


async def GetStatus_CCTV(ws):
    command = {"action": "status", "lfv": "cctv"}
    json_string = await send_command(ws, command)
    json_obj = json.loads(json_string)
    global CCTV_Status
    #TODO

async def GetStatus_Lighting(ws):
    command = {"action": "status", "lfv": "lighting"}
    json_string = await send_command(ws, command)
    json_obj = json.loads(json_string)
    global Lighting_Status
    #TODO


async def GetStatus_VRI(ws):
    command = {"action": "status", "lfv": "vri"}
    json_string = await send_command(ws, command)
    json_obj = json.loads(json_string)
    global VRI_Status 
    VRI_Status = [d["state"] for d in json_obj["data"]]

async def GetStatus_Barrier(ws):
    command = {"action": "status", "lfv": "barrier"}
    json_string = await send_command(ws, command)
    json_obj = json.loads(json_string)
    global Barrier_Status
    #TODO

async def GetStatus_MSI(ws):
    command = {"action": "status", "lfv": "msi"}
    json_string = await send_command(ws, command)
    json_obj = json.loads(json_string)
    global MSI_Status
    #TODO


async def send_command(websocket, command):
    await websocket.send(json.dumps(command))
    return await websocket.recv()


async def UpdateAllStatusses():
    async with websockets.connect("ws://213.93.142.164:8080") as websocket:
        await GetStatus_SOS(websocket)
        await GetStatus_CCTV(websocket)
        await GetStatus_Lighting(websocket)
        await GetStatus_VRI(websocket)
        await GetStatus_Barrier(websocket)
        await GetStatus_MSI(websocket)
        

if __name__ == "__main__":
    asyncio.run(UpdateAllStatusses())
