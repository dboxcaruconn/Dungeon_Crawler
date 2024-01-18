import os

def button_icon_path(icon_name):
    button_icons_folder = 'Icons_Buttons'
    icon_path = os.path.join(os.path.dirname(__file__), button_icons_folder, icon_name)
    return icon_path

print(button_icon_path('close_button.png'))