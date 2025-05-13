if __name__ == "__main__":

    start = 1
    while start <= 10:
        print(str(start))
        start += 1
    
    print()
    list = ["entry1", "entry2", "entry3"]
    for line in list:
        print(line)

    print()
    dic = {"liste": list}
    for line in dic["liste"]:
        print("loop list from a dic: " + line)