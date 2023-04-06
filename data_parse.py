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
            await self.UpdateStatus_SOS(websocket)
            await self.UpdateStatus_CCTV(websocket)
            await self.UpdateStatus_Lighting(websocket)
            await self.UpdateStatus_VRI(websocket)
            await self.UpdateStatus_Barrier(websocket)
            await self.UpdateStatus_MSI(websocket)

    # TODO
    #############
    def Control_SOS(self, id, command):
        return {"id": id, "action": "command", "lfv": "sos", "command": command}
    #############

    # command (string): change_pan change_tilt change_zoom change_preset     id (int): 0 1 2   value (int): number between min and max value
    def Control_CCTV(self, id, command, value):
        return {"id": id ,"action": "command", "lfv": "cctv", "command": command, "new_value": value}

    # command (string): auto 0 1 2 3 4 5 6 7 8 9 19     id (int): 0 1 2 3 4 5 6 
    def Control_Lighting(self, id, command):
        return {"id": id, "action": "command", "lfv": "lights", "command": command}

    # command (string): on off   id (int): 0 1 2 3
    def Control_VRI(self, id, command) :
        return {"id": id, "action": "command", "lfv": "vri", "command" : command}

    # command (string): none down up stop   id: 0 1
    def Control_Barrier(self, id, command):
        return {"id": id, "action": "command", "lfv": "barrriers", "command" : command}

    # command (string): off red_cross green_arrow arrow_left arrow_right end_limitation 50 60 70 80 90 100  id: 0 1
    def Control_MSI(self, id, command):
        return {"id": id ,"action": "command", "lfv": "msi", "command": command}

    # Retrieving Status Commando's

    # server returns a json object for every "SOS"
    # sos_state: array of objects of the form: { ? }
    async def UpdateStatus_SOS(self,ws):
        command = {"action": "status", "lfv": "sos"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.sos_state = [json_obj["data"]]

    # server returns a json object for every camera
    # sos_state: array of objects of the form: {id, pan, tilt, zoom, preset}
    async def UpdateStatus_CCTV(self,ws):
        command = {"action": "status", "lfv": "cctv"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.cctv_state = [json_obj["data"]]

    # server returns a json object for every light
    # lighting_state: array of objects of the form: {id, level, capacity, energy_usage, light_hours}
    async def UpdateStatus_Lighting(self,ws):
        command = {"action": "status", "lfv": "lighting"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.lighting_state = [json_obj["data"]]

    # server returns a json object for every traffic light
    # vri_state: array of objects of the form: {id, available_state, error_state, state}
    async def UpdateStatus_VRI(self,ws):
        command = {"action": "status", "lfv": "vri"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.vri_state = [json_obj["data"]]
        #[d["state"] for d in json_obj["data"]] provides vri_state in the form: [ 'state', 'state', 'state', 'state']

    # server returns a json object for every barrier
    # vri_state: array of objects of the form: {id, state, available_state, movement_state, obstacle_state, error_state}
    async def UpdateStatus_Barrier(self, ws):
        command = {"action": "status", "lfv": "barrier"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.barrier_state = [json_obj["data"]]

    # server returns a json object for every matrix bord
    # vri_state: array of objects of the form: {id, state, available_state, flashing_state, error_state}
    async def UpdateStatus_MSI(self, ws):
        command = {"action": "status", "lfv": "msi"}
        json_string = await self.send_command(ws, command)
        json_obj = json.loads(json_string)
        self.msi_state = [json_obj["data"]]

    # Function to send a command to the receiving server and returns its response
    async def send_command(self, websocket, command):
        await websocket.send(json.dumps(command))
        return await websocket.recv()
