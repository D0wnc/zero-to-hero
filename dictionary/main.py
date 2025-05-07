if __name__ == "__main__":
 myDict = {"age": 20, "name": "dummy"}
 print(myDict["age"])


 print("delete entry wit del")
 del myDict["age"]
 print("without giving a key and only the dic, the whole dic is getting deleted")
 del myDict


 dic = {"one":1, "two":2, "three":3}
 print(dic)
 test = dir(dict)
 print("here is a list of the different methods that a dic contains")
 print(test)

 print(dic.values())
 print(dic.keys())

 print("clear cleares the dic, without deleting it entirely")
 copy_dic = dic.copy()
 dic.clear()