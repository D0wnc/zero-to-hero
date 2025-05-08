if __name__ == "__main__":
    print("it makes a difference how you write out ur tupels with only one entry see:")
    print(type(("Test",)))
    print(type(("string")))

    tupel = ("unchangeable1", "unchangeable2", "unchangeable3")
    print(tupel[0])
    print(tupel[0:2])

    print(dir(tupel))

    print(tupel[tupel.index("unchangeable1")])