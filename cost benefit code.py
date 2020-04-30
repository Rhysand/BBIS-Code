


import math

# cost benefit analysis for drone



print("This program is a cost benefit analysis for investors to evaluate how long it will"
      "ntake to break even and how many times it will needed to be used: ") 
# these are the user inputs, there are some rounding functions as well and formulas

drone_flytime = int(input("Please enter the drone fly time in minutes: " ))#drone fly time in minutes

labor_cost = float(input("Please enter hourly pay:" ))

hiking_time = float(input("Please enter the time your employee can hike one mile in minutes,"
                          "the average is 1 mile per 35 minutes: " )) 

hiking_time2 = (60 - hiking_time)*(1/(hiking_time)) +1 # conversion for hiking time from minutes to hours

hiking_time3 = round(hiking_time2, 3) # rounding for hiking time

total_cost = float(input("Please enter the total amount of cost for the system: " )) #total cost input

drone_speed = float(input("Please enter the speed the drone flies in miles per hour: " ))#drone speed input

# these are formulas and rounds to the formulas

drone_coverage = (.5)*(drone_speed) # how far the drone will travel per hour

ranger_to_drone = (drone_coverage)*(1/(hiking_time2))# how long for the employee to reach drone coverage

ranger_to_drone2= round(ranger_to_drone, 2)# rounding the ranger to drone coverage

ranger_drone_price = (ranger_to_drone)*(labor_cost)# cost of ranger to drone coverage 

ranger_drone_price2 = round(ranger_drone_price, 2) # rounding for cost comparison

drone_break_even = (total_cost)/(ranger_drone_price) #the break even point

drone_break_even2 = round(drone_break_even, 2)# rounding the drone break even point

times_to_use_until_breakeven = (drone_break_even*60)/(drone_flytime)# drone times to use until break even


                                                    

#prints for the program

print("The total system cost is: ", "\n" "$",total_cost) 

print("Employee pay is: ", "\n" "$",labor_cost)

print("The distance the employee covers in miles per hour is: ", hiking_time3)

print("The distance the drone covers per hour is: ", "\n", drone_coverage,"miles")

print("The time the employee takes to cover drone coverage is: ", "\n", ranger_to_drone2, "Hours") 
                                   
print("How much it will cost for the employee to cover the drone in one hour is:", "\n", "$",ranger_drone_price2) 

print("This is how many hours it will take to offset total cost: ", "\n", drone_break_even2,"hours")

print("This is how many times you will have to use the drone to break even: ", "\n", math.ceil(times_to_use_until_breakeven))













