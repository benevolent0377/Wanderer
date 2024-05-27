from . import internet
from source.core import IO, log

def main(varsIn):
    internet.HTTPget(varsIn('host'), varsIn('stor'), varsIn('timeout'))
