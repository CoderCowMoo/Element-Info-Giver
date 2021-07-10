import json
import sys
from colorama import Fore
from colorama import init
init()
def parse():
    jsonElementsFile = open(r"C:\Users\ALS0003\Documents\Coding\Resources\periodic_table.json", 'r', encoding='utf-8')
    parse.jsonElements = json.loads(jsonElementsFile.read())
    pass
def parseElementInfo(element):
    parseElementInfo.ElementInfo = parse.jsonElements[element] # Grab the info about the string of the element inputted.
    pass
if __name__ == "__main__":
    element = str(sys.argv[1])
    parse()
    parseElementInfo(element.lower())
    for i in parseElementInfo.ElementInfo:
        print( Fore.RED + str(i).capitalize() + ': ' + Fore.RESET + str(parseElementInfo.ElementInfo[i]))