from pylive import live_plotter, live_bar
from pprint import pprint as pp
import numpy as np
import asyncio
import websockets
import json

WHITE_MIN = 900
size = 100
x_vec = np.linspace(0, 1, size + 1)[0:-1]
y_mat = [np.zeros(size)] * 5
lines = [-1]*5
ax = -1
data = []


async def ir_bar_graph(websocket):
    global  ax
    async for message in websocket:
        raw_data = json.loads(message)["IR"]
        ax = live_bar(raw_data, ax)  
        
async def raw_telemetry(websocket):
    global size, x_vec, y_mat, lines
    async for message in websocket:
        print("Got dadta")
        data = json.loads(message)["IR"]
        for i, (y_vec, datum )in enumerate(zip(y_mat, data)):
            y_mat[i][-1] = datum
        lines = live_plotter(x_vec, y_mat, lines, title="IR Sensor Values", pause_time=0.01)
        for i, y_vec in enumerate(y_mat):
            y_mat[i] = np.append(y_vec[1:], 0.0)



async def main():
    async with websockets.serve(raw_telemetry, "192.168.126.139", 6969):
        print("Running websocket server")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
