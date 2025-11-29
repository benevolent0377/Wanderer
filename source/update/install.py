from source.update import Ucore as core

def main(recursion):
    if recursion == 2:
        core.selfUpdate()

    elif recursion < 2:

        core.get()
    if recursion == 0:
        return 0
    
    recursion -= 1
    main(recursion)


if __name__ == "__main__":
    main(2)