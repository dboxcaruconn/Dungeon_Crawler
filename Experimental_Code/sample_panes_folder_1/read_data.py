import pandas as pd
import path_defs

def generate_button_config_code_from_excel(excel_path):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(excel_path, header=None)
    
    button_codes = []  # List to store code for all buttons

    # Helper function to generate code for a single button
    def generate_single_button_code(name, config):
        # Convert button name to the format used in image filenames
        image_name = f"{name}_button.png"  # Assuming the naming convention follows this pattern

        action_function = f"\ndef {name}_action(button_callbacks):\n" \
                          f"    button_callbacks['{name}']()\n"

        config_function = f"\ndef {name}_button_config(regular_button_config):\n" \
                          "    scale = regular_button_config['scale']\n" \
                          "    font = regular_button_config['font']\n" \
                          "    pane_dict = regular_button_config['pane_dict']\n" \
                          "    button_callbacks = regular_button_config['button_callbacks']\n\n" \
                          "    return {\n"

        # Iterate over the configuration items
        for prop, value in config.items():
            if prop in ['x', 'y', 'width', 'height']:
                # x, y, width, and height may include an offset based on pane_dict with scaling
                if isinstance(value, tuple):  # If value is a tuple, there's a pane prefix
                    config_function += f"        '{prop}': pane_dict['{value[0]}_pane_{prop}'] + {value[1]}*scale,\n"
                else:  # No pane prefix, apply the value with scaling if width or height
                    if prop in ['width', 'height']:
                        config_function += f"        '{prop}': {value}*scale,\n"
                    else:
                        config_function += f"        '{prop}': {value},\n"
            elif prop in ['button_color', 'hover_color', 'text_color']:
                # Assume value is a string with comma-separated numbers, convert it to a tuple
                color_values = tuple(int(num) for num in value.split(','))
                config_function += f"        '{prop}': {color_values},\n"
            elif prop in ['text','hover_text']:
                # hover_text is a string
                config_function += f"        '{prop}': '{value}',\n"
            elif prop == 'image':
                if value and value.lower() == 'yes':
                    # Add the image path using the name of the button
                    config_function += f"        '{prop}': path_defs.button_icon_path('{image_name}'),\n"

        # Add the font and scale at the end
        config_function += "        'font': font,\n"
        config_function += "        'scale': scale,\n"

        # Add the action line at the end using the button name
        config_function += f"        'action': lambda: button_callbacks['{name}']()\n    }}\n"

        return action_function + config_function

    # Iterate over the DataFrame rows
    current_button_name = None
    current_button_config = {}
    for index, row in df.iterrows():
        if row[0] == 'button_name':
            if current_button_name:
                # Finish the previous button and start a new one
                button_codes.append(generate_single_button_code(current_button_name, current_button_config))
            current_button_name = row[1]
            current_button_config = {}
        elif row[0] == 'end_button':
            # End the current button configuration
            button_codes.append(generate_single_button_code(current_button_name, current_button_config))
            current_button_name = None
            current_button_config = {}
        else:
            # Continue with the current button configuration
            if pd.notnull(row[2]):
                # If there's a third column, it's a tuple with a prefix
                current_button_config[row[0]] = (row[2], row[1])
            else:
                # Otherwise, it's a direct value
                current_button_config[row[0]] = row[1]

    # Generate code for the last button if the loop ends before 'end_button'
    if current_button_name:
        button_codes.append(generate_single_button_code(current_button_name, current_button_config))

    return "\n".join(button_codes)

# Path to the excel file - update this to the correct path
excel_path = path_defs.data_path('button_config_excel.xlsx')

# Generate Python code for all buttons in the dataframe
button_config_code = generate_button_config_code_from_excel(excel_path)

# Output path for the button_config.py - update this to the correct path
output_path = 'button_config.py'

def save_button_config_py(button_code, file_path):
    header = "import path_defs\n"
    full_code = header + button_code
    with open(file_path, 'w') as file:
        file.write(full_code)

# Save the generated code to button_config.py
save_button_config_py(button_config_code, output_path)
