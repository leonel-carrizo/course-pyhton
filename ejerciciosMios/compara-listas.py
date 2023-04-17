# Alice and Bob each created one problem for HackerRank. A reviewer rates the two challenges, awarding points on a scale from 1 to 100 for three categories: problem clarity, originality, and difficulty.
# The rating for Alice's challenge is the triplet a = (a[0], a[1], a[2]), and the rating for Bob's challenge is the triplet b = (b[0], b[1], b[2]).
# The task is to find their comparison points by comparing a[0] with b[0], a[1] with b[1], and a[2] with b[2].
# If a[i] > b[i], then Alice is awarded 1 point.
# If a[i] < b[i], then Bob is awarded 1 point.
# If a[i] = b[i], then neither person receives a point.
# Comparison points is the total points a person earned.
a = [17, 28, 30, 3, 10, 11]
b = [99, 16, 8, 3, 10, 11]

def compareTriplets(a, b):
    alice = 0
    bob = 0
    for x, y in zip(a, b):
        print("soy el for")
        if x > y:
            alice = alice + 1
            bob = bob + 0
            print("Alice ", x, "Bob ", y)
        if x < y:
            alice = alice + 0
            bob = bob + 1
            print("Alice ", x, "Bob ", y)
    return alice, bob

result = compareTriplets(a, b)
print(result)
