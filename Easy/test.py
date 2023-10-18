def kidsWithCandies(candies, extraCandies):
    m = max(candies)
    return [m <= candy for candy in map(lambda x: x + extraCandies, candies)]

def kidsWithCandies2(candies, extraCandies):
    m = max(candies)
    return [(m <= candy+extraCandies) for candy in candies]

def kidWithCandies3(candies, extraCandies):
    bench = max(candies)
    l = []

    for i in candies:
        if i + extraCandies >= bench:
            l.append(True)
        else:
            l.append(False)
    
    return l

import time, random

candies =  [random.randint(1, 100) for i in range(10000000)]
extraCandies = random.randint(1,50)

start = time.time()
test2 = kidsWithCandies2(candies, extraCandies)
end = time.time()
print(f'time total 2: {end - start} .s')

start = time.time()
test3 = kidsWithCandies2(candies, extraCandies)
end = time.time()
print(f'time total 3: {end - start} .s')
