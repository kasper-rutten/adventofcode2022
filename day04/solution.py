with open("input.txt", "r") as input:
    assignments = input.readlines()
assignments = [x.strip('\n') for x in assignments]
assignments = [x.split(',') for x in assignments]
fully_contains_count = 0
overlaps_count = 0
for a in assignments:
    r1_lim = a[0].split('-')
    range_1 = range(int(r1_lim[0]), int(r1_lim[1]) + 1)
    r2_lim = a[1].split('-')
    range_2 = range(int(r2_lim[0]), int(r2_lim[1]) + 1)
    if (min(range_1) <= min(range_2) and max(range_1) >= max(range_2)) or (min(range_2) <= min(range_1) and max(range_2) >= max(range_1)):
        fully_contains_count += 1
    # BEHOLD MY BRACKET FOREST!! ALL SHALL KNOW ME AND DESPAIR!!
    if (len(range(max(min(range_1), min(range_2)), min(max(range_1),max(range_2)) + 1)) > 0): # if the max of the lower bounds is lower than the min of the upper bounds, there is overlap
        overlaps_count += 1
print(fully_contains_count)
print(overlaps_count)