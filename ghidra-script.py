# Lee Chun Hao
# https://github.com/0x4F776C/drcov-to-ghidra

from java.awt import Color
from ghidra.util.task import ConsoleTaskMonitor
from ghidra.program.model.block import BasicBlockModel
from docking.options.editor import GhidraColorChooser

# Find function via address (color coded)------------------------------------------------
def Main():
    BB_File = askFile("Select BB file to use", "Select")
    BB_File = str(BB_File)
    _color = Color(0xcc, 0xff, 0xcc)
    color = GhidraColorChooser.showDialog(None, "Choose a Color", _color)

    print(color)

    if color is None:
        color = _color

    BB_Addresses = []

    with open(BB_File, "r") as f:
        for line in f:
            try:
                address = int(line.strip(), 16)
                BB_Addresses.append(address)
            except ValueError:
                continue

    Color_BB(BB_Addresses, color)
    Count_Total()
    Count_Ran(BB_Addresses)

def Color_BB(BB_Addresses_List, color):
    BlockModel = BasicBlockModel(currentProgram)
    Monitor = ConsoleTaskMonitor()

    for addresses in BB_Addresses_List:
        addresses_obj = toAddr(addresses)

        if addresses is None:
            print("Invalid address: {}", addresses)
            continue

        BasicBlock = BlockModel.getCodeBlockAt(addresses_obj, Monitor)

        if BasicBlock is None:
            # Can log here
            #print("Basic block does not exist in address: {:#018x}".format(addr))
            continue
        setBackgroundColor(BasicBlock, color)
# ---------------------------------------------------------------------------------------

# Count total number of function---------------------------------------------------------
def Count_Total():
    fm = currentProgram.getFunctionManager()
    funcs = fm.getFunctions(True) # True means 'forward'
    
    funcList = []

    for func in funcs:
        funcList.append(func)

    print("Number of function in total: {count}".format(count = len(funcList)))
# ---------------------------------------------------------------------------------------

# Count total number of function ran-----------------------------------------------------
def Count_Ran(BB_Addresses_List):
    funcList = []
    
    for addresses in BB_Addresses_List:
        funcList.append(addresses)

        if addresses is None:
            # Can log here
            #print("Invalid address: {}", addresses)
            continue

    print("Number of function ran: {count}".format(count = len(funcList)))
# ---------------------------------------------------------------------------------------
    
Main()
