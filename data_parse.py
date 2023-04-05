import asyncio
import json
import websockets

class DataParser:
    
    def __init__(self):
        self.sos_state = []
        self.cctv_state = []
        self.lighting_state = []
        self.vri_state = []
        self.barrier_state = []
        self.msi_state = []
        asyncio.run(self.UpdateAllStatusses())

    async def UpdateAllStatusses(self):
        async with websockets.connect("ws://213.93.142.164:8080") as websocket:
            await self.GetStatus_SOS(websocket)
            await self.GetStatus_CCTV(websocket)
            await self.GetStatus_Lighting(websocket)
            await self.GetStatus_VRI(websocket)
            await self.GetStatus_Barrier(websocket)
            await self.GetStatus_MSI(websocket)

    def Control_SOS(self):
        return 0

    # parameter definitions
    def Control_CCTV(self):
        return 0

    # parameter definitions
    def Control_Lighting(self):
        return 0

    # command: on off   id: 0 1 2 3
    def Control_VRI(self,command, id) :
        return {"action": "command", "lfv": "vri", "command" : command, "id": id}


    # parameter definitions
    def Control_Barrier(self):
        return 0

    # parameter definitions
    def Control_MSI(self):
        return 0

    # Retrieving Status commando in the form: lfv
    async def GetStatus_SOS(self,ws):
        command = {"action": "status", "lfv": "sos"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.sos_state #= [d["state"] for d in json_obj["data"]]


    async def GetStatus_CCTV(self,ws):
        command = {"action": "status", "lfv": "cctv"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.cctv_state #= [d["state"] for d in json_obj["data"]]

    async def GetStatus_Lighting(self,ws):
        command = {"action": "status", "lfv": "lighting"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.lighting_state #= [d["state"] for d in json_obj["data"]]


    async def GetStatus_VRI(self,ws):
        command = {"action": "status", "lfv": "vri"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        print(json_obj)
        self.vri_state = [d["state"] for d in json_obj["data"]]


    async def GetStatus_Barrier(self, ws):
        command = {"action": "status", "lfv": "barrier"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.barrier_state #= [d["state"] for d in json_obj["data"]]

    async def GetStatus_MSI(self, ws):
        command = {"action": "status", "lfv": "msi"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.msi_state #= [d["state"] for d in json_obj["data"]]


    async def send_command(self, websocket, command):
        await websocket.send(json.dumps(command))
        return await websocket.recv()
        


