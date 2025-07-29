answer = input("I ACCEPT ONLY YES OR NO")

if answer != "YES" and answer !="NO":
    raise ValueError
else:
    print("ISPOLNYAMYJ FAIL")