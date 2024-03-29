import os
import sys
import logging
import tempfile
import signal

# IF YOU NEED TO DELETE LOCK FILE, ENTER INTO TERMINAL:
# Remove-Item -Path "$(Get-ChildItem -Path $env:TEMP -Recurse -Filter "window_test_pic.lock" | Select-Object -ExpandProperty FullName)"

lock_file_path = None

def ensure_single_instance():
    global lock_file_path
    
    logging.basicConfig(filename='single_instance.log', level=logging.DEBUG,
                        format='%(asctime)s:%(levelname)s:%(message)s')

    logging.debug("Checking for existing application instance.")

    temp_dir = tempfile.gettempdir()
    lock_file_path = os.path.join(temp_dir, 'window_test_pic.lock')

    if os.path.exists(lock_file_path):
        logging.info("Application is already running.")
        sys.exit(0)

    try:
        with open(lock_file_path, 'x') as lock_file:
            lock_file.write('Lock')
        logging.debug("Lock file created.")
        return lock_file_path
    except FileExistsError:
        logging.info("Application is already running.")
        sys.exit(0)

def clean_up():
    global lock_file_path
    
    if os.path.exists(lock_file_path):
        os.remove(lock_file_path)
        logging.debug("Lock file deleted.")

def signal_handler(signum, frame):
    clean_up(lock_file_path)
    sys.exit(0)

def start():
    # Ensure single instance
    if not ensure_single_instance():
        sys.exit("Another instance of the game is already running.")
    
    # Set the signal handler for termination signals
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    
