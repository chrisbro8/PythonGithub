for i in range(3):
    print("---> Outer loop:",i)
    for j in range(end+4):
        print("---> inner loop:",j)
    print("Out of Inner loop back to Outer loop")
print('completety Out')