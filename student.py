import datetime
import json
from plyer import notification

class Student:
    def __init__(self, name, breaks=None):
        self.name = name
        self.breaks = breaks if breaks else []

    def start_break(self):
        if len(self.breaks) < 2:
            current_break = {'start': datetime.datetime.now().isoformat(), 'end': None}
            self.breaks.append(current_break)
            print(f"{self.name} started a break.")
        else:
            print(f"{self.name} has already taken 2 breaks today.")

    def end_break(self):
        if self.breaks and self.breaks[-1]['end'] is None:
            self.breaks[-1]['end'] = datetime.datetime.now().isoformat()
            print(f"{self.name} ended their break.")
        else:
            print(f"{self.name} has not started a break yet.")

    def get_current_break(self):
        if self.breaks and self.breaks[-1]['end'] is None:
            start_time = datetime.datetime.fromisoformat(self.breaks[-1]['start'])
            elapsed_time = (datetime.datetime.now() - start_time).total_seconds() / 60
            remaining_time = max(15 - elapsed_time, 0)

            # Check if the break has exceeded 15 minutes and send notification
            if elapsed_time > 1:
                notification.notify(
                    title='Break Time Alert',
                    message=f"{self.name}'s break exceeded 15 minutes!",
                    app_name='Break Time Tracker'
                )

            return f"{self.name}: Break started at {start_time.strftime('%H:%M:%S')}, {remaining_time:.2f} minutes remaining"
        return None

def save_breaks(students, filename="breaks.json"):
    with open(filename, 'w') as file:
        json.dump({name: student.breaks for name, student in students.items()}, file)

def load_breaks(filename="breaks.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return {name: Student(name, breaks) for name, breaks in data.items()}
    except FileNotFoundError:
        return {}
