import sys
from multiprocessing import freeze_support

from interfaces.cli import CommandLineInterface
from interfaces.gui import GraphicalUserInterface

from constants.hexCodesReference import AttributesAndRaces, Archetypes
from classes.downloadManager import DownloadManager

from classes.sql import CardsCDB
from classes.lookup import Lookup

# Main function. Runs when main.py is called.
def main():
    freeze_support()

    # Setup
    DownloadManager.DownloadFiles()
    Archetypes.Setup()
    AttributesAndRaces.Setup()
    CardsCDB.Setup()
    Lookup.Setup()
    print("")

    if("--cli" in sys.argv):
        interface = CommandLineInterface()
    else:
        interface = GraphicalUserInterface()
    
    interface.StartInterface()

if __name__ == '__main__':
    main()