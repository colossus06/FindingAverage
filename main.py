
# Here's how you can find the average of a set of numbers.
# Find the sum of the numbers
# Divide the sum by the number of addends.
count = 0
sum = 0

for value in [ 5,4,3,2,1]:
  count= count + 1
  sum= sum + value
  print("Count is:", count, " Current value is:",value, " Count adds Value(Sum) equals to:", sum, )
print("The average of all these",count,"number/s are", int(sum/count))
  