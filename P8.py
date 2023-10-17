#EX:3
val1 = int(input("Enter Amount:"))
val2 = int(input("Enter Amount:"))
if val1>val2:
    greater=val1
    smaller=val2
    print("greater is:",val1)
    print("smaller is:",val2)
else:
    greater=val2
    smaller=val1
    print("greater is:",val2)
    print("smaller is:",val1)