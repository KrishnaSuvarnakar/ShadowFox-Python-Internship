workouts = {
    "Push-ups": 10,
    "Squats": 15,
    "Jumping Jacks": 20
}

print("Today's Workout:")

total = 0

for exercise, repetitions in workouts.items():
    print(exercise, "-", repetitions, "reps")
    total += repetitions

print("Total repetitions:", total)