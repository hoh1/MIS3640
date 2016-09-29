def move(n,source, bridge, destination):
    if n >= 1:
        move(n-1,source,destination,bridge)
        moveDisk(source,bridge)
        move(n-1,destination,bridge,source)

def moveDisk(source, bridge):
    print("moving disk from",source,"to",bridge)

move(3,"A","B","C")
