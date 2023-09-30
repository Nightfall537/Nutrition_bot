print("Welcome to your Personal Nutrition bot")

name = input("\nEnter your name: ") #Enter your name

target_weight = input("\nEnter your target weight: ") #Enter the target weight you want to achieve

print(name.title())
print(target_weight + "kg")

print(name.title() + " your target weight goal is " + target_weight + "kg.")

print("\nHi there! How can I assist you today?")

user_input = input("\nChoose your goal,loose weight or muscle gain:  ")


AI_assistant = "\nThat's great! Are you sure you want to focus on " + user_input + "?"
print(AI_assistant)

AI_assistant = "\nTo help you with your " + user_input.title() + " \nI have a few options for you to choose from. Here are some items that can aid you to " + user_input.title() + "."
print(AI_assistant)

#Option one consist of a list of food group and one example of the recommended food item for muscle gain
option_one = {
    'carbohydrates' : 'banku',
    'proteins' : 'grilled tilapia fish',
    'vegetables' : 'kontomire stew',
    'fruits' : 'avocado'
}
#Option two consist of a list of food group and one example of the recommended food item for loose weight
option_two = {
    'lean protein' : 'grilled chicked breast',
    'high fiber carbohydrates' : 'waakye',
    'healthy fats' : 'garden egg stew with minimal palm oil',
    'low calorie fruits' : 'watermelon'
}

AI_assistant = "\nLet me know which option you'd like to include in your diet plan."

print(AI_assistant)

print("\nHere are your options: ")

for food_groups, foods in option_one.items():
    if user_input == 'muscle_gain':
        print('Food:' + foods + ';' + ' Food Group: ' + food_groups)


for food_groups1, foods2 in option_two.items():
    if user_input == 'loose weight':
        print('Food: ' + foods2 + ';' + ' Food Group: ' + food_groups1)

issue = input("List the food items you're allergic to or do not like: ")
#Enter a food item that you dont personally like for your own reason


if issue in option_one and option_two:
    issue.pop() #Remove a food item 

else: 
    if issue == ' ':
        #If the user does not type a food item, the code continues
        print("No issues found")
    
AI_assistant = "\Great choice! Good choice to help you with " + user_input + "."
print(AI_assistant)