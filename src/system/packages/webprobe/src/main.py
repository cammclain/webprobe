from __future__ import annotations
import asyncio
import uvloop
from rich.console import Console
import typer


from webprobe.application.app import WebProbeApp

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app: typer.Typer = typer.Typer()

@app.command()
async def scan(
    target_site: str = typer.Argument(..., help="Target site to scan"),
) -> None:
   webprobe_app: WebProbeApp = WebProbeApp()
   webprobe_app.console.print("Web Probe App started")
   webprobe_app.console.print(f"Scanning {target_site}...")
   # Add your scanning logic here 


if __name__ == "__main__":
    uvloop.run(app())

