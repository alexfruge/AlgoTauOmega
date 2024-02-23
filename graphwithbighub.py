import sys

numNodes = sys.argv[1]
f = open(sys.argv[2], "w")
f.write(numNodes+"\n")
f.write(f"1 {int(numNodes) // 2 + 2}\n")
f.write(f"1 {int(numNodes) // 2 + 2}\n")
f.write(f"1 1\n")
for i in range(3, int(numNodes) // 2):
    f.write(f"0\n")
f.write(f"{int(numNodes) // 2} ")
for i in range(1,int(numNodes) // 2+1):
    f.write(f"{i} ")
f.write("\n")
f.write(f"2 3 {int(numNodes) // 2+1}\n")
f.write(f"3 1 2 {int(numNodes) // 2+1}\n")
for i in range(int(numNodes) // 2+2, int(numNodes)-1):
    f.write(f"1 {int(numNodes) // 2+1}")
    if i != int(numNodes)-2:
        f.write(f"\n")
f.close()