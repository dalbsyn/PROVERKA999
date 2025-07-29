answer = input("I ACCEPT ONLY YES OR NO:\n")

if answer != "YES" and answer !="NO":
    raise ValueError("I ACCEPT ONLY YES OR NO")
else:
    print("VSCODE UMEET PODPISYVAT COMMITY?")
    print("ISPOLNYAMYJ FAIL.")