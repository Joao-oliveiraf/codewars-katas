# Problem Statement: Destroying Card Houses
# Sam has constructed a row of n card houses, numbered from 1 to n from left to right.
#
# Now, Sam wants to destroy all the card houses. To do this, he will place a fan to the left of the first card house,
# creating wind directed towards the card houses with a strength equal to a positive integer X.
#
# If the strength of the wind exceeds the resilience of the i-th card house, it will fall onto the next card house,
# reducing its resilience by a(i). If the resilience of the next card house is less than a(i), its resilience will become 0.
# The wind will pass through each card house from left to right one by one.
# If a card house falls, the resilience of the next card house will decrease before the wind reaches it.
# Find the minimum wind strength needed for all card houses to be destroyed.
#
# Explaining that part:
# When the strength of the wind is the same as the house, the house is destroyed but doesn't fall to the next house.
# Meaning, that the next house is not affected by the current house.
# When the wind is bigger than the house, the house will fall to the next house, reducing the strength of the next
# house by the current house's strength.
# Wind doesn't go through buildings. When a house breaks, it “stays in place” and therefore it takes + wind to knock
# it down so the wind can pass through.

# Examples:
# For the array [2, 5, 1, 3, 6], the minimum wind strength needed is 4.
# The resilience of the first card house is 2. It falls onto the second card house,
# reducing its resilience to 5-2=3. The second card house falls onto the third one, reducing its resilience to 0.
# The third card house falls onto the fourth one, reducing its resilience to 3-0=3.
# The fourth card house falls onto the fifth one,# reducing its resilience to 6-3=3. Since the resilience of the fifth
# card house is less than the wind strength, it falls.
#
# It can be shown that with a lower wind strength, not all card houses will fall.


hello = [2, 5, 1, 3, 6]
hello2 = [9, 8, 7, 6, 5]
import functools
def min_wind_strength(strengths):
    def myfunc(a, b):
        if a < 0:
            a = 0
        elif b < 0:
            b = 0
        return b - a
    return functools.reduce(myfunc, strengths)

print(min_wind_strength(hello))

