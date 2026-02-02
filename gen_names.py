
import random
random.seed(42)
first = ["Alex","Ben","Chris","Daniel","Ethan","Finn","Henry","Jack","Leo","Lucas","Mason","Noah","Owen","Ryan","Sam","Theo","William","Zack","Amy","Bella","Chloe","Daisy","Emma","Grace","Hannah","Ivy","Lily","Mia","Nina","Olivia","Sophia","Zoe"]
last  = ["Smith","Johnson","Brown","Taylor","Anderson","Thomas","Jackson","White","Harris","Martin","Thompson","Garcia","Martinez","Robinson","Clark","Rodriguez","Lewis","Lee","Walker","Hall"]
with open("names_en_100k.txt","w",encoding="utf-8") as f:
    for _ in range(100000):
        f.write(f"{random.choice(first)} {random.choice(last)}\n")
print("OK: names_en_100k.txt")

