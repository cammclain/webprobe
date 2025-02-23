
import uvloop
from rich.console import Console
async def main() -> None:
    console: Console = Console()
    console.print("Launching webprobe...")



uvloop.run(main())

