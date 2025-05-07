

if __name__ == "__main__":
 name = ["Mario", "Olivia", "Marc"]
 print("----------------------------------------------")
 print(name)
 print("print only Mario... -> " + name[0])
 print("print marc but reverse -> " + name[-1])

 print("----------------------------------------------")
 name[0] = "Wario"
 print("Now we released Mario with another cool name: -> " + name[0])

 print("----------------------------------------------")
 new_names = ["luigi", "Bowser"]
 name += new_names
 print("New names were appended to the list via += operator")
 print(name)

 print("----------------------------------------------")
 name.append("Toad")
 print("with append method u can also add net entries, as I did with Toad-> " + name[-1])
 print("as you can see, you can also add an entry at a specific location with insert")
 name.insert(1, "Toad_via_insert")
 print(name[1])

 print("----------------------------------------------")
 print("with del keyword, u can delete the unused list")
 del(new_names)
 
 print("----------------------------------------------")
 print("delete specific entries with del")
 del name[1] #deletes our Toad_via_insert
 name.pop()#deletes our last entry but also u can receive it into a variable
 name.remove("Wario")#or you can delete via the value
 print(name)

 print("----------------------------------------------")
 sorted_list = sorted(name)
 print("sorted list: ")
 print(sorted_list)
 sorted_list = sorted(sorted_list, reverse=True)
 print(sorted_list)
 sorted_list = sorted(sorted_list, key=str.lower)#ignoriert Großschreibung
 print(sorted_list)


 
