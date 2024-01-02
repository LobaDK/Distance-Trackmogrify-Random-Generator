from os import system, name
import random
import string
from time import sleep
import sqlite3
from json import loads


# Function to clear the console regardless of OS
def clear():
    system('cls' if name == 'nt' else 'clear')


try:
    import pyperclip
except ImportError:
    pass

# Create a string of all possible characters, both in lower and upper case, and digits
characters = string.ascii_letters + string.digits

# Load all the json files
Misc_color_mod = loads(open('data\\misc_color_mod.json').read())

Color_mod = loads(open('data\\color_mod.json').read())

Track_lighting_mod = loads(open('data\\track_lighting_mod.json').read())

Environment_mod = loads(open('data\\environment_mod.json').read())

Difficulty_mod = loads(open('data\\difficulty_mod.json').read())

Elevation_mod = loads(open('data\\elevation_mod.json').read())

Style_mod = loads(open('data\\style_mod.json').read())

Scenery_type_mod = loads(open('data\\scenery_type_mod.json').read())

Scenery_size_mod = loads(open('data\\scenery_size_mod.json').read())

Scenery_placement_mod = loads(open('data\\scenery_placement_mod.json').read())

Intensity_mod = loads(open('data\\intensity_mod.json').read())

Advanced_color_mod = loads(open('data\\advanced_color_mod.json').read())

Global_lighting_mod = loads(open('data\\global_lighting_mod.json').read())

Length_mod = loads(open('data\\length_mod.json').read())

Hazard_mod = loads(open('data\\hazard_mod.json').read())

# Set console size
system('mode 200,20')

# Enter the main loop
while (True):
    clear()
    output = '{Misc_color} {Color} {Track_lighting} {Environment} {Difficulty} {Elevation} {Style} {Scenery_type} {Scenery_size} {Scenery_placement} {Intensity} {Advanced_color} {Global_lighting} {Length} {Hazard} {Salt}'.format(
             Misc_color=" ".join(random.sample(Misc_color_mod, k=random.randint(0, 1))),
             Color=" ".join(random.sample(Color_mod, k=random.randint(0, 4))),
             Track_lighting=" ".join(random.sample(Track_lighting_mod, k=random.randint(0, 1))),
             Environment=" ".join(random.sample(Environment_mod, k=random.randint(0, 3))),
             Difficulty=" ".join(random.choices(Difficulty_mod, k=1, weights=(5, 10, 15, 20, 50, 70, 90, 100, 100, 100, 100, 100, 100, 100, 100))),
             Elevation=" ".join(random.sample(Elevation_mod, k=random.randint(0, 3))),
             Style=" ".join(random.sample(Style_mod, k=random.randint(0, 3))),
             Scenery_type=" ".join(random.sample(Scenery_type_mod, k=random.randint(0, 3))),
             Scenery_size=random.choice(Scenery_size_mod),
             Scenery_placement=random.choice(Scenery_placement_mod),
             Intensity=random.choice(Intensity_mod),
             Advanced_color=" ".join(random.sample(Advanced_color_mod, k=random.randint(0, 2))),
             Global_lighting=" ".join(random.sample(Global_lighting_mod, k=random.randint(0, 1))),
             Length=" ".join(random.choices(Length_mod, k=1, weights=(5, 10, 20, 40, 100, 80))),
             Hazard=" ".join(random.sample(Hazard_mod, k=random.randint(0, 7))),
             Salt="".join(random.choice(characters) for _ in range(random.randint(5, 40))))

    output = " ".join(output.split())
    sequence_hash = output.split()[-1]
    output_without_hash = output.rsplit(' ', 1)[0]

    try:
        pyperclip.copy(output)
        print("\nSequence has been copied to clipboard.\n\n", output)
    except NameError:
        print(output, "\n\nWant to get the sequence automatically saved to clipboard? Use 'pip install pyperclip' to install the required module, and it should work")

    while True:
        datebase_interact = ''
        datebase_interact = input('\nInteract with the database? y/N: ').upper()
        if datebase_interact == '':
            datebase_interact = 'N'
        if datebase_interact == 'Y':
            while True:
                con = sqlite3.connect('Distance-trackmogrify-sequences.db')
                cur = con.cursor()
                cur.execute('CREATE TABLE IF NOT EXISTS sequences(ID INTEGER PRIMARY KEY, sequence NOT NULL, sequence_hash NOT NULL, description, liked NOT NULL);')
                save_sequence = input('\n[R]eturn, [S]ave sequence or [V]iew database? R/S/V: ').upper()
                if save_sequence == 'R':
                    cur.close()
                    break
                elif save_sequence == 'S':
                    sequence_description = input('\nSequence description (press enter to skip): ')
                    while True:
                        sequence_liked = input('\nLiked the sequence? Y/N: ').upper()
                        if sequence_liked == 'Y':
                            liked = 'yes'
                        elif sequence_liked == 'N':
                            liked = 'no'
                        else:
                            print('Invalid choice')
                            sleep(2)
                            continue
                        break
                    cur.execute('INSERT INTO sequences (sequence, sequence_hash, description, liked) VALUES(?, ?, ?, ?);', (output_without_hash, sequence_hash, sequence_description, liked))
                    con.commit()
                    cur.close()

                elif save_sequence == 'V':
                    db_sequence = []
                    db_sequence_hash = []
                    db_description = []
                    db_liked = []
                    res = cur.execute('SELECT sequence, sequence_hash, description, liked from sequences')
                    for fetch in res.fetchall():
                        db_sequence.append(fetch[0])
                        db_sequence_hash.append(fetch[1])
                        db_description.append(fetch[2])
                        db_liked.append(fetch[3])
                    print('\n')
                    if len(db_sequence) == 0:
                        print('No entries in database')
                        sleep(2)
                        continue
                    for i in range(len(db_sequence)):
                        print(f'Entry[{i}] SEQUENCE: {db_sequence[i]}, SEQUENCE_HASH: {db_sequence_hash[i]}, DESCRIPTION: {db_description[i] if db_description[i] else "None"}, LIKED: {liked[i]}')
                        print('------------------------------------------------------------------------------------')
                        cur.close()
                    while True:
                        entry_id = ''
                        try:
                            entry_id = int(input('\nProvide entry ID to copy sequence and hash, or press enter without entering anything, to just return: '))
                        except ValueError:
                            if not entry_id:
                                break
                            print('\nPlease input a number')
                            continue
                        if len(db_sequence) > entry_id >= 0:
                            try:
                                pyperclip.copy(db_sequence[entry_id] + db_sequence_hash[entry_id])
                                print(f'\nSequence: {db_sequence[entry_id] + db_sequence_hash[entry_id]} copied to clipboard!')
                            except NameError:
                                print(f"\nPyperclip is not installed, but here's the sequence and hash: {db_sequence[entry_id] + db_sequence_hash[entry_id]}")
                            break
                        else:
                            print('\nEntry ID outside of range!')
                    continue
                else:
                    print('Invalid choice')
                    sleep(2)
                    continue
                break
            break
        elif datebase_interact == 'N':
            break
        else:
            print('Invalid choice')
            sleep(2)
            continue
