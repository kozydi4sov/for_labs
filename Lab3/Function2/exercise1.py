def rate(x, num):
    for dictionary in movies:
        for key in dictionary:
            if dictionary.get("name", "movie not found") == x:
               if dictionary["imdb"] > num:
                   return True
    return False