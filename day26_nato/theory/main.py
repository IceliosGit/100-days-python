import random

objs = ["chicken", "pesto", "Beaver", "drum", "Wapiti"]
obj_score = {obj: random.randint(1, 50) for obj in objs}
print(obj_score)

great_objs = {obj: score for (obj, score) in obj_score.items() if score > 25}  # .items() give the returns a view object
# The view object contains the key-value pairs of the dictionary, as tuples in a list.
print(great_objs)
