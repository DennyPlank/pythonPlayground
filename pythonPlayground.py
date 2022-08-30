highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
titles = []
poets = []
dates = []
highlighted_poems_details = []
highlighted_poems_stripped = []


highlighted_poems_list = highlighted_poems.split(",")
for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())

for poem in highlighted_poems_stripped:
   highlighted_poems_details.append(poem.split(':'))
for x in highlighted_poems_details:
  titles.append(x[0])
  poets.append(x[1])
  dates.append(x[2])
print(titles)
index = 0
for poem in highlighted_poems_details:
  print("The poem {} was published by {} in {}".format(titles[index], poets[index], dates[index]))
  index += 1