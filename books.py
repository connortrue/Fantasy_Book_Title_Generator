#!/usr/bin/python3
import random

# Databases
races = ["Elf", "Dwarf", "Orc", "Human", "Goblin", "Aasimar", "Argonian", "Asura", "Dragonspawn", "Draugr", "Dwemer", "Gold dwarf", "Grawl", "Half-draenei", "Mountain dwarf", "Treant"]
adjectives = ["Brave", "Cowardly", "Wise", "Foolish", "Mysterious", "Abandoned", "Able", "Absolute", "Adorable", "Adventurous", "Academic", "Acceptable", "Acclaimed", "Accomplished", "Accurate", "Aching"]
actions = ["Fighting", "Cooking", "Writing", "Singing", "Dancing", "Advise", "Agree", "Arrive", "Ask", "Bake", "Build", "Buy", "Call", "Catch", "Change", "Choose", "Clean", "Climb", "Close", "Come",
    "Cook", "Cry", "Cut", "Dance", "Decide", "Draw", "Drink", "Drive", "Eat", "Explain", "Fall", "Feel", "Find", "Fly", "Forget",
    "Give", "Go", "Help", "Hurt", "Jump", "Keep", "Know", "Laugh", "Leave", "Listen", "Make", "Move", "Need", "Open", "Play", "Read",
    "Ride", "Run", "Say", "See", "Sell"]
adverbs = ["Quickly", "Slowly", "Carefully", "Recklessly", "Quietly", "Abruptly", "Absently", "Accurately", "Adorably", "Adventurously", "Almost", "Always", "Angrily", "Anxiously", "Awkwardly", "Badly",
    "Beautifully", "Bitterly", "Blindly", "Boldly", "Briefly", "Briskly", "Brutally", "Calmly", "Carefully", "Casually", "Cautiously",
    "Cheerfully", "Clearly", "Closely", "Constantly", "Correctly", "Cruelly", "Dangerously", "Defiantly", "Deliberately", "Delicately",
    "Desperately", "Directly", "Eagerly", "Easily", "Elegantly", "Endlessly", "Enthusiastically", "Equally", "Especially", "Eventually",
    "Exactly", "Excitedly", "Exclusively", "Expectedly", "Fast", "Ferociously", "Fiercely", "Firmly"]
places = ["Quartzquarry", "Cindercliff", "Marblemeadow", "Obsidianoasis", "Sapphiresea", "Amethystarch", "Emeraldeye", "Topaztide", "Rubyridge", "Pearlplain",
    "Opalocean", "Jadejungle", "Garnetgrove", "Diamonddepth", "Amberabyss", "Turquoisetwilight", "Bronzebreeze", "Silvershadow", "Goldenglow", "Ironisle",
    "Coppercove", "Tintrack", "Leadlane", "Zinclabyrinth", "Nickelnook", "Aluminumarchway", "Titaniumtundra", "Platinumpath", "Chromiumchasm", "Manganesemeadow",
    "Cobaltcanyon", "Antimonyalley", "Silversteep", "Bismuthbend", "Thalliumthicket", "Indiumisle", "Tinteal", "Iridiuminlet", "Plutoniumpoint", "Goldengate",
    "Uraniumunderworld", "Neptuniumnexus", "Plutoniumpassage", "Americiumarch", "Curiumcreek", "Berkeliumbay", "Californiumcliff", "Einsteiniumedge", "Fermiumford", "Mendeleviummountain", "Mountains", "Forests", "Deserts", "Cities", "Oceans", "Zephyria", "Borendell", "Glimmerdeep", "Shadowfen", "Starlatch", "Thundertop", "Whisperwind", "Gloomwood", "Frostfield", "Sunblaze",
    "Moonveil", "Stormwatch", "Everpeak", "Galeglen", "Dawnhold", "Ravenrock", "Mistmoor", "Violetvale", "Silverstone", "Emeraldend",
    "Firefall", "Ironhaven", "Crystalcairn", "Brightbow", "Silentshore", "Goldenleaf", "Ebonheart", "Stormshroud", "Azuremyst", "Eaglecrest",
    "Windwail", "Thunderthrone", "Stonewarden", "Nightnook", "Flamefount", "Waterwhisper", "Skyshatter", "Earthend", "Lightlace", "Darkdell",
    "Frostfountain", "Sunshadow", "Starshroud", "Windwarp", "Flamefen", "Waterwatch", "Earthedge", "Lightloch", "Skyshard", "Darkdale"]
names = ["Eldorin", "Thalion", "Belerand", "Firion", "Nimrodel", "Gwindor", "Earendil", "Galadhrim", "Celeborn", "Elrohir", "Elenwe", "Glorfindel",
    "Haldir", "Idril", "Luthien", "Mithrandir", "Nienor", "Oropher", "Radagast", "Silmaril", "Turgon", "Ungoliant", "Varda", "Yavanna", "Zirakzigil",
    "Aerandir", "Barahir", "Curufin", "Denethor", "Ecthelion", "Finarfin", "Gil-galad", "Huan", "Ilmare", "Lorien", "Maedhros", "Namo", "Orome",
    "Pallando", "Rumil", "Sauron", "Aelrindel", "Belthor", "Ceolwulf", "Daelis", "Earendur", "Faelwen", "Gaelbryn", "Haereldor", "Iaeril", "Jaehaerys", "Kaeris", "Laenor", "Maerys",
    "Naeryndam", "Oaeryn", "Paeris", "Qaelin", "Raenor", "Saeran", "Taerys", "Uaerin", "Vaeril", "Waeris", "Xaeryn", "Yaeril", "Zaeris", "Aelwyn", "Belgar",
    "Ceolred", "Daelon", "Earendil", "Faelivrin", "Gaelion", "Haerelis", "Iaerion", "Jaehaeron", "Kaerion", "Laenar", "Maeron", "Naeron", "Oaeron", "Paeron",
    "Qaeron", "Raenys", "Saeron", "Taeron", "Uaeron", "Vaeron", "Waeron", "Xaeron", "Yaeron", "Zaeron", "Tulkas", "Ulmo", "Vaire", "Wingolot", "Xanwe", "Yrch", "Zaramoth"]

# Title formats
formats = [
    "A(n) {race}'s {adjective} Guide to {action}ing {adverb} in {adjective2} {place}",
    "{adjective} {action}: by {name}",
    "{place} Living: A {race} Perspective"
]

def generate_title():
    # Choose a random format
    title_format = random.choice(formats)

    # Fill in the format with random choices from the databases
    if "{adjective2}" in title_format:
        # If the format requires two different adjectives, select them separately
        adjectives_list = random.sample(adjectives, 2)
        title = title_format.format(
            race=random.choice(races),
            adjective=adjectives_list[0],
            action=random.choice(actions),
            adverb=random.choice(adverbs),
            place=random.choice(places),
            name=random.choice(names),
            adjective2=adjectives_list[1]
        )
    else:
        # If the format doesn't require two different adjectives, select one
        title = title_format.format(
            race=random.choice(races),
            adjective=random.choice(adjectives),
            action=random.choice(actions),
            adverb=random.choice(adverbs),
            place=random.choice(places),
            name=random.choice(names)
        )

    return title

# Generate and print a title
print(generate_title())