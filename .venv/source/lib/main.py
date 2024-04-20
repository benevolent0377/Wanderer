
# imports
from . import IO
from . import setup
import sys

def run():

    setup.run()

    if len(sys.argv) < 2:
        yes = IO.say(["what is your name", "what is your dob?", "how are you feeling today"], True, True, True, "internal")
        IO.say(yes, isLoop=True)

    else:

        yes = IO.say("what is your fav color ", True, syntaxChk=True, synType="internal")
        IO.say(yes)

