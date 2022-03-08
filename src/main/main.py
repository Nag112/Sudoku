import os
import sys
import json
from src.generators import Generators as Gen
from src.ratingSudos import rating as RT

def gen_save(num, sym, destination):
    num1 = 0
    num2 = 0
    num3 = 0
    num4 = 0
    num5 = 0
    result = []
    if (sym):
        for i in range(num):
            b, s, lvl = Gen.GenerateString(0, 0, i % 11+1)
            result.append(
                {
                    "id": i+1,
                    "board": b,
                    "solution": s,
                    "rating": lvl
                })
            if (lvl == 1):
                num1 = num1+1
            elif (lvl == 2):
                num2 = num2+1
            elif (lvl == 3):
                num3 = num3+1
            elif (lvl == 4):
                num4 = num4+1
            else:
                num5 = num5+1
            print(i+1, lvl)
    else:
        for i in range(num):
            # 22 to 32 knokn cells
            b, s, lvl = Gen.GenerateString(22, 32, 0)
            result.append(
                {
                    "id": i+1,
                    "board": b,
                    "solution": s,
                    "rating": lvl
                })
            if (lvl == 1):
                num1 = num1+1
            elif (lvl == 2):
                num2 = num2+1
            elif (lvl == 3):
                num3 = num3+1
            elif (lvl == 4):
                num4 = num4+1
            else:
                num5 = num5+1
            print(i+1, lvl)
    print(" ")

    with open("sudoku.json", "r+") as outfile:
        data = json.load(outfile)
        for i in range(len(result)):
            result[i]["id"] = data[-1]["id"]+1
            data.append(result[i])
        outfile.seek(0)
        json.dump(data, outfile, indent = 4)
    print(num1, "very Easy, ", num2, "Easy, ", num3, "Medium, ",
          num4, "Hard & ", num5, "Very Hard boards generated.")

path = os.path.dirname(os.path.abspath("."))
num = int(sys.argv[-2])
answ = sys.argv[-1]
answ = int(answ)
if (answ == 1 or answ == None):
    destination = path[0:len(path)-3]+"SudoProblems/Symmetrical/"
    gen_save(num, True, destination)
elif(answ == 2):
    destination = path[0:len(path)-3]+"SudoProblems/NonSymmetrical/"
    gen_save(num, False, destination)
else:
    print("Wrong input!")
