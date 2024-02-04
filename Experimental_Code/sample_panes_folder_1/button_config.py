import path_defs

def close_game_action(button_callbacks):
    button_callbacks['close_game']()

def close_game_button_config(regular_button_config):
    scale = regular_button_config['scale']
    font = regular_button_config['font']
    pane_dict = regular_button_config['pane_dict']
    button_callbacks = regular_button_config['button_callbacks']

    return {
        'x': pane_dict['journal_pane_x'] + 20*scale,
        'y': pane_dict['journal_pane_y'] + 40*scale,
        'width': 28*scale,
        'height': 28*scale,
        'button_color': (200, 0, 0, 255),
        'hover_color': (255, 0, 0, 255),
        'text_color': (0, 0, 0),
        'hover_text': 'Close Game',
        'image': path_defs.button_icon_path('close_game_button.png'),
        'font': font,
        'scale': scale,
        'action': lambda: button_callbacks['close_game']()
    }


def max_heroes_pane_action(button_callbacks):
    button_callbacks['max_heroes_pane']()

def max_heroes_pane_button_config(regular_button_config):
    scale = regular_button_config['scale']
    font = regular_button_config['font']
    pane_dict = regular_button_config['pane_dict']
    button_callbacks = regular_button_config['button_callbacks']

    return {
        'x': pane_dict['exploration_pane_x'] + -26*scale,
        'y': pane_dict['heroes_pane_y'] + 4*scale,
        'width': 24*scale,
        'height': 24*scale,
        'button_color': (200, 0, 0, 255),
        'hover_color': (255, 0, 0, 255),
        'text_color': (0, 0, 0),
        'hover_text': 'Maximize Pane',
        'image': path_defs.button_icon_path('max_heroes_pane_button.png'),
        'font': font,
        'scale': scale,
        'action': lambda: button_callbacks['max_heroes_pane']()
    }
