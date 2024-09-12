# Input the current traffic light color
light = input("Enter the traffic light color (Red, Yellow, Green): ").strip().lower()

# Determine the action based on the traffic light color
if light == "red":
    print("Stop")
elif light == "yellow":
    print("Slow down")
elif light == "green":
    print("Go")
else:
    print("Invalid color")


