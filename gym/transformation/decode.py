flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥ㄴㅡて㝽"

# ord(flag[i] << 8) + ord(flag[i + 1]) = ord(nFlag[i])
# ord(nFlag[i]) = ord(flag[i] << 8) + ord(flag[i + 1])

res = ""

for char in flag:
    first_char = chr(ord(char) >> 8)
    second_char = chr(ord(char) - (ord(first_char) << 8))
    res += first_char + second_char

print(res)
