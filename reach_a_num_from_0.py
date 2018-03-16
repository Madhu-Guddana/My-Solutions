# Question:
#   Given a number, reach the number from 0 by performing any of the 3
#   operation.
#   1) Addition of 1
#   2) Subtracting 1
#   3) Multiplication of 2
#   Eg:= To reach 9,  0->1->2->4->5->10->9.
#
#   Cost of operation.
#   Add and Sub will cost add_op_cost
#   Multiplication will cost mul_cost
#
#   Find the minimum cost required to reach the number from 0.

# Solution:
# 1.When it is even, then only option we have to reach num/2 is sub and
# div. Check for cost of both and do accordingly.
# 2. When it is odd, then we have 2 situation,
#   a. num+1 and num-1 are even, but which one will have more factors of 2
#      is what we have to know.
#      eg: num = 13, num-1 = 12 = 2*2*3, num+1 = 14 = 2*7.
#   b. So which is the easier way to reach half of more even number i.e 12.
#      And we need to reach 6 from 13
#

def get_more_neigh_even(odd_num):
  def count_fact_of_two(even_num):
    count = 0
    while even_num %2 == 1:
      even_num = even_num/2
      count += 1
    return count

  num1 = odd_num+1
  num2 = odd_num-1

  count1 = count_fact_of_two(num1)
  count2 = count_fact_of_two(num2)

  if count1 > count2:
    return num1
  return num2

def reach_zero(num):
  cost = 0
  while(num):
    if num==1:
      cost+= add_op_cost
      break

    temp = num
    extra_cost = 0

    # If number is odd.
    if num%2 == 1:
      temp = get_more_neigh_even(num)
      extra_cost = add_op_cost

    mul_way_cost = extra_cost + mul_op_cost
    add_way_cost = add_op_cost * (num-temp/2)

    num = temp/2
    cost += min(mul_way_cost, add_way_cost)
  return cost

# Inputs.
num = 200
add_op_cost = 1
mul_op_cost = 10

print reach_zero(num)
