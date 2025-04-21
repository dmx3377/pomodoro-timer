import time

def timer(duration, message):
    """Runs a timer for a given duration and prints a message."""
    print(f"{message} for {duration // 60} minutes...")
    time.sleep(duration)
    print(f"{message} ended!")

def get_duration(prompt, default_minutes):
    """Gets a duration in minutes from the user, with a default value."""
    while True:
        user_input = input(f"{prompt} (default: {default_minutes} minutes): ").strip()
        if not user_input:
            return default_minutes * 60
        try:
            minutes = int(user_input)
            if minutes > 0:
                return minutes * 60
            else:
                print("Please enter a positive number of minutes.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def pomodoro_cycle(work_duration, short_break, long_break, num_pomodoros=4):
    """Runs a cycle of Pomodoros with short breaks and a long break."""
    pomodoro_count = 0
    while True:
        pomodoro_count += 1
        print(f"\n--- Pomodoro {pomodoro_count} ---")
        timer(work_duration, "Work session")

        if pomodoro_count % num_pomodoros == 0:
            print("\n--- Long Break ---")
            timer(long_break, "Long break")
        else:
            print("\n--- Short Break ---")
            timer(short_break, "Short break")

        another = input("Start another Pomodoro? (y/n): ").lower()
        if another != 'y':
            break

if __name__ == "__main__":
    print("--- Pomodoro Timer ---")
    work_minutes = get_duration("Enter work duration in minutes", 25)
    short_break_minutes = get_duration("Enter short break duration in minutes", 5)
    long_break_minutes = get_duration("Enter long break duration in minutes", 15)

    pomodoro_cycle(work_minutes, short_break_minutes, long_break_minutes)

    print("\nPomodoro cycle ended. Have a productive day!")
