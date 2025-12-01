
def get_user_input():
    print("Welcome to Smart Traffic Advisor!")
    start = input("Enter your starting location (e.g., Delhi, Noida): ").strip().title()
    end = input("Enter your destination (e.g., Gurgaon, Faridabad): ").strip().title()
    time = input("Enter travel time in HH:MM format: ").strip()
    return start, end, time

