import random
import time
from datetime import datetime
from os import system

from vocabulary import *

startTime = datetime.now()


def clear_output():
    # for windows, use cls command
    # system('cls')

    # for mac and linux, use clear command
    system("clear")


listRevise = {
    "List1": List1,
    "List2": List2,
    "List3": List3,
    "List4": List4,
    "List5": List5,
    "List6": List6,
    "List7": List7,
    "List8": List8,
    "List9": List9,
    "List10": List10,
    "List11": List11,
    "List12": List12,
    "List13": List13,
    "List14": List14,
}
# listRevise={'List1':List1}

listOfList = list(listRevise.keys())

print(
    "Please Enter Number \n1: Serial Revision \n2: Random Revision \n3: Serial Revision With Practise\n4: Random Revision With Practice\n5: List Group Name Revision\n6: Revision Words Only \n7: Random Revision(With Out Time Stamp)\n8: Find Group Using Word"
)
number = int(input())

if number == 1:
    clear_output()
    for x in range(len(listRevise.keys())):
        randomNumberList = x
        listKey1 = list(listRevise[listOfList[randomNumberList]].keys())
        for x in range(0, len(listRevise[listOfList[randomNumberList]].keys())):
            print("From ", listOfList[randomNumberList], "\n")
            time.sleep(0.5)
            print(
                "Total Words in this group is ",
                len(listRevise[listOfList[randomNumberList]][listKey1[x]]),
            )
            time.sleep(3)
            print(
                "("
                + str(listKey1.index(listKey1[x]) + 1)
                + ") "
                + str(listKey1[x])
                + " ("
                + str(len(listRevise[listOfList[randomNumberList]][listKey1[x]]))
                + ")"
            )
            time.sleep(1)
            for y in range(len(listRevise[listOfList[randomNumberList]][listKey1[x]])):
                time.sleep(2)
                print(
                    "  ",
                    "(" + str(y + 1) + ")",
                    listRevise[listOfList[randomNumberList]][listKey1[x]][y],
                )
            time.sleep(5)
            clear_output()
            time.sleep(0.5)
    print("Total time to execute this part is ", datetime.now() - startTime)

if number == 2:
    clear_output()
    for x in range(len(listRevise.keys())):
        randomNumberList = random.randint(0, len(listOfList) - 1)
        listKey1 = list(listRevise[listOfList[randomNumberList]].keys())
        for x in range(len(listRevise[listOfList[randomNumberList]].keys())):
            randomNumber = random.randint(0, len(listKey1) - 1)
            time.sleep(0.5)
            print(
                "Do you know this one ?   "
                + "\t"
                + "From "
                + str(listOfList[randomNumberList])
                + "\n"
                + "--> "
                + str(
                    random.choice(
                        listRevise[listOfList[randomNumberList]][listKey1[randomNumber]]
                    )
                )
            )
            time.sleep(1)
            print(
                "\n",
                "Total Words in this group is ",
                str(
                    len(
                        listRevise[listOfList[randomNumberList]][listKey1[randomNumber]]
                    )
                ),
            )
            # time.sleep(len(listRevise[listOfList[randomNumberList]][listKey1[randomNumber]]))
            time.sleep(1)
            print("\n")
            print(
                str(
                    list(listRevise[listOfList[randomNumberList]].keys()).index(
                        listKey1[randomNumber]
                    )
                    + 1
                )
                + ".",
                listKey1[randomNumber],
                "("
                + str(
                    len(
                        listRevise[listOfList[randomNumberList]][listKey1[randomNumber]]
                    )
                )
                + ")",
            )
            for y in range(
                len(listRevise[listOfList[randomNumberList]][listKey1[randomNumber]])
            ):
                time.sleep(2)
                print(
                    "  ",
                    "(" + str(y + 1) + ")",
                    listRevise[listOfList[randomNumberList]][listKey1[randomNumber]][y],
                )
            time.sleep(2)
            clear_output()
            del listKey1[randomNumber]
        del listOfList[randomNumberList]
    print("Total time to execute this part is ", datetime.now() - startTime)


def wordMatch(user, select):
    return user.upper() == select.upper()


