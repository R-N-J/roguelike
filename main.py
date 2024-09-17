#!/usr/bin/env python3
#https://rogueliketutorials.com/tutorials/tcod/v2/part-8/
import copy

import tcod

import color
from engine import Engine
import entity_factories
from procgen import generate_dungeon


def main() -> None:
    #actual size of the window    
    screen_width = 80 #80
    screen_height = 50 #50

    map_width = 80 #80
    map_height = 43 #45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    #tileset = tcod.tileset.load_tilesheet("dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD)
    
    #  Load a TrueType font from a file and return a Tileset object.
    #  The font size is 16x16 pixels, and the character map is the default one.
    #  The font is loaded from the file "HackNerdFontMono-Regular.ttf" in
    #  the current working directory.
    #  The tileset is stored in the variable tileset.
    # 
    #  The tileset is a Tileset object, which is a container for a set of
    #  tiles.  Each tile is a 2D array of pixels, and each pixel
    #   is either black (0) or white (1).  The tileset is used to draw
    #   the game world on the screen.
    # 
    # https://python-tcod.readthedocs.io/en/latest/tcod/tileset.html
    # see note in   https://github.com/libtcod/python-tcod/blob/main/examples/ttf.py
    #               https://github.com/libtcod/python-tcod/issues/75
    tileset = tcod.tileset.load_truetype_font("HackNerdFontMono-Regular.ttf",0 , 16)



    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine,
    )
    engine.update_fov()

    engine.message_log.add_message("Hello and welcome, adventurer, to yet another dungeon!", color.welcome_text)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)
            engine.event_handler.handle_events(context)


if __name__ == "__main__":
    main()
