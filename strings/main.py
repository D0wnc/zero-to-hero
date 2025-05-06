input_String = input("Input a strings: ")


if __name__ == "__main__":


    if input_String.isdigit():
        print("its a number")

        print("fill with leading zero's" + input_String.zfill(8))
    else:
        if input_String.islower():
            print("Capitalize..." + input_String.upper())
        if input_String.isupper():
            print("Convert to lower ...: " + input_String.lower())

        print("Titel conversion.." + input_String.title())
        print("reverse case:" + input_String.swapcase())
        print("--------------------------------------------------------------------------")
        proof = "X" + input_String.strip() + "X"
        print("strip..." +  input_String.strip() + " Proof:" + proof)
        print("left.." + input_String.lstrip())
        print("right.." +  input_String.rstrip())
        print("--------------------------------------------------------------------------")
        print("Justify content left and fill with dots:" + input_String.ljust(10, "."))
        print("do the same on the right:" +  input_String.rjust(10, "."))
        print("--------------------------------------------------------------------------")
        print("now we are replacing.. hello:" + input_String.replace("Hello", "Ciao"))
        print("--------------------------------------------------------------------------")
        print("now we are counting for 'l' occurences:" +  str(input_String.count("l")))
        print("--------------------------------------------------------------------------")
        list_with_strings = input_String.split(",")
        for line in list_with_strings:
            print("Loop: .... " +  line.strip())
        print("--------------------------------------------------------------------------")
        #u can also choose words where strings getting splitted at
        partioned_list = input_String.partition(",")
        for line in list_with_strings:
            print("Partioned value: .. " + line.strip())

        print("--------------------------------------------------------------------------")
        print("now we put partioned_list back together")
        seperator = ""
        print(seperator.join(partioned_list))
        print("--------------------------------------------------------------------------")