if number == 3:
    clear_output()
    for x in range(len(listRevise.keys())):
        randomNumberList = x
        listKey1 = list(listRevise[listOfList[randomNumberList]].keys())
        initial = 0
        final = int(len(listRevise[listOfList[randomNumberList]].keys()))
        x = 0
        while x < final:
            correct = 0
            incorrect = 0
            print("From ", listOfList[randomNumberList])
            print(str(listKey1.index(listKey1[x]) + 1))
            topic = str(input("Enter Topic Name :  "))
            print(
                "\t\t"
                + "("
                + str(listKey1.index(listKey1[x]) + 1)
                + ") "
                + str(listKey1[x])
                + "  ("
                + str(len(listRevise[listOfList[randomNumberList]][listKey1[x]]))
                + ")"
            )
            print("\n")
            y = 0
            while y < len(listRevise[listOfList[randomNumberList]][listKey1[x]]):
                word = str(input("Enter Name : "))
                if wordMatch(
                    word, listRevise[listOfList[randomNumberList]][listKey1[x]][y]
                ):
                    print("\t     Correct   \u2714")
                    print(
                        "\t",
                        "(" + str(y + 1) + ")",
                        listRevise[listOfList[randomNumberList]][listKey1[x]][y],
                    )
                    print("\n")
                    y = y + 1
                    correct = correct + 1
                else:
                    print("\t     Incorrect    \u274c")
                    print(
                        "\t",
                        "(" + str(y + 1) + ")",
                        listRevise[listOfList[randomNumberList]][listKey1[x]][y],
                    )
                    print("\n")
                    incorrect = incorrect + 1

            print(
                "You have made "
                + str(
                    (
                        incorrect
                        / int(
                            len(listRevise[listOfList[randomNumberList]][listKey1[x]])
                        )
                    )
                    * 100
                )
                + " % mistake..."
            )
            if (
                incorrect / len(listRevise[listOfList[randomNumberList]][listKey1[x]])
            ) >= 0.2:
                print("\nRepeat Again because you make more than 20% mistake")
                x = x
            else:
                print("\nMove to next topic because you make less mistake(below 20%)")
                x = x + 1
            time.sleep(2)
            clear_output()
    print("Total time to execute this part is ", datetime.now() - startTime)

if number == 4:
    clear_output()
    check = 0
    for x in range(len(listRevise.keys())):
        randomNumberList = random.randint(0, len(listOfList) - 1)
        listKey1 = list(listRevise[listOfList[randomNumberList]].keys())
        x = 0
        while x < len(listRevise[listOfList[randomNumberList]].keys()):
            correct = 0
            incorrect = 0
            if check == 0:
                randomNumber = random.randint(0, len(listKey1) - 1)
            print(
                "Do you know this one ?   "
                + "\t"
                + "From "
                + str(listOfList[randomNumberList])
                + "\n"
                + "--> "
                + str(
                    random.choice(
                        listRevise[listOfList[randomNumberList]][listKey1[randomNumber]]
                    )
                )
            )
            print("\n")
            topic = str(input("Enter Topic : "))
            print(
                "\t  ",
                str(
                    list(listRevise[listOfList[randomNumberList]].keys()).index(
                        listKey1[randomNumber]
                    )
                    + 1
                )
                + ".",
                listKey1[randomNumber],
                "("
                + str(
                    len(
                        listRevise[listOfList[randomNumberList]][listKey1[randomNumber]]
                    )
                )
                + ")\n",
            )
            y = 0
            while y < len(
                listRevise[listOfList[randomNumberList]][listKey1[randomNumber]]
            ):
                word = str(input("Enter Name : "))
                if wordMatch(
                    word,
                    listRevise[listOfList[randomNumberList]][listKey1[randomNumber]][y],
                ):
                    print("\t     Correct   \u2714")
                    print(
                        "\t",
                        "(" + str(y + 1) + ")",
                        listRevise[listOfList[randomNumberList]][
                            listKey1[randomNumber]
                        ][y],
                    )
                    print("\n")
                    y = y + 1
                    correct = correct + 1
                else:
                    print("\t     Incorrect    \u274c")
                    print(
                        "\t",
                        "(" + str(y + 1) + ")",
                        listRevise[listOfList[randomNumberList]][
                            listKey1[randomNumber]
                        ][y],
                    )
                    print("\n")
                    incorrect = incorrect + 1
            print(
                "You have made "
                + str(
                    (
                        incorrect
                        / int(
                            len(
                                listRevise[listOfList[randomNumberList]][
                                    listKey1[randomNumber]
                                ]
                            )
                        )
                    )
                    * 100
                )
                + " % mistake..."
            )
            if (
                incorrect
                / len(listRevise[listOfList[randomNumberList]][listKey1[randomNumber]])
            ) >= 0.2:
                print("\nRepeat Again because you make more than 20% mistake")
                x = x
                check = 1
            else:
                print("\nMove to next topic because you make less mistake(below 20%)")
                x = x + 1
                del listKey1[randomNumber]
                check = 0
            time.sleep(2)
            clear_output()
        del listOfList[randomNumberList]
    print("Total time to execute this part is ", datetime.now() - startTime)

