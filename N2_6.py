import uvicorn
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
app = FastAPI()
# Простой HTML для тестирования чата
file = open('templates/chat.html', 'r')
html = file.read()
@app.get("/")
async def get():
    return HTMLResponse(html)
@app.websocket("/chat_ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Пользователь сказал: {data}")