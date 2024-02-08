def avecat(x, y):
    sum = float(0)
    for dictionary in movies:
        for key in dictionary:
            if dictionary.get("category", 'category not exist' ) == x:
                sum += dictionary["imdb"]
    return sum / len(y)
    
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
while True:
    print('write number from 1 to 5')
    x = int(input())
    if x == '/n':
        break
    else:
       if x == 1:
          print('print the rate')
          num = float(input())
          print('choose movies name if you want know that imdb above ', num, ' or not')
          name = input()
          print(rate(name, num))
       elif x == 2:
          print('choose above which imdb movies you want to find')
          rang = float(input())
          sublist(rang)
       elif x == 3:
          print('choose a category you intresting')
          cat = input()
          category(cat)
       elif x == 4:
          print(average(movies))
       else:
          print('choose category to see average imdb')
          moviecategory = input()
          print(avecat(moviecategory, movies))
       print('if you want to know anything else , please write number from 1 to 5')