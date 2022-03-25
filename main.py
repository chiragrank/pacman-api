import socketio
import uvicorn
from fastapi import FastAPI
from rich.console import Console

console = Console()
app = FastAPI()
sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*",
    ping_interval=ping_freq,
    ping_timeout=ping_wait
    # async_handlers=True
)

socket_app = socketio.ASGIApp(sio)
app.mount("/", socket_app)


@sio.on("player_move")
async def player_movement_handler(sid, message):
    console.print(message, sid, style="bold blue")
    await sio.emit("player_move_success", message)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000)
