if __name__=="__main__":
    print("here we go over sets and what they are: ")

    tuple_values = (1,1,1,1,2,3,4,6,7,7)
    set_values = set(tuple_values)

    print(tuple_values)
    print(set_values)
    print("as you can see the values from the tuple get sorted out because there are not all unique")


    set_values_b = {1,5,6,8}
    print()
    print(set_values)
    print(set_values_b)
    print( set_values & set_values_b ) #prints out the duplicate values between the two sets
    print( set_values | set_values_b ) #prints out the combined unique values
    print(set_values - set_values_b ) #prints the difference from set 1 to set 2
    print( set_values ^ set_values_b ) #prints out differences from both sets


    print(dir(set))