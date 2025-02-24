
import os
import sys

from rich.console import Console
from webprobe.application.configs.config import Settings



class WebProbeApp:

    async def __init__(self):
        # validate all tools are available to the program
        # this includes tools like BBOT, Nuclei, etc.
        # we will basically put all the application integrity checks here
        # oh we will also load the config here. we should probably do that first actually lol
        console: Console = Console()
        console.print("Loading configuration...")
        self.settings = Settings()
        
        ### self.check_tools()


    async def first_recon_phase(self, target_site: str) -> None:
        # this will be the first phase of the recon
        # we will use tools like subfinder, assetfinder, etc.
        pass