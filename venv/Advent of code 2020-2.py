passwords = [[14, 15, "d", "dzjgbdwdkdhdddh"], [1, 3, "a", "aabc"], [2, 4, "b", "abcd"]]
print(passwords)
result = 0
for password in passwords: #każdy element np: [1, 3, "a", "aabc"]
    count = password[3].count(password[2])
    if password[0] <= count <= password[1]:
        result += 1
print(result)


