import random

print("Welcome to kaun banega crorepati")
print("You won 1000 for every question")

l=["What is the capital of india ","What is the capital of up","Who is the prime minister of india","What is our national bird"]
d=[["(a)dellhi\n(b)jalandhar\n(c)chennai\n(d)mumbai"],["(a)lucknow\n(b)jahidpur\n(c)merathh\n(d)kanpur"],["(a)Narendra modi\n(b)Rahul gandhi\n(c)Amit saah\n(d)Akhilesh yadav"],["(a)peacock\n(b)crow\n(c)swift\n(d)Eagal"]]

count=0
money=0
while count<4:
    g = random.choice(l)
    print(g)

    s = l.index(g)
    l.remove(g)


    print(d[s][0])
    d.remove(d[s])
    inp=input("Enter your answer\n")
    if inp=="a":
        print("Sahi jawaab")

        money+=1000
    else:
        print("wrong answer")
    count+=1
print(f"You won {money} rupees")