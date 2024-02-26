import sys

numHubs = int(sys.argv[1])
numNodesInRow = int(sys.argv[2])
f = open(sys.argv[3], "w")
f.write(f"{numHubs * (numNodesInRow+1)}\n")
f.write("0\n")
for currHub in range(1,numHubs+1):
    hubNum = (currHub-1)*(numNodesInRow+1)+1
    if hubNum != 1:
        prereqsOfHub = [x for x in range(hubNum - numNodesInRow, hubNum)]
        f.write(f"{hubNum}")
        for prereq in prereqsOfHub:
            f.write(f" {prereq}")
        f.write("\n")
    for currNodeInRow in range(numNodesInRow):
        if currNodeInRow == 0:
            f.write(f"2 {hubNum} {hubNum + 2}\n")
        elif currNodeInRow == numNodesInRow - 1:
            f.write(f"2 {hubNum} {hubNum+numNodesInRow-1}\n")
        else:
            f.write(f"3 {hubNum} {currNodeInRow + hubNum} {currNodeInRow + hubNum + 2 }\n")