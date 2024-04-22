import random
import string
from . import log
# a file for misc commands
def keyGen(length=16, seed=hash(random)):

    seed = seed.__str__()
    key = ''.join(random.choices(string.ascii_uppercase + string.digits + seed, k=length))
    log.log("", "rand")
    return key
