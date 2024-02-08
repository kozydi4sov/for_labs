def category(x):
    for dictionary in movies:
        for key in dictionary:
            if dictionary["category"] == x:
                print(dictionary["name"])
                break
