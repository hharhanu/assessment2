import json
  f = open('data.json',)
data = json.load(f)
   for i in data['movies_data_details']:
    print(i)
   dictionary ={
    "movie_name" = "pushpa",
    "year_of release" = 2021
    }

with open("movies_data.json", "w") as outfile:
    json.dump(dictionary, outfile)
