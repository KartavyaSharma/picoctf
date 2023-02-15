chars = []
with open('out.txt', 'r') as inFile:
    chars = [chr(int(line.strip())) for line in inFile]

print("".join(chars))
