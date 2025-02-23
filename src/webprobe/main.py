from __future__ import annotations
import asyncio
import uvloop
from rich.console import Console
import typer


asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app: typer.Typer = typer.Typer()

@app.command()
async def scan(
    target_site: str = typer.Argument(..., help="Target site to scan"),

) -> None:
    console: Console = Console()
    console.print("Launching webprobe...")
    

if __name__ == "__main__":
    uvloop.run(app())

