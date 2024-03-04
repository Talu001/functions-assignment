#3.travel cost estimator
def travel_cost(transportation_cost, accommodation_cost, activities_cost, duration):
   
    total_cost = (transportation_cost + accommodation_cost + activities_cost)

    total_cost *= duration

    return total_cost




transportation_cost = int(input("Enter transportation cost: $"))
accommodation_cost = int(input("Enter accommodation cost: $"))
activities_cost = int(input("Enter activities cost: $"))
travel_style = input("Enter travel style (budget/luxury):") == "luxury"
duration = int(input("Enter travel duration in days: "))

total_cost = travel_cost(transportation_cost, accommodation_cost, activities_cost, duration)

if travel_style == False:
    print("Your Estimated Travel Cost of Budget Is: $", total_cost)
else:
    print("Your Estimated Travel Cost of Luxury Is: $", total_cost)