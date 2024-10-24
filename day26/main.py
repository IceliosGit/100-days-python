import random

objs = ["chicken", "pesto", "Beaver", "drum", "Wapiti"]
obj_score = {obj: random.randint(1, 50) for obj in objs}
print(obj_score)