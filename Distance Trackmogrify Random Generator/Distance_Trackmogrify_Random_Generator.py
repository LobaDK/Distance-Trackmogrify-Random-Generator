import random
import os
try:
    import pyperclip
except:
    pass

os.system('mode 200,20')
while(True):
    Difficulty = ["Casual","Trivial","Safe","Easy","Normal","Medium","Advanced","Hard","Expert","Nightmare","Doom","Challenging","Maniac","Hazardous","Extreme"]
    Color = ["Red","Blue","Green","Yellow","Purple","Pink","Orange","Black","White","Grey","Tan"]
    Advanced_Color = ["Iridescent","Pearl","Monochromatic","Analogous","Triad","Complementary","Compound","Shades","Perlin"]
    Lighting = ["Iridescent","Desaturated","Saturated","Bright","Dim","Mute"]
    Track_Lighting = ["Iridescent","Desaturated","Saturated","Bright","Dim","Mute"]
    Global_Lighting = ["Sunrise","Morning","Day","Afternoon","Evening","Sunset","Night","Midnight","Light","Dark","Shadow","Moon"]
    Environment = ["Fog","Mist","Smoke","Ooze","Slime","Radioactive","Radiation","Biohazard","Storm","Thunder","Lightning","Gas","Ocean","Water","Marine","Sea"]
    Theme = ["space","Nightmare","Water","Dark","Fire","Not","Tron","Slime","Zebra","Rainbow","America","Stone","Transparent","Metallic","Metal","Ice","Neon","Copper","Silver","Gold","Platinum","Brass","Iron","Steel","Aluminum","Bronze","Titanium"]
    Elevation = ["Uphill","Climb","Ascent","Rise","Elevate","Downhill","Descent","Fall","Down","Lower"]
    Style = ["Twisty","Crazy","Bumpy","Road","Straight","Chill","Boring","Angry","Flat","Dull","Hilly","Zigzag","Loopy","UpsideDown","Snakey","Turn","Corkscrew","Helix","Inverted","Ceiling","Bouncy","Winding","Rollercoaster","Screwy"]
    Length = ["Fleeting","Momentary","Short","Quick","Long","Marathon"]
    Hazard = ["Pop-up","Barrier","Jump","Stop","Breakable","Egg","Roller","Laser","Saw","Shard","Dropper","Pumpkin"]
    Scenery = ["Empire","Virus","Infected","Ancient","Old","Broken","Simple","Toon","Minecraft","Halloween","Spooky","Graveyard","Round","Blocky","Angled","Spiky","Cube","Plane","Sphere","Cylinder","Hexagon","Triangle","Ring","Capsule","Transparent","Glow","Reflective","Flashing","Party","Disco","Dance","Dull","Speckledlights","Striped","Untextured","Rocklike","Factory","Plant","Industrial","City","Alien","Nature","Forest","Moving","Breakable","Alliancelogo","Logo","Sponsored","Cluster","Sign","Drone"]
    Size = ["Big","Super","Monster","Small","Tiny","Mini","Shrunk","Micro","Giant","Colossus"]
    Placement = ["Vast","Tight","Space","Above","Under","Below","Uniform"]
    Intensity = ["Barely","Slightly","Kinda","So","Very","Double","Super","Triple","Mega","Ultra","Insanely"]


    RNGOutput = []
    Output = ""
    Choice = ""
    Color_Choice = ""
    Advanced_Color_Choice = ""
    Lighting_Choice = ""
    Track_Lighting_Choice = ""
    Global_Lighting_Choice = ""
    Environment_Choice = ""
    Theme_Choice = ""
    Elevation_Choice = ""
    Style_Choice = ""
    Length_Choice = ""
    Hazard_Choice = ""
    Scenery_Choice = ""
    Size_Choice = ""
    Placement_Choice = ""
    Intensity_Choice = ""

    #Randomly add a difficulty
    Output = random.choice(Difficulty)
    #Randomly add between 0 and 2 colors
    RNGOutput += random.sample(Color, k=random.randint(0,2))
    if RNGOutput:
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add between 0 and 2 Advanced colors
    RNGOutput += random.sample(Advanced_Color, k=random.randint(0,2))
    if RNGOutput:
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add between 0 and 2 Lighting
    RNGOutput += random.sample(Lighting, k=random.randint(0,2))
    if RNGOutput:
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add between 0 and 2 Track_Lighting
    RNGOutput += random.sample(Track_Lighting, k=random.randint(0,2))
    if RNGOutput:
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add between 0 and 3 Global_Lighting
    RNGOutput += random.sample(Global_Lighting, k=random.randint(0,3))
    if RNGOutput:
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add between 0 and 3 Environment
    RNGOutput += random.sample(Environment, k=random.randint(0,3))
    if RNGOutput:
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add between 0 and 2 Theme
    RNGOutput += random.sample(Theme, k=random.randint(0,2))
    if RNGOutput:    
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add between 0 and 3 Elevation
    RNGOutput += random.sample(Elevation, k=random.randint(0,3))
    if RNGOutput:
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add between 0 and 3 Style
    RNGOutput += random.sample(Style, k=random.randint(0,3))
    if RNGOutput:
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add Length
    #RNGOutput += random.choices(Length,cum_weights=(5,15,35,60,90,115),k=1)
    Output += " " + " ".join(random.choices(Length,cum_weights=(5,15,35,60,90,115),k=1))
    RNGOutput = []
    #Randomly add between 1 and 12 Hazard
    #RNGOutput += random.sample(Hazard, k=random.randint(1,12))
    Output += " " + " ".join(random.sample(Hazard, k=random.randint(1,12)))
    RNGOutput = []
    #Randomly add between 0 and 3 Scenery
    RNGOutput += random.sample(Scenery, k=random.randint(0,3))
    if RNGOutput:
        Output += " " + " ".join(RNGOutput)
    RNGOutput = []
    #Randomly add Size
    Output += " " + random.choice(Size)
    #Randomly add Placement
    Output += " " + random.choice(Placement)
    #Randomly add Intensity
    Output += " " + random.choice(Intensity)
    
    try:
        pyperclip.copy(Output)
        print("Sequence has been copied to clipboard.\n\n",Output)
    except:
        print(Output,"\n\nWant to get the sequence automaticalled saved to clipboard? Use 'pip install pyperclip' to install the required module, and it should work")
    input("\nPress enter to conitnue")