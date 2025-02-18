import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

# List of CSV files to watch
csv_files = [
    "/home/steam/api2/JTWP.app-API-backend/data/death_events.csv",
    "/home/steam/api2/JTWP.app-API-backend/data/join_events.csv",
    "/home/steam/api2/JTWP.app-API-backend/data/killer_events.csv",
    "/home/steam/api2/JTWP.app-API-backend/data/kys_events.csv",
    "/home/steam/api2/JTWP.app-API-backend/data/left_events.csv",
    "/home/steam/api2/JTWP.app-API-backend/data/teamkill_events.csv"
]

# Extract the directory path
directory_to_watch = os.path.dirname(os.path.abspath(csv_files[0])) if csv_files else os.getcwd()

# Extract only the filenames for comparison
watched_filenames = {os.path.basename(file) for file in csv_files}

class CSVChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return

        # Check if the modified file is in our watch list
        if os.path.basename(event.src_path) in watched_filenames:
            print(f"{event.src_path} has been modified. Running buildStats.py...")
            try:
                result = subprocess.run(["python3", "/home/steam/api2/JTWP.app-API-backend/math/buildStats.py"], check=True, capture_output=True, text=True)
                print("buildStats.py output:\n", result.stdout)
            except subprocess.CalledProcessError as e:
                print(f"Error running buildStats.py: {e}\n{e.stderr}")

if __name__ == "__main__":
    event_handler = CSVChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_watch, recursive=False)
    observer.start()

    print(f"Watching directory: {directory_to_watch} for changes in: {watched_filenames}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down gracefully...")
        observer.stop()
    observer.join()

