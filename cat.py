# Create a class called Cat
class Cat:
    # Every cat should have three attributes when they're created: name, preferred_food and meal_time
    def __init__(self,name,food,time):
        self.name = name
        self.preferred_food = food
        self.meal_time = time

    # Define a __str__() instance method.
    def __str__(self):
        return "This cat is named {}, it eats {}, and it's feeding time is {}.".format(self.name,self.preferred_food,self.meal_time)

    # Add an instance method called eats_at that returns the hour of the day with AM or PM that this cat eats.
    #     The return value should be something like "11 AM" or "3 PM"
    #     Make sure your method returns this string rather than printing it
    def eats_at(self):
        if self.meal_time == 0:
            return "12 AM"
        elif self.meal_time == 12:
            return "12 PM"
        elif self.meal_time > 0 and self.meal_time < 12:
            return "{} AM".format(self.meal_time)
        elif self.meal_time > 12 and self.meal_time < 24:
            return "{} PM".format(self.meal_time % 12)

    # Add another instance method called meow that returns a string of the cat telling you all about itself
    #     The return value should be something like "My name is Sparkles and I eat tuna at 11 AM"
    # Call the meow method on each of the cats you instantiated in step 3
    def meow(self):
        return "My name is {} and my favourite thing is eating {} at {}!".format(self.name,self.preferred_food,self.eats_at())


# Create two instances of the Cat class in your file
#     They should each have unique names, preferred foods and meal times
#     Let's assume meal_time is an integer from 0 to 23 (representing the hour of the day in 24 hour time)
midnight = Cat("Midnight","tuna",6)
mushu = Cat("Mushu","salmon",8)
print(midnight)
print(mushu)
print(midnight.eats_at())
print(midnight.meow())
print(mushu.meow())

# print("What do you want to call the cat?")
# cat_name = input()
# print("What does the cat eat?")
# cat_food = input()
# print("What time does it eat?")
# cat_time = int(input())
# new_cat = Cat(cat_name,cat_food,cat_time)
# print(new_cat)
# print(new_cat.meow())
