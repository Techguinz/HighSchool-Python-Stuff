#The car dealership sells electric cars, which require charging before they can be driven.
#Charging the battery by 1% takes 10 minutes.
 #For example, a battery has 80% charge. It would take 200 minutes, or 3 hours and 20 minutes
#to charge to 100%.
 #Write an algorithm that:
#• asks the user for the current battery charge percentage
#• outputs "full" for a battery currently at 100%
#• calculates how long this battery would take to charge
#• outputs this in hours and minutes.
# Ask the user for the current battery charge percentage
current_charge = float(input("Enter the current battery charge percentage: "))

# Check if the battery is already at 100%
if current_charge == 100:
    print("Battery is already full.")
else:
    # Calculate the remaining charge needed to reach 100%
    remaining_charge = 100 - current_charge

    # Calculate the time required to charge the remaining percentage
    time_required_minutes = remaining_charge * 10

    # Convert time from minutes to hours and minutes
    hours = time_required_minutes // 60
    minutes1 = time_required_minutes % 60

    # Output the time required to charge
    if hours == 0:
        print("Charging will take", minutes1, "minutes.")
    elif hours == 1:
        print("Charging will take 1 hour and", minutes1, "minutes.")
    else:
        print("Charging will take", hours, "hours and", minutes1, "minutes.")


