destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]
attractions = [[], [], [], [], []]
test_traveler = ['Erin Wilkes', 'Sao Paulo, Brazil', ['historical site', 'art']]
user = ['Dereck Smill', 'Paris, France', ['monument']]

def get_dest_index(dest):
  dest_index = destinations.index(dest)
  return dest_index

def get_trav_location(trvlr):
  trv_destination = trvlr[1]
  return trv_destination

def add_attractions(dest, att):
  index = get_dest_index(dest)
  attractions[index].append(att)

traveler_destination = get_dest_index(get_trav_location(test_traveler))

add_attractions('Los Angeles, USA', ['Venice Beach,', ['beach']])
add_attractions("Paris, France", ["the Louvre", ["art", "museum"]])
add_attractions("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attractions("Shanghai, China", ["Yu Garden", ["garden", "historical site"]])
add_attractions("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attractions("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attractions("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attractions("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attractions("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attractions("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attractions("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(dest, interests):
  possible_attractions = []
  attractions_in_city = attractions[get_dest_index(dest)]
  for att in attractions_in_city:
    attraction_tags = att[1] 
    for ints in interests:
      if ints in attraction_tags:
        possible_attractions.append(att[0])
  return possible_attractions

# Test for attraction logic
# test = find_attractions("Paris, France", ['art', 'monument'])
# print(test)

def get_attractions_for_traveler(traveler):
  traveler_destination = traveler[1]
  traveler_interests = traveler[2] 
  traveler_attractions = find_attractions(traveler_destination, traveler_interests)
  return traveler_attractions

results = get_attractions_for_traveler(user)
interests_string = "Hi " + user[0] + ", we think you'll like these places around " + user[1] + ":"

def return_results():
   print(interests_string)
   for res in results:
    print(res)

return_results()

