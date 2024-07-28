import time

def countdown(time_sec):
    while time_sec > 0:
        mins, secs = divmod(time_sec, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_sec -= 1
    print("Time's up!")

while True:
    try:
        time_input = int(input("Enter the time in seconds: "))
        if time_input >= 0:
            countdown(int(time_input))
            break
        else:
            print("ERROR: The number must not be negative!")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")


