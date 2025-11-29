from . import internet
from source.core import IO, log
from source.lib import dialog, helper

# "(http(s)?:\\/\\/)?([a-z0-9]){3,256}\\.([a-z0-9]){2,6}$"
def exec(varsIn):
    IO.say(varsIn)
    internet.HTTPget(varsIn['host'], varsIn['stor'], varsIn['timeout'])


def parse(varsIn, mode=0, req=""):
    IO.say(varsIn)
    if mode == 0:
        if varsIn.__contains__("help"):
            helper.request(varsIn.__getitem__("help"))
        else:
            # add custom syntax or regex checks for each of the command's arguments before passing them, they have only been stripped and lowercased for internal processing ease
            for item in req:
                if not varsIn.__contains__(item):
                    print()
                    dialog.missingArgs(item)

