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






#self.close_game_button = Button(
#    self.scale,x=journal_pane.x + self.scale*20, y=journal_pane.y + self.scale*40, width=self.scale*28, height=self.scale*28, 
#    button_color=(200, 0, 0, 128),
#    hover_color=(255, 0, 0, 128),
#    text_color=(0, 0, 0),
#    #text="Close Game",
#    font=self.custom_font,
#    image=path_defs.button_icon_path('close_game_button.png'),  # Pass the loaded image
#    hover_text="Close Game"
#)

#    self.max_heroes_pane_button = Button(
#        self.scale,x=exploration_pane.x - 26*self.scale, y=heroes_pane.y + 4*self.scale, width=24*self.scale, height=24*self.scale, 
#       button_color=(200, 0, 0, 128),
#       hover_color=(255, 0, 0, 128),
#       text_color=(0, 0, 0),
#       #text="Close Game",
#       font=self.custom_font,
#       image=path_defs.button_icon_path('max_heroes_pane_button.png'),  # Pass the loaded image
#       hover_text="Maximize Pane"
#    )