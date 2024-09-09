#Task 1
attendees = int(input("Enter number of attendees: "))

print("large hall") if attendees > 100 else print("conference room")
# Task 2
print("audio system") if attendees >= 150 else print("projector")
# Task 3
food_preference = input("Would you like vegetarian food?(yes or no): ")

print("Veggie Delight Caterers") if food_preference == "yes" else print("Gourmet Meals Caterers")