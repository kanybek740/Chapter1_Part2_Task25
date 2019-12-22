stroka = 'python lang is the most powerfull and lkjlkjlkjsd'
liststroka = stroka.split()
longest = 0
for i in range(1, len(liststroka)):
    if len(liststroka[longest]) < len(liststroka[i]):
        longest = i
print(liststroka[longest])
