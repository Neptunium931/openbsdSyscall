#!/usr/bin/env python3

import re


def getType(splitLine: list[str]) -> str:
    r = []
    if splitLine[1] == "STD":
        for t in splitLine[1:]:
            if t == "{":
                break
            r.append(t)
        return " ".join(r)
    return splitLine[1]


def getReturn(splitLine):
    i = 0
    while splitLine[i] != "{":
        i += 1
        if i == len(splitLine):
            return ""
    return splitLine[i + 1]


def joinLine(lines, i):
    line = lines[i]
    while "\\" in lines[i - 1]:
        line = lines[i - 1] + line
        i = i - 1
    return line.replace("\\\n", " ")


def getArgs(line):
    pattern = re.compile(r"\(((.*),?)\)")
    matches = pattern.findall(line)
    if matches == []:
        return matches
    return matches[0][0].replace("(", "").replace(")", "").split(",")


def getName(splitLine):
    i = 0
    while "(" not in splitLine[i]:
        i += 1
        if i == len(splitLine):
            return splitLine[-1].strip()
    pattern = re.compile(r".*\(")
    matches = pattern.findall(splitLine[i])
    return matches[0].replace("(", "").replace("*", "")


with open("./syscalls.master") as f:
    lines = f.readlines()

tab = []
for i in range(len(lines)):
    line = lines[i]
    if line[0] == ";" or line[0] == "#":
        continue
    if line == "\n":
        continue
    if line[-2] == "\\":
        continue
    line = joinLine(lines, i)
    line = line.replace("\t", " ")
    while "  " in line:
        line = line.replace("  ", " ")
    splitLine = line.split(" ")
    dic = {"id": splitLine[0], "rax": hex(int(splitLine[0]))}
    dic["type"] = getType(splitLine)
    dic["return"] = getReturn(splitLine)
    dic["args"] = getArgs(line)
    dic["name"] = getName(splitLine)
    tab.append(dic)
    # print(line.strip().encode())

print(
    "| NR | SYSCALL NAME | RAX | ARG0 (rdi) | ARG1 (rsi) | ARG2 (rdx) | ARG3 (rcx) | ARG4 (r8) | ARG5 (r9)"
)
print(
    "| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |"
)
for dic in tab:
    print(f"|{dic['id']}|{dic['name']}|{dic['rax']}|", end="")
    for i in range(6):
        if i < len(dic["args"]):
            print(f"{dic['args'][i]}", end="|")
        else:
            print("-", end="|")
    print("")
