from . import internet
from source.core import IO, log, helper


def exec(varsIn):
    IO.say(varsIn)
    internet.HTTPget(varsIn['host'], varsIn['stor'], varsIn['timeout'])

def parse(varsIn):
    IO.say(varsIn)
    if varsIn.__contains__("help"):
        helper.request(varsIn.__getitem__("help"))
    else:
        # add custom syntax or regex checks for each of the command's arguments before passing them, they have only been stripped and lowercased for internal processing ease
        for item in req:
            if not varsIn.__contains__(item):
                print()
                # dialog.missingArgs(item)