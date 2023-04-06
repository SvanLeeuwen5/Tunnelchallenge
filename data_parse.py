import asyncio
import json
import websockets

class DataParser:
    
    def __init__(self):
        self.ipaddress = "ws://213.93.142.164:8080"
        #self.ipaddress = "ws://128.64.32.35:8081"
        self.websocket = None
        self.sos_state = []
        self.cctv_state = []
        self.lighting_state = []
        self.vri_state = []
        self.barrier_state = []
        self.msi_state = []
        asyncio.run(self.UpdateAllStatusses())

    async def UpdateAllStatusses(self):
        self.websocket = await websockets.connect(self.ipaddress)
        await self.UpdateStatus_SOS()
        await self.UpdateStatus_CCTV()
        await self.UpdateStatus_Lighting()
        await self.UpdateStatus_VRI()
        await self.UpdateStatus_Barrier()
        await self.UpdateStatus_MSI()

    # TODO
    #############
    async def Control_SOS(self, id, command):
        control_command = {"id": id, "action": "command", "lfv": "sos", "command": command}
        return self.ResponseIsSuccesful(await self.send_command(control_command))
    #############

    # command (string): change_pan change_tilt change_zoom change_preset     id (int): 0 1 2   value (int): number between min and max value
    async def Control_CCTV(self, id, command, value):
        control_command = {"id": id ,"action": "command", "lfv": "cctv", "command": command, "new_value": value}
        return self.ResponseIsSuccesful(await self.send_command(control_command))

    # command (string): auto 0 1 2 3 4 5 6 7 8 9 19     id (int): 0 1 2 3 4 5 6 
    async def Control_Lighting(self, id, command):
        control_command = {"id": id, "action": "command", "lfv": "lights", "command": command}
        return self.ResponseIsSuccesful(await self.send_command(control_command))

    # command (string): on off   id (int): 0 1 2 3
    async def Control_VRI(self, id, command) :
        control_command = {"id": id, "action": "command", "lfv": "vri", "command" : command}
        return self.ResponseIsSuccesful(await self.send_command(control_command))

    # command (string): none down up stop   id (int): 0 1
    async def Control_Barrier(self, id, command):
        control_command = {"id": id, "action": "command", "lfv": "barriers", "command": command}
        return self.ResponseIsSuccesful(await self.send_command(control_command))

    # command (string): off red_cross green_arrow arrow_left arrow_right end_limitation 50 60 70 80 90 100  id (int): 0 1
    async def Control_MSI(self, id, command):
        control_command = {"id": id ,"action": "command", "lfv": "msi", "command": command}
        return self.ResponseIsSuccesful(await self.send_command(control_command))

    # Retrieving Status Commando's

    # server returns a json object for every "SOS"
    # sos_state: array of objects of the form: { ? }
    async def UpdateStatus_SOS(self):
        command = {"action": "status", "lfv": "sos"}
        self.sos_state = [await self.send_command(command)["data"]]

    # server returns a json object for every camera
    # sos_state: array of objects of the form: {id, pan, tilt, zoom, preset}
    async def UpdateStatus_CCTV(self):
        command = {"action": "status", "lfv": "cctv"}
        self.cctv_state = [await self.send_command(command)["data"]]

    # server returns a json object for every light
    # lighting_state: array of objects of the form: {id, level, capacity, energy_usage, light_hours}
    async def UpdateStatus_Lighting(self):
        command = {"action": "status", "lfv": "lighting"}
        self.lighting_state = [await self.send_command(command)["data"]]

    # server returns a json object for every traffic light
    # vri_state: array of objects of the form: {id, available_state, error_state, state}
    async def UpdateStatus_VRI(self):
        command = {"action": "status", "lfv": "vri"}
        self.vri_state = [await self.send_command(command)["data"]]
        #[d["state"] for d in json_obj["data"]] provides vri_state in the form: [ 'state', 'state', 'state', 'state']

    # server returns a json object for every barrier
    # barrier_state: array of objects of the form: {id, state, available_state, movement_state, obstacle_state, error_state}
    async def UpdateStatus_Barrier(self):
        command = {"action": "status", "lfv": "barrier"}
        self.barrier_state = [await self.send_command(command)["data"]]

    # server returns a json object for every matrix bord
    # msi_state: array of objects of the form: {id, state, available_state, flashing_state, error_state}
    async def UpdateStatus_MSI(self):
        command = {"action": "status", "lfv": "msi"}
        self.msi_state = [await self.send_command(command)["data"]]       

    # function that executes a given command and returns the response
    async def send_command(self, command):
        await self.websocket.send(json.dumps(command))
        json_string = await self.websocket.recv()
        return json.loads(json_string)
    
    # return true when response status code equals 'success'
    def ResponseIsSuccesful(self, response):
        return (response.get("status") == "success")



# Testcode below

#c = DataParser()
#c.Control_Barrier(0, "down")
#print(c.barrier_state)
# c = DataParser()
# response = { "status": "success", "data": {"message": "Command sent."}}
# message = response["data"]["message"]
# print(message)
# print(c.ResponseIsSuccesful(response))