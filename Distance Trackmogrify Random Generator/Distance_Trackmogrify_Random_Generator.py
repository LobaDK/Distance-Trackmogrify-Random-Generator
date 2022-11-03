import os
import random
import string
from time import sleep
import sqlite3

try:
    import pyperclip
except:
    pass

os.system('mode 200,20')
while(True):

    characters = string.ascii_letters + string.digits

    Misc_color_mod = ['Rainbow',
                'Neon',
                'Tron',
                'America',
                'Transparent',
                'Zebra',
                'Stone',
                'Flame',
                'Fire',
                'Ice',
                'Metallic',
                'Metal',
                'Copper',
                'Gold',
                'Silver',
                'Platinum',
                'Brass',
                'Iron',
                'Steel',
                'Aluminum',
                'Bronze',
                'Titanium'
                ]

    Color_mod = ['indianRed',
                'lightCoral',
                'salmon',
                'darkSalmon',
                'lightSalmon',
                'crimson',
                'red',
                'fireBrick',
                'darkRed',
                'pink',
                'lightPink',
                'hotPink',
                'deepPink',
                'mediumVioletRed',
                'paleVioletRed',
                'coral',
                'tomato',
                'orangeRed',
                'darkOrange',
                'orange',
                'yellow',
                'lightYellow',
                'lemonChiffon',
                'lightGoldenrodYellow',
                'papayaWhip',
                'moccasin',
                'peachPuff',
                'paleGoldenrod',
                'khaki',
                'darkKhaki',
                'lavender',
                'thistle',
                'plum',
                'violet',
                'orchid',
                'fuchsia',
                'magenta',
                'mediumOrchid',
                'mediumPurple',
                'amethyst',
                'blueViolet',
                'darkViolet',
                'darkOrchid',
                'darkMagenta',
                'purple',
                'indigo',
                'slateBlue',
                'darkSlateBlue',
                'mediumSlateBlue',
                'greenYellow',
                'chartreuse',
                'lawnGreen',
                'lime',
                'limeGreen',
                'paleGreen',
                'lightGreen',
                'mediumSpringGreen',
                'springGreen',
                'mediumSeaGreen',
                'seaGreen',
                'forestGreen',
                'green',
                'darkGreen',
                'yellowGreen',
                'oliveDrab',
                'olive',
                'darkOliveGreen',
                'mediumAquamarine',
                'darkSeaGreen',
                'lightSeaGreen',
                'darkCyan',
                'teal',
                'aqua',
                'cyan',
                'lightCyan',
                'paleTurquoise',
                'aquamarine',
                'turquoise',
                'mediumTurquoise',
                'darkTurquoise',
                'cadetBlue',
                'steelBlue',
                'lightSteelBlue',
                'powderBlue',
                'lightBlue',
                'skyBlue',
                'lightSkyBlue',
                'deepSkyBlue',
                'dodgerBlue',
                'cornflowerBlue',
                'royalBlue',
                'blue',
                'mediumBlue',
                'darkBlue',
                'navy',
                'midnightBlue',
                'cornsilk',
                'blanchedAlmond',
                'bisque',
                'navajoWhite',
                'wheat',
                'burlyWood',
                'tan',
                'rosyBrown',
                'sandyBrown',
                'goldenrod',
                'darkGoldenrod',
                'peru',
                'chocolate',
                'saddleBrown',
                'sienna',
                'brown',
                'maroon',
                'white',
                'snow',
                'honeydew',
                'mintCream',
                'azure',
                'aliceBlue',
                'ghostWhite',
                'whiteSmoke',
                'seashell',
                'beige',
                'oldLace',
                'floralWhite',
                'ivory',
                'antiqueWhite',
                'linen',
                'lavenderBlush',
                'mistyRose',
                'gainsboro',
                'lightGrey',
                'darkGray',
                'gray',
                'dimGray',
                'lightSlateGray',
                'slateGray',
                'darkSlateGray',
                'black'
                ]

    Track_lighting_mod = ['Iridescent',
                    'Desaturated',
                    'Saturated',
                    'Bright',
                    'Dim',
                    'Mute'
                    ]

    Environment_mod = ['Fog',
                    'Mist',
                    'Smoke',
                    'Ooze',
                    'Slime',
                    'Radioactive',
                    'Radiation',
                    'Biohazard',
                    'Storm',
                    'Thunder',
                    'Lightning',
                    'Gas',
                    'Ocean',
                    'Water',
                    'Marine',
                    'Sea'
                    ]

    Difficulty_mod = ['Casual',
                    'Trivial',
                    'Safe',
                    'Easy',
                    'Normal',
                    'Medium',
                    'Advanced',
                    'Hard',
                    'Expert',
                    'Nightmare',
                    'Doom',
                    'Challenging',
                    'Maniac',
                    'Hazardous',
                    'Extreme'
                    ]

    Elevation_mod = ['Uphill',
                    'Climb',
                    'Ascent',
                    'Rise',
                    'Elevate',
                    'Downhill',
                    'Descent',
                    'Fall',
                    'Down',
                    'Lower'
                    ]

    Style_mod = ['Twisty',
                'Crazy',
                'Bumpy',
                'Road',
                'Straight',
                'Straightaway',
                'Chill',
                'Boring',
                'Angry',
                'Flat',
                'Dull',
                'Hilly',
                'Zigzag',
                'Loopy',
                'UpsideDown',
                'Snaky',
                'Turn',
                'Corkscrew',
                'Helix',
                'Inverse',
                'Inverted',
                'Ceiling',
                'Bouncy',
                'Winding',
                'Rollercoaster',
                'Screwy',
                ]

    Scenery_type_mod = ['Empire',
                        'Virus',
                        'Infected',
                        'Ancient',
                        'Old',
                        'Broken',
                        'Simple',
                        'Toon',
                        'Minecraft',
                        'Halloween',
                        'Spooky',
                        'Graveyard',
                        'Round',
                        'Blocky',
                        'Angled',
                        'Spiky',
                        'Spike',
                        'Cube',
                        'Box',
                        'Plane',
                        'Sphere',
                        'Ball',
                        'Cylinder',
                        'Tube',
                        'Hexagon',
                        'Hex',
                        'Triangle',
                        'Ring',
                        'Donut',
                        'Cone',
                        'Capsule',
                        'Pill',
                        'Transparent',
                        'Clear',
                        'Glow',
                        'Reflective',
                        'Flashing',
                        'Party',
                        'Disco',
                        'Dance',
                        'Dull',
                        'Speckledlights',
                        'Striped',
                        'Untextured',
                        'Rocklike',
                        'Factory',
                        'Plant',
                        'Industrial',
                        'City',
                        'Alien',
                        'Nature',
                        'Forest',
                        'Moving',
                        'Breakable',
                        'Alliancelogo',
                        'Alliance',
                        'Logo',
                        'Sponsored',
                        'Cluster',
                        'Sign',
                        'Drone'
                        ]

    Scenery_size_mod = ['Big',
                        'Super',
                        'Monster',
                        'Small',
                        'Tiny',
                        'Mini',
                        'Shrunk',
                        'Micro',
                        'Giant',
                        'Colossus'
                        ]

    Scenery_placement_mod = ['Vast',
                            'Tight',
                            'Space',
                            'Above',
                            'Under',
                            'Below',
                            'Uniform'
                            ]

    Intensity_mod = ['Barely',
                    'Slightly',
                    'Kinda',
                    'So',
                    'Very',
                    'Double',
                    'Super',
                    'Triple',
                    'Mega',
                    'Ultra',
                    'Insanely'
                    ]

    Advanced_color_mod = ['Iridescent',
                        'Pearl',
                        'Monochromatic',
                        'Analogous',
                        'Triad',
                        'Complementary',
                        'Compound',
                        'Shades',
                        'Perlin'
                        ]

    Global_lighting_mod = ['Sunrise',
                        'Morning',
                        'Day',
                        'Afternoon',
                        'Evening',
                        'Sunset',
                        'Night',
                        'Midnight',
                        'Light',
                        'Dark',
                        'Shadow',
                        'Moon'
                        ]

    Length_mod = ['Fleeting',
                'Momentary',
                'Short',
                'Quick',
                'Long',
                'Marathon'
                ]

    Hazard_mod = ['Pop-Up',
                'Barrier',
                'Jump',
                'Stop',
                'Breakable',
                'Egg',
                'Roller',
                'Laser',
                'Saw',
                'Shard',
                'Dropper',
                'Pumpkin'
                ]

    Output = '{Misc_color} {Color} {Track_lighting} {Environment} {Difficulty} {Elevation} {Style} {Scenery_type} {Scenery_size} {Scenery_placement} {Intensity} {Advanced_color} {Global_lighting} {Length} {Hazard} {Salt}'.format(
                            Misc_color=" ".join(random.sample(Misc_color_mod, k=random.randint(0,1))),
                            Color=" ".join(random.sample(Color_mod, k=random.randint(0,4))),
                            Track_lighting=" ".join(random.sample(Track_lighting_mod, k=random.randint(0,1))),
                            Environment=" ".join(random.sample(Environment_mod, k=random.randint(0,3))),
                            Difficulty=" ".join(random.choices(Difficulty_mod, k=1, weights=(5,10,15,20,50,70,90,100,100,100,100,100,100,100,100))),
                            Elevation=" ".join(random.sample(Elevation_mod, k=random.randint(0,3))),
                            Style=" ".join(random.sample(Style_mod, k=random.randint(0,3))),
                            Scenery_type=" ".join(random.sample(Scenery_type_mod, k=random.randint(0,3))),
                            Scenery_size=random.choice(Scenery_size_mod),
                            Scenery_placement=random.choice(Scenery_placement_mod),
                            Intensity=random.choice(Intensity_mod),
                            Advanced_color=" ".join(random.sample(Advanced_color_mod, k=random.randint(0,2))),
                            Global_lighting=" ".join(random.sample(Global_lighting_mod, k=random.randint(0,1))),
                            Length=" ".join(random.choices(Length_mod, k=1, weights=(5, 10, 20, 40, 100, 80))),
                            Hazard=" ".join(random.sample(Hazard_mod, k=random.randint(0,7))),
                            Salt="".join(random.choice(characters) for _ in range(random.randint(5,40)))
                            )

    Output = " ".join(Output.split())

    try:
        pyperclip.copy(Output)
        print("Sequence has been copied to clipboard.\n\n",Output)
    except:
        print(Output,"\n\nWant to get the sequence automatically saved to clipboard? Use 'pip install pyperclip' to install the required module, and it should work")

    while True:
        save_sequence = input('\nSave sequence to database? Y/N: ').upper()
        if save_sequence == 'Y':
            con = sqlite3.connect('Distance-trackmogrify-sequences.db')
            cur = con.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS sequences(ID INTEGER PRIMARY KEY, sequence NOT NULL, description, liked BOOLEAN NOT NULL);')
            sequence_description = input('\nSequence description (press enter to skip): ')
            while True:
                sequence_liked = input('\nLiked the sequence? Y/N: ').upper()
                if sequence_liked == 'Y':
                    liked = 1
                elif sequence_liked == 'N':
                    liked = 0
                else:
                    print('Invalid choice')
                    sleep(2)
                    continue
                break
            cur.execute('INSERT INTO sequences (sequence, description, liked) VALUES(?, ?, ?);', (Output, sequence_description, sequence_liked))
            con.commit()
            cur.close()

        elif save_sequence == 'N':
            break
        else:
            print('Invalid choice')
            sleep(2)
            continue
        break