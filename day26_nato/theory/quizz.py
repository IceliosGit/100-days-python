# Quizz 1:
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# sentence_list = sentence.split()
# result = {item: len(item) for item in sentence_list}

# Quizz 2:
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}
weather_f = {day: (degree * 9/5) + 32 for (day, degree) in weather_c.items()}
print(weather_f)
