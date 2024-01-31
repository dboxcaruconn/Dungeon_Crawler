import path_defs

# Close Game Button
def close_game_button_config(scale, font, pane_dict):
    return {
        'scale': scale,
        'x': pane_dict['journal_pane_x'] + 20*scale,
        'y': pane_dict['journal_pane_y'] + 40*scale,
        'width': 28*scale,
        'height': 28*scale,
        'button_color': (200, 0, 0, 128),
        'hover_color': (255, 0, 0, 128),
        'text_color': (0, 0, 0),
        # 'text': 'Close Game',
        'font': font,  # set this in GameManager
        'image': path_defs.button_icon_path('close_game_button.png'),
        'hover_text': 'Close Game'
    }

# Max Heroes Pane Button
def max_heroes_pane_button_config(scale, font, pane_dict):
    return {
        'scale': scale,
        'x': pane_dict['exploration_pane_x'] - 26*scale,
        'y': pane_dict['heroes_pane_y'] + 4*scale,
        'width': 24*scale,
        'height': 24*scale,
        'button_color': (200, 0, 0, 128),
        'hover_color': (255, 0, 0, 128),
        'text_color': (0, 0, 0),
        # 'text': 'Maximize Pane',
        'font': font,  # set this in GameManager
        'image': path_defs.button_icon_path('max_heroes_pane_button.png'),
        'hover_text': 'Maximize Pane'
    }