if number == 5:
    clear_output()
    for x in range(len(listRevise.keys())):
        randomNumberList = x
        listKey1 = list(listRevise[listOfList[randomNumberList]].keys())
        print(
            "Total Group in ",
            listOfList[randomNumberList],
            " is ",
            len(listRevise[listOfList[randomNumberList]].keys()),
        )
        time.sleep(len(listRevise[listOfList[randomNumberList]].keys()))
        # time.sleep(1)
        clear_output()
        for x in range(0, len(listRevise[listOfList[randomNumberList]].keys())):
            time.sleep(0.5)
            print(
                "From ",
                listOfList[randomNumberList],
                "\t",
                "Group Number :- ",
                listKey1.index(listKey1[x]) + 1,
                "\n",
            )
            time.sleep(1.5)
            print(
                "("
                + str(listKey1.index(listKey1[x]) + 1)
                + ") "
                + str(listKey1[x])
                + " ("
                + str(len(listRevise[listOfList[randomNumberList]][listKey1[x]]))
                + ")"
            )
            time.sleep(5)
            print("\nNext.........")
            time.sleep(5)
            clear_output()
            time.sleep(0.5)
    print("Total time to execute this part is ", datetime.now() - startTime)

if number == 6:
    clear_output()
    for x in range(len(listRevise.keys())):
        randomNumberList = x
        listKey1 = list(listRevise[listOfList[randomNumberList]].keys())
        wordDict = {
            value: x
            for x in listRevise[listOfList[randomNumberList]]
            for value in listRevise[listOfList[randomNumberList]][x]
        }
        listKey2 = list(wordDict.keys())
        for x in range(len(listKey2)):
            time.sleep(0.25)
            randomNumber = random.randint(0, len(listKey2) - 1)
            print("Do you know this word ?\t", "From ", listOfList[randomNumberList])
            print("-->", listKey2[randomNumber])
            time.sleep(2)
            print("\n", wordDict[listKey2[randomNumber]])
            time.sleep(1.5)
            clear_output()
            time.sleep(0.25)
            del listKey2[randomNumber]
    print("Total time to execute this part is ", datetime.now() - startTime)

if number == 7:
    clear_output()
    for x in range(len(listRevise.keys())):
        randomNumberList = random.randint(0, len(listOfList) - 1)
        listKey1 = list(listRevise[listOfList[randomNumberList]].keys())
        print(
            "Do you know this one ?   "
            + "\t"
            + "From "
            + str(listOfList[randomNumberList]),
            "\n",
        )
        for x in range(len(listRevise[listOfList[randomNumberList]].keys())):
            randomNumber = random.randint(0, len(listKey1) - 1)
            print(
                "--> "
                + str(
                    random.choice(
                        listRevise[listOfList[randomNumberList]][listKey1[randomNumber]]
                    )
                ),
                "\n",
            )
            del listKey1[randomNumber]
        del listOfList[randomNumberList]
    print("Total time to execute this part is ", datetime.now() - startTime)


if number == 8:
    clear_output()
    print("Enter Words :\n")
    word = str(input()).lower()
    for x in range(len(listRevise.keys())):
        listKey1 = list(listRevise[listOfList[x]].keys())
        for y in range(len(listRevise[listOfList[x]].keys())):
            data = [
                c.split("(")[0].lower() for c in listRevise[listOfList[x]][listKey1[y]]
            ]
            if word in [
                c.split("(")[0].lower() for c in listRevise[listOfList[x]][listKey1[y]]
            ]:
                print(
                    "\nGroup Name :("
                    + str(list(listRevise[listOfList[x]].keys()).index(listKey1[y]) + 1)
                    + ")",
                    listKey1[y],
                )
                print(
                    "List Name  :",
                    list(listRevise.keys())[x],
                    "(" + str(len(listRevise[listOfList[x]][listKey1[y]])) + ")",
                    "\n",
                )
                print(*listRevise[listOfList[x]][listKey1[y]], sep="\n")
