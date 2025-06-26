# Initial setup
monkey_position = "door"
box_position = "window"
banana_position = "center"
monkey_on_box = False
banana_taken = False

# Step 1: Move to box
if monkey_position != box_position:
    print("Monkey moves to the box.")
    monkey_position = box_position

# Step 2: Push box to banana
if monkey_position == box_position:
    print("Monkey pushes the box to the banana.")
    box_position = banana_position
    monkey_position = banana_position

# Step 3: Climb the box
if monkey_position == box_position == banana_position:
    print("Monkey climbs the box.")
    monkey_on_box = True

# Step 4: Take the banana
if monkey_on_box:
    print("Monkey takes the banana.")
    banana_taken = True

# Final Result
if banana_taken:
    print("Success! Monkey got the banana!")
else:
    print("Monkey failed to get the banana.")