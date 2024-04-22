from . import IO
from . import system
# a file to parse all commands

def parse(values):
    cmdList = IO.yamlRead(f'{system.getConfigPath()}parent.yaml', 'cmdList')

    for argument in values:
