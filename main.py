from functools import reduce


def non_negative_sum(accumulator, element):
   if element >= 0:
       return accumulator + element
   else:
       return accumulator


def rainfall_total(the_list):
   return reduce(non_negative_sum, the_list, 0)


result1 = rainfall_total([3, -2, 4, 5, -1, 0])
result2 = rainfall_total([-1, -2, -3, -4])

print(result1)
print(result2)
