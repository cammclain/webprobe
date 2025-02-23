
import os
import sys






class WebProbeApp:

    async def __init__(self):
        # validate all tools are available to the program
        # this includes tools like BBOT, Nuclei, etc.
        # we will basically put all the application integrity checks here
        # oh we will also load the config here. we should probably do that first actually lol