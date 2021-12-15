# Count the one and three chain links

import re
import pprint
import copy

pp = pprint.PrettyPrinter(indent=4)

with open('/Users/christian.asivido/repos/advent_2020/day20/input1_test.txt', 'r') as input:
    input_text = [line.strip() for line in input.readlines()]

id_pattern = r'''Tile (\d*):'''

index = 0
# Gather tiles
tiles = {}
while index < len(input_text):
    id = int(re.match(id_pattern, input_text[index]).groups()[0])
    index += 1

    tile_text = []
    while index < len(input_text) and input_text[index] != '':
        tile_text.append(input_text[index])
        index += 1

    tiles[id] = tile_text
    index += 1

markers = {
    'top': {},
    'bot': {},
    'left': {},
    'right': {},
}
def addTileMarker(value, id, side, markers):
    if value not in markers[side]:
        markers[side][value] = []
    markers[side][value].append(id)


# Extrapolate Tiles
for id, text in tiles.items():
    # Top
    length = len(text[0])
    top = 0
    power = 0
    for border in text[0]:
        if border == '#':
            top += 2**power
        power += 1

    # Bot
    bot = 0
    power = 0
    for border in text[-1]:
        if border == '#':
            bot += 2**power
        power += 1

    # Right & Left
    right = 0
    left = 0
    power = 0
    for line in text:
        if line[-1] == '#':
            right += 2**power
        if line[0] == '#':
            left += 2**power
        power += 1

    addTileMarker(top, id, 'top', markers)
    addTileMarker(bot, id, 'bot', markers)
    addTileMarker(left, id, 'left', markers)
    addTileMarker(right, id, 'right', markers)

    tiles[id] = [
        {
        'top': top,
        'bot': bot,
        'right': right,
        'left': left,
        },
        {
        'top': top,
        'bot': bot,
        'right': right,
        'left': left,
        },
    ]


starter = tiles[id]
placed_tiles = {
    # X
    len(tiles): {
        # Y
        len(tiles): starter
    }
}

pp.pprint(tiles)
pp.pprint(markers)

def intersection(lst1, lst2):
    return set(lst1).intersection(lst2)

# Assumption: Empty and at least one tile around this spot
def checkSpot(col_index, row_index, placed_tiles):
    fitting_tiles = []
    # Above
    if col_index-1 in placed_tiles:
        if row_index in placed_tiles[col_index-1]:
            tile_above = placed_tiles[col_index-1][row_index]
            if tile_above['bot'] in markers['top']:
                fitting_tiles.append(markers['top'][tile_above['bot']])
    # Below
    if col_index+1 in placed_tiles:
        if row_index in placed_tiles[col_index+1]:
            tile_below = placed_tiles[col_index+1][row_index]
            if tile_below['top'] in markers['bot']:
                fitting_tiles.append(markers['bot'][tile_below['top']])
    # Right-Side
    if col_index in placed_tiles:
        if row_index+1 in placed_tiles[col_index]:
            tile_right = placed_tiles[col_index][row_index+1]
            if tile_right['left'] in markers['right']:
                fitting_tiles.append(markers['right'][tile_right['left']])
    # Left-Side
    if col_index in placed_tiles:
        if row_index-1 in placed_tiles[col_index]:
            tile_left = placed_tiles[col_index][row_index-1]
            if tile_left['right'] in markers['left']:
                fitting_tiles.append(markers['left'][tile_left['right']])

    if not len(fitting_tiles):
        return []

    validTiles = fitting_tiles[0]
    for fitting_list in fitting_tiles[1:]:
        validTiles = intersection(validTiles, fitting_list)

    return validTiles

tile_ids_placed = [id]
while len(tile_ids_placed) < len(tiles):
    tileFoundID = 0
    cur_row = None
    cur_col = None
    for row_index, row in placed_tiles.items():
        if tileFoundID:
            break
        for col_index, tile in row.items():
            placeableTiles = []
            # Above
            if col_index-1 not in row:
                cur_row = row_index
                cur_col = col_index-1
                placeableTiles = checkSpot(cur_row, cur_col, placed_tiles)
            # Below
            if col_index+1 not in row and not len(placeableTiles):
                cur_row = row_index
                cur_col = col_index+1
                placeableTiles = checkSpot(cur_row, cur_col, placed_tiles)
            # Left
            if row_index-1 not in tiles and not len(placeableTiles):
                cur_row = row_index-1
                cur_col = col_index
                placeableTiles = checkSpot(cur_row, cur_col, placed_tiles)
            # Right
            if row_index+1 not in tiles and not len(placeableTiles):
                cur_row = row_index+1
                cur_col = col_index
                placeableTiles = checkSpot(cur_row, cur_col, placed_tiles)
            if len(placeableTiles):
                if len(placeableTiles > 1):
                    print('MULTIPLE TILES')
                    exit()

                tileFoundID = placeableTiles[0]
                break
    if tileFoundID:
        placed_tiles[cur_row][cur_col] = tiles[tileFoundID]
        tile_ids_placed[tileFoundID] = True

print(placed_tiles)
            # Mark new tile found and break loops, then add tile and restart