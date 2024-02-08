def average(x):
    sum = float(0)
    for dictionary in movies:
        for key in dictionary:
            sum += dictionary["imdb"]
    return sum / (len(x) * 3)