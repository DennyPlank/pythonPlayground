def over_nine_thousand(lst1):
  i = 0
  count = 0
  while count <= 9000:
    count += lst1[i] 
    i += 1
  return count
#Uncomment the line below when your function is done
print(over_nine_thousand([9000, 900, 120, 5000]))