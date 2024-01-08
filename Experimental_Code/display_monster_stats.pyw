import os
import pandas as pd
import tkinter as tk
from pandastable import Table

# Ensure single instance
import single_instance

def window_cleanup(lock_file_path):
    single_instance.clean_up(lock_file_path)
    window.destroy()
    
# Main function
def display_monster_stats():
    
    #Set the lock file path to ensure a single instance
    lock_file_path = single_instance.ensure_single_instance()
    
    # Set the working directory to Dungeon_Crawler
    os.chdir(os.path.join(os.path.dirname(__file__), ".."))

    # Read the monster_stats.xlsx from Stats folder and save as CSV in Current_Run folder
    stats_path = os.path.join("Stats", "monster_stats.xlsx")
    output_csv_path = os.path.join("Current_Run", "current_monster_stats.csv")
    df = pd.read_excel(stats_path, sheet_name='Export')
    df.to_csv(output_csv_path, index=False)

    # Create a window with specified dimensions
    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = screen_width // 2
    window_height = screen_height // 2
    window.geometry(f"{window_width}x{window_height}")

    # Bind the clean_up function to the window close event
    window.protocol("WM_DELETE_WINDOW", window_cleanup)

    # Display the CSV data in the window
    frame = tk.Frame(window)
    frame.pack(fill=tk.BOTH, expand=True)
    table = Table(frame, dataframe=df, showtoolbar=False, showstatusbar=True)
    table.show()
    
    # Bind the clean_up function to the window close event
    window.protocol("WM_DELETE_WINDOW", lambda: window_cleanup(lock_file_path))

    return window

# Open the window
if __name__ == "__main__":
    window = display_monster_stats()
    window.mainloop()
    