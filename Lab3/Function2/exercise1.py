def rate(x, b):
    for dictionary in movies:
        for key in dictionary:
            if dictionary.get("name", "movie not found") == x:
               if dictionary["imdb"] > b:
                   return True
    return False