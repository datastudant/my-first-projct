import time
import pygame
import datetime

def initialize_pygame():
    """Initialize the pygame mixer for playing music."""
    pygame.mixer.init()

def load_alarm_sound(sound_file):
    """Load the alarm sound file."""
    pygame.mixer.music.load(sound_file)

def play_alarm_sound():
    """Play the alarm sound until it finishes."""
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        time.sleep(1)

def set_alarm(alarm_time):
    """Set the alarm for the specified time."""
    print(f"Alarm set for {alarm_time}")
    sound_file = "v000002/my_music.mp3"  # Update the path as needed
    initialize_pygame()
    load_alarm_sound(sound_file)

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time: {current_time}")

        if current_time == alarm_time:
            print("Wake Up!")
            play_alarm_sound()
            break  # Exit the loop once the alarm has gone off
        time.sleep(1)

def main():
    """Main function to run the alarm clock."""
    alarm_time = input("Enter the time in HH:MM:SS format: ")
    try:
        # Validate the input time format
        datetime.datetime.strptime(alarm_time, "%H:%M:%S")
        set_alarm(alarm_time)
    except ValueError:
        print("Invalid time format. Please enter time in HH:MM:SS format.")

if __name__ == "__main__":
    main()