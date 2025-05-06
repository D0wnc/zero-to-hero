input_String = input("Input a strings: ")


if __name__ == "__main__":
    print("Convert to lower ...: " + input_String.lower())
    print("Capitalize..." + input_String.capitalize())
    print("Titel conversion.." + input_String.title())
    print("--------------------------------------------------------------------------")
    proof = "X" + input_String.strip() + "X"
    print("strip..." +  input_String.strip() + " Proof:" + proof)
    print("left.." + input_String.lstrip())
    print("right.." +  input_String.rstrip())
    print("--------------------------------------------------------------------------")