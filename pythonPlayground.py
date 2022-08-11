def over_nine_thousand(lst):
  count = 0
  for num in lst:
      if count <= 9000:
        count += num
  return count
#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))