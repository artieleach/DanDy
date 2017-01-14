race_list = ["Dwarf", "Elf", "Halfling", "Human", "Gnome", "Half Elf", "Half Orc"] 
class_list = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Sorcerer", "Rogue", "Wizard"]

skill_list = {
"Barbarian": ["Climb", "Craft", "Handle Animal", "Intimidate", "Jump", "Listen", "Ride", "Survival", "Swim"],
"Bard": ["Appraise", "Balance", "Bluff", "Climb", "Concentration", "Craft", "Decipher Script", "Diplomacy", "Disguise", "Escape Artist", "Gather Information", "Hide", "Intimidate", "Jump", "Knowledge (arcana)", "Knowledge (architecture and engineering)", "Knowledge (dungeoneering)", "Knowledge (geography)", "Knowledge (history)", "Knowledge (local)", "Knowledge (nature)", "Knowledge (nobility and royalty)", "Knowledge (religion)", "Knowledge (the planes)", "Listen", "Move Silently", "Perform", "Profession", "Ride", "Search", "Sense Motive", "Sleight of Hand", "Speak Language", "Spellcraft", "Swim", "Tumble", "Use Magic Device"],
"Cleric": ["Concentration", "Craft", "Diplomacy", "Heal", "Knowledge (arcana)", "Knowledge (history)", "Knowledge (religion)", "Knowledge (the planes)", "Profession", "Spellcraft"],
"Druid": ["Concentration", "Craft", "Diplomacy", "Handle Animal", "Heal", "Knowledge (nature)", "Listen", "Profession", "Ride", "Spellcraft", "Spot", "Survival", "Swim"],
"Fighter": ["Climb", "Craft", "Handle Animal", "Intimidate", "Jump", "Ride", "Swim"],
"Monk": ["Balance", "Climb", "Concentration", "Craft", "Diplomacy", "Escape Artist", "Hide", "Jump", "Knowledge (arcana)", "Knowledge (religion)", "Listen", "Move Silently", "Perform", "Profession", "Sense Motive", "Spot", "Swim", "Tumble"],
"Paladin": ["Concentration", "Craft", "Diplomacy", "Handle Animal", "Heal", "Knowledge (nobility and royalty)", "Knowledge (religion)", "Profession", "Ride", "Sense Motive", "Spot", "Swim", "Tumble"],
"Ranger": ["Climb", "Concentration", "Craft", "Handle Animal", "Heal", "Hide", "Jump", "Knowledge (local)", "Listen", "Move Silently", "Profession", "Ride", "Search", "Spot", "Survival", "Swim", "Use Rope"],
"Rogue": ["Appraise", "Balance", "Bluff", "Climb", "Craft", "Decipher Script", "Diplomacy", "Disable Device", "Disguise", "Escape Artist", "Forgery", "Gather Information", "Hide", "Intimidate", "Jump", "Knowledge (local)", "Listen", "Move Silently", "Open Lock", "Perform", "Profession", "Search", "Sense Motive", "Sleight of Hand", "Spot", "Swim", "Tumble", "Use Magic Device", "Use Rope"],
"Sorcerer": ["Bluff", "Concentration", "Craft", "Knowledge (arcana)", "Profession", "Spellcraft"],
"Wizard": ["Concentration", "Craft", "Decipher Script", "Knowledge (Arcana)", "Knowledge (Architecture and Engineering)", "Knowledge (Dungeoneering)", "Knowledge (Geography)", "Knowledge (History)", "Knowledge (Local)", "Knowledge (Nature)", "Knowledge (Nobility and Royalty)", "Knowledge (Religion)", "Knowledge (The Planes)", "Spellcraft", "Profession"]
}
class_health = {"Barbarian": 12, "Bard": 6, "Cleric": 8, "Druid": 8, "Fighter": 10, "Monk": 8, "Paladin": 10, "Ranger": 8, "Sorcerer": 4, "Rogue": 6, "Wizard": 4}
class_xp = {"Barbarian": 4, "Bard": 6, "Cleric": 2, "Druid": 4, "Fighter": 2, "Monk": 4, "Paladin": 2, "Ranger": 6, "Sorcerer": 2, "Rogue": 8, "Wizard": 2}
alignment1 = ["Lawful ", "Neutral ", "Chaotic "]
alignment2 = ["Good", "Neutral", "Evil"]
niche_feats = ["Combat Experience (int 13)", "Dodge (dex 13)", "Power Attack (str 13)", "Simple Weapon Proficency (druids, monks, rogues, and wizards)", "Spell Mastery (Wizard)", "Two weapon fighting (Dex 15)"]

feats = ["Acrobatic", "Agile", "Alertness", "Animal Affinity", "Armor Proficency", "Athletic", "Blind Fight", "Combat Casting", "Combat Reflexes", "Deceitful", "Deft Hands", "Diligent", "Endurance", "Eschew Materials", "Great Fortitude", "Improved Counterspell", "Improved Initiative", "Improved Unarmed Strike", "Investigator", "Iron Will", "Lightning Reflexes", "Magical Aptitude", "Martial Weapon Proficency", "Negotiator", "Nimble Fingers", "Persuasive", "Point Blank Shot", "Run", "Self Sufficent", "Skill Focus", "Spell Focus", "Spell Penetration", "Stealthy", "Toughness", "Track"]

melee_weapons = ["Club", "Dagger", "Javelin", "Light Mace", "Heavy Mace", "Short Spear", "Sickle", "Spear", "Spiked Gauntlet", "Great Club", "Morningstar", "Quarterstaff", "Scythe"]
ranged_weapons = ["Light Crossbow", "Sling", "Heavy Crossbow"]

armor = ["Padded", "Leather", "Padded Leather", "Chain Shirt", "Hide", "Scalemail", "Chainmail", "Breastplate", "Splintmail", "Bandedmail", "Half Plate"]
shields = ["Light Wooden", "Light Steel", "Heavy Wooden", "Heavy Steel", "Buckler"]

religions = ["Heironeous", "Moradin", "Yondalla", "Ehlonna", "Garl Glittergold", "Pelor", "Corellon Larethian", "Kord", "Wee Jas", "St. Cuthbert", "Boccob", "Fharlanghn", "Obad Hai", "Olidammara", "Hextor", "Nerull", "Vecna", "Erythnul", "Gruumsh"]

religion_domains = {
"Boccob": ["Knowledge", "Magic", "Trickery"],
"Corellon Larethian": ["Chaos", "Good", "Protection", "War"],
"Ehlonna": ["Animal", "Good", "Plant", "Sun"],
"Erythnul": ["Chaos", "Evil", "Trickery", "War"],
"Fharlanghn": ["Luck", "Protection", "Travel"],
"Garl Glittergold": ["Good", "Protection", "Trickery"],
"Gruumsh": ["Chaos", "Evil", "Strength"],
"Heironeous": ["Good", "Law", "War"],
"Hextor": ["Destruction", "Evil", "Law", "War"],
"Kord": ["Chaos", "Good Luck", "Strength"],
"Moradin": ["Earth", "Good", "Law", "Protection"],
"Nerull": ["Death", "Evil", "Trickery"],
"Obad Hai": ["Air", "Animal", "Earth", "Fire", "Plant", "Water"],
"Olidammara": ["Chaos", "Luck", "Trickery"],
"Pelor": ["Good", "Healing", "Strength"],
"St. Cuthbert": ["Destruction", "Law", "Protection", "Strength"],
"Vecna": ["Evil", "Knowledge", "Magic"],
"Wee Jas": ["Death", "Law", "Magic"],
"Yondalla": ["Good", "Law", "Protection"],
}
religion_weapons = {"Boccob": "Quarterstaff", "Corellon Larethian": "Long Sword", "Ehlonna": "Long Bow", "Erythnul": "Morningstar", "Fharlanghn": "Quarterstaff", "Garl Glittergold": "Battleaxe", "Gruumsh": "Spear", "Heironeous": "Long Sword", "Hextor": "Flail", "Kord": "Greatsword", "Moradin": "Warhammer", "Nerull": "Scythe", "Obad Hai": "Quarterstaff", "Olidammara": "Rapier", "Pelor": "Heavy Mace", "St. Cuthbert": "Light Mace", "Vecna": "Dagger", "Wee Jas": "Dagger", "Yondalla": "Short Sword"}
religion_alignments = {"Boccob": 5, "Corellon Larethian": 7, "Ehlonna": 4, "Erythnul": 9, "Fharlanghn": 5, "Garl Glittergold": 4, "Gruumsh": 9, "Heironeous": 1, "Hextor": 3, "Kord": 7, "Moradin": 1, "Nerull": 6, "Obad Hai": 5, "Olidammara": 8, "Pelor": 4, "St. Cuthbert": 2, "Vecna": 6, "Wee Jas": 2, "Yondalla": 1}
religion_table = {1: "Lawful Good", 2: "Lawful Neutral", 3: "Lawful Evil", 4: "Neutral Good", 5: "Neutral Neutral", 6: "Neutral Evil", 7: "Chaotic Good", 8: "Chaotic Neutral", 9: "Chaotic Evil"}

cleric_armor = ['Padded', 'Leather', 'Padded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Chainmail', 'Breastplate', 'Splintmail', 'Bandedmail', 'Half Plate']

druid_weapons = ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Short Spear', 'Sling', 'Spear']

ranger_favored_enemies = ['Aberration', 'Animal', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Giant', 'Humanoid (aquatic)', 'Humanoid (dwarf)', 'Humanoid (elf)', 'Humanoid (goblinoid)', 'Humanoid (gnoll)', 'Humanoid (gnome)', 'Humanoid (halfling)', 'Humanoid (human)', 'Humanoid (orc)', 'Humanoid (reptilian)', 'Magical beast', 'Monstrous humanoid', 'Ooze', 'Outsider (air)', 'Outsider (chaotic)', 'Outsider (earth)', 'Outsider (evil)', 'Outsider (fire)', 'Outsider (good)', 'Outsider (lawful)', 'Outsider (native)', 'Outsider (water)', 'Plant', 'Undead', 'Vermin']

druid_companions = ['Badger', 'Camel', 'Dire Rat', 'Dog', 'Riding Dog', 'Eagle', 'Hawk', 'Light Horse', 'Heavy Horse', 'Owl', 'Pony', 'Small Snake', 'Medium Snake', 'Viper', 'Wolf']

fighter_religions = ['Heironeous', 'Kord', 'St. Cuthbert', 'Hextor', 'Erythnul']

monk_weapons = ['Club', 'Light Crossbow', 'Heavy Crossbow', 'Dagger', 'Handaxe', 'Javelin', 'Kama', 'Nunchaku', 'Quarterstaff', 'Sai', 'Shuriken', 'Siangham', 'Sling']

rogue_weapons = ['Hand Crossbow', 'Sap', 'Short Bow', 'Rapier', 'Short Sword', 'Club', 'Dagger', 'Javelin', 'Light Mace', 'Heavy Mace', 'Short Spear', 'Sickle', 'Spear', 'Spiked Gauntlet', 'Great Club', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Light Crossbow', 'Heavy Crossbow']

familiars = ["Bat", "Cat", "Hawk", "Lizard", "Owl", "Rat", "Raven", "Snake", "Toad", "Weasel"]

wizard_schools = {'Abjuration':2, 'Conjuration':2, 'Divination':1, 'Enchantment':2, 'Evocation':2, 'Illusion':2, 'Necromancy':2, 'Transmutation':2}
wizard_weapons = ['Club', 'Dagger', 'Heavy Crossbow', 'Light Crossbow', 'Quarterstaff']

language_list = ["Abyssal", "Aquan", "Auran", "Celestial", "Draconic", "Dwarven", "Elven", "Giant", "Gnome", "Goblin", "Gnoll", "Halfling", "Ignan", "Infernal", "Orc", "ylvan", "Terran", "Undercommon"]

weapon_data = {
"Gauntlet": {"Cost": 2, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Dagger": {"Cost": 2, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Spiked Gauntlet": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Light Mace": {"Cost": 5, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "One"},
"Sickle": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Club": {"Cost": 0, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Bludgeoning", "Handed": "One"},
"Heavy Mace": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "One"},
"Morningstar": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning and Piercing", "Handed": "One"},
"Short Spear": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Long Spear": {"Cost": 5, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 9, "Type": "Piercing", "Handed": "Two"},
"Quarterstaff": {"Cost": 0, "Damage (S)": "2d6", "Damage (M)": "2d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "Two"},
"Spear": {"Cost": 2, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Piercing", "Handed": "Two"},
"Heavy Crossbow": {"Cost": 50, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Piercing", "Handed": "One"},
"Light Crossbow": {"Cost": 35, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Javelin": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Sling": {"Cost": 0, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Throwing Axe": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Hammer": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Handaxe": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 3, "Type": "Slashing", "Handed": "One"},
"Kukri": {"Cost": 8, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Pick": {"Cost": 4, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 4, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Sap": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Short Sword": {"Cost": 10, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Battleaxe": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Flail": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Long Sword": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Heavy Pick": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 4, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Rapier": {"Cost": 20, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Scimitar": {"Cost": 15, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Trident": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Warhammer": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Falchion": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Glaive": {"Cost": 8, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Greataxe": {"Cost": 20, "Damage (S)": "1d10", "Damage (M)": "1d12", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Great Club": {"Cost": 5, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "Two"},
"Heavy Flail": {"Cost": 15, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Greatsword": {"Cost": 50, "Damage (S)": "1d10", "Damage (M)": "2d6", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Guisarme": {"Cost": 9, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Halberd": {"Cost": 10, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 12, "Type": "Piercing or Slashing", "Handed": "Two"},
"Lance": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Ranseur": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Piercing", "Handed": "Two"},
"Scythe": {"Cost": 18, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 4, "Weight": 10, "Type": "Piercing or Slashing", "Handed": "Two"},
"Long Bow": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 3, "Type": "Piercing", "Handed": "Two"},
"Short Bow": {"Cost": 30, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 2, "Type": "Piercing", "Handed": "Two"},
"Kama": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Nunchaku": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Sai": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Siangham": {"Cost": 3, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Bastard Sword": {"Cost": 35, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Dwarven Waraxe": {"Cost": 30, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 8, "Type": "Slashing", "Handed": "One"},
"Whip": {"Cost": 1, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Orc Doubleaxe": {"Cost": 60, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 3, "Weight": 15, "Type": "Slashing", "Handed": "Two"},
"Spiked Chain": {"Cost": 25, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Dire Flail": {"Cost": 90, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Gnome Hooked Hammer": {"Cost": 20, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3.5, "Weight": 6, "Type": "Bludgeoning and piercing", "Handed": "Two"},
"Two Bladed Sword": {"Cost": 100, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Dwarven Urgrosh": {"Cost": 50, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3, "Weight": 12, "Type": "Slashing or Piercing", "Handed": "Two"},
"Bolas": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Hand Crossbow": {"Cost": 100, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Heavy Repeating Crossbow": {"Cost": 400, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 12, "Type": "Piercing", "Handed": "One"},
"Light Repeating Crossbow": {"Cost": 250, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Net": {"Cost": 20, "Damage (S)": "0", "Damage (M)": "0", "Critical": 0, "Weight": 6, "Type": "None", "Handed": "Two"},
"Shuriken": {"Cost": 1, "Damage (S)": "1", "Damage (M)": "1d2", "Critical": 2, "Weight": 0.5, "Type": "Piercing", "Handed": "One"},
"Unarmed": {"Cost": 0, "Damage (S)": "1", "Damage (M)": "1", "Critical": 0, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"}
}
armor_data = {
"None": {"Cost": 0, "Armor Bonus": 0, "Max Dex Bonus": 100, "Armor Check": 0, "Arcane Spell Failure": 0, "Weight": 0, "Class": "None"},
"Padded": {"Cost": 5, "Armor Bonus": 1, "Max Dex Bonus": 8, "Armor Check": 0, "Arcane Spell Failure": 5, "Weight": 10, "Class": "Light"},
"Leather": {"Cost": 10, "Armor Bonus": 2, "Max Dex Bonus": 6, "Armor Check": 0, "Arcane Spell Failure": 10, "Weight": 15, "Class": "Light"},
"Padded Leather": {"Cost": 25, "Armor Bonus": 3, "Max Dex Bonus": 5, "Armor Check": -1, "Arcane Spell Failure": 15, "Weight": 20, "Class": "Light"},
"Chain Shirt": {"Cost": 100, "Armor Bonus": 4, "Max Dex Bonus": 4, "Armor Check": -2, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Light"},
"Hide": {"Cost": 15, "Armor Bonus": 3, "Max Dex Bonus": 4, "Armor Check": 3, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Medium"},
"Scalemail": {"Cost": 50, "Armor Bonus": 4, "Max Dex Bonus": 3, "Armor Check": 4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Chainmail": {"Cost": 150, "Armor Bonus": 5, "Max Dex Bonus": 2, "Armor Check": 5, "Arcane Spell Failure": 30, "Weight": 40, "Class": "Medium"},
"Breastplate": {"Cost": 200, "Armor Bonus": 5, "Max Dex Bonus": 3, "Armor Check": -4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Splintmail": {"Cost": 200, "Armor Bonus": 6, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 45, "Class": "Heavy"},
"Bandedmail": {"Cost": 250, "Armor Bonus": 6, "Max Dex Bonus": 1, "Armor Check": 6, "Arcane Spell Failure": 35, "Weight": 35, "Class": "Heavy"},
"Half Plate": {"Cost": 600, "Armor Bonus": 7, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 50, "Class": "Heavy"},
"Buckler": {"Cost": 15, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Wooden": {"Cost": 3, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Steel": {"Cost": 9, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 6, "Class": "Light"},
"Heavy Wooden": {"Cost": 7, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 10, "Class": "Heavy"},
"Heavy Steel": {"Cost": 20, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 15, "Class": "Heavy"}
}

barbarian_armor = ['Padded Leather', 'Padded Leather', 'Chain Shirt', 'Hide', 'Scalemail', 'Chainmail', 'Breastplate']

bard_weapons = ['Whip', 'Long Sword', 'Rapier', 'Sap', 'Short Sword', 'Short Bow', 'Dagger', 'Gauntlet', 'Light Mace', 'Sickle', 'Club', 'Heavy Mace', 'Morningstar', 'Short Spear', 'Long Spear', 'Quarterstaff', 'Spear', 'Heavy Crossbow', 'Light Crossbow', 'Javelin', 'Sling']

dwarf_first_names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik",
"Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
dwarf_last_names = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
dwarf_clans = ["Balderk", "Dankil", "Gorunn", " Holderhek", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
dwarf_skin_tone = ['Deep Tan', 'Pale', 'Beige', 'Light Brown']
dwarf_hair_color = ['Black', 'Brown', 'Grey']
dwarf_hair_type = ['Curly', 'Wavy', 'Straight']
dwarf_eye_color = ['Brown', 'Black', 'Deep Grey']

elf_first_names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias",
"Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
elf_last_names = ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Naïlo", "Siannodel", "Xiloscient"]
elf_skin_tone = ['Light Pale', 'Pale', 'Dark Pale']
elf_hair_color = ['Black', 'Brown', 'Grey']
elf_hair_type= ['Curly', 'Wavy', 'Straight']
elf_eye_color = ['Light Green', 'Green', 'Dark Green', 'Green Grey']

halfling_first_names = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
halfling_last_names = ["Brushgather", "Goodbarrel", "Greenbottle", "Highhill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"]
halfling_skin_tones = ['Light Pale', 'Pale', 'Pink']

half_elf_skin_tones = ['Brown', 'Beige', 'White', 'Pink']
half_elf_hair_color = ['Black', 'Brown', 'Blond', 'Red', 'White']
half_elf_hair_type = ['Curly', 'Wavy', 'Straight']
half_elf_eye_color = ['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel']

half_orc_skin_tone = ['Black', 'Brown', 'Grey', 'White']
half_orc_hair_color = ['Black', 'Brown', 'Blond', 'Red', 'White']
half_orc_hair_type = ['Curly', 'Wavy', 'Straight']
half_orc_eye_color = ['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel']

gnome_first_names = ["Boddynock", "Dimble", "Fonkin", "Gimble", "Glim", "Gerbo", "Jebeddo", "Namfoodle", "Roondar", "Seebo", "Zook"]
gnome_last_names = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]
gnome_clans = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]
gnome_nick_names = ["Aleslosh", "Ashhearth", "Badger", "Cloak", "Doublelock", "Filchbatter", "Fnipper", "Oneshoe", "Sparklegem", "Stumbleduck"]
gnome_eye_color = ['Light Blue', 'Blue', 'Dark Blue', 'Blue Grey']

orc_first_names = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront", "Shump", "Thokk"]
human_first_names = {
"Calishite": {"Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir"},
"Chondathan": {"Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd"},
"Damaran": {"Bor", "Fodel", "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor"},
"Illuskan": {"Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth"},
"Mulan": {"Aoth", "Bareris", "Ehput Ki", "Kethoth", "Mumed", "Ramas", "So Kehur", "Thazar De", "Urhur"},
"Rashemi": {"Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar", "Vladislak"},
"Shou": {"Chien", "Huang", "Kao", "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum", "Tan", "Wan"},
"Turami": {"Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"}
}
human_last_names = {
"Calishite": {"Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein"},
"Chondathan": {"Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag"},
"Damaran": {"Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag"},
"Illuskan": {"Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind", "Windrivver"},
"Mulan": {"Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"},
"Rashemi": {"Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"},
"Shou": {"An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui", "Wen"},
"Turami": {"Agosto", "Astorio", "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"}
}
human_tribes = ["Calishite", "Chondathan", "Damaran", "Illuskan", "Mulan", "Rashemi", "Shou", "Turami"]
human_skin_tone = ['Black', 'Brown', 'Beige', 'White', 'Pink']
human_hair_color = ['Black', 'Brown', 'Blond', 'Red', 'White']
human_hair_type = ['Curly', 'Wavy', 'Straight']
human_eye_color = ['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel']


"Vecna": ["Evil", "Knowledge", "Magic"],
"Wee Jas": ["Death", "Law", "Magic"],
"Yondalla": ["Good", "Law", "Protection"],
}
religion_weapons = {"Boccob": "Quarterstaff", "Corellon Larethian": "Long Sword", "Ehlonna": "Long Bow", "Erythnul": "Morningstar", "Fharlanghn": "Quarterstaff", "Garl Glittergold": "Battleaxe", "Gruumsh": "Spear", "Heironeous": "Long Sword", "Hextor": "Flail", "Kord": "Greatsword", "Moradin": "Warhammer", "Nerull": "Scythe", "Obad Hai": "Quarterstaff", "Olidammara": "Rapier", "Pelor": "Heavy Mace", "St. Cuthbert": "Light Mace", "Vecna": "Dagger", "Wee Jas": "Dagger", "Yondalla": "Short Sword"}
religion_alignments = {"Boccob": 5, "Corellon Larethian": 7, "Ehlonna": 4, "Erythnul": 9, "Fharlanghn": 5, "Garl Glittergold": 4, "Gruumsh": 9, "Heironeous": 1, "Hextor": 3, "Kord": 7, "Moradin": 1, "Nerull": 6, "Obad Hai": 5, "Olidammara": 8, "Pelor": 4, "St. Cuthbert": 2, "Vecna": 6, "Wee Jas": 2, "Yondalla": 1}
religion_table = {1: "Lawful Good", 2: "Lawful Neutral", 3: "Lawful Evil", 4: "Neutral Good", 5: "Neutral Neutral", 6: "Neutral Evil", 7: "Chaotic Good", 8: "Chaotic Neutral", 9: "Chaotic Evil"}

cleric_armor = ['Padded', 'Leather', 'Padded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Chainmail', 'Breastplate', 'Splintmail', 'Bandedmail', 'Half Plate']

druid_weapons = ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Short Spear', 'Sling', 'Spear']

ranger_favored_enemies = ['Aberration', 'Animal', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Giant', 'Humanoid (aquatic)', 'Humanoid (dwarf)', 'Humanoid (elf)', 'Humanoid (goblinoid)', 'Humanoid (gnoll)', 'Humanoid (gnome)', 'Humanoid (halfling)', 'Humanoid (human)', 'Humanoid (orc)', 'Humanoid (reptilian)', 'Magical beast', 'Monstrous humanoid', 'Ooze', 'Outsider (air)', 'Outsider (chaotic)', 'Outsider (earth)', 'Outsider (evil)', 'Outsider (fire)', 'Outsider (good)', 'Outsider (lawful)', 'Outsider (native)', 'Outsider (water)', 'Plant', 'Undead', 'Vermin']

druid_companions = ['Badger', 'Camel', 'Dire Rat', 'Dog', 'Riding Dog', 'Eagle', 'Hawk', 'Light Horse', 'Heavy Horse', 'Owl', 'Pony', 'Small Snake', 'Medium Snake', 'Viper', 'Wolf']

fighter_religions = ['Heironeous', 'Kord', 'St. Cuthbert', 'Hextor', 'Erythnul']

monk_weapons = ['Club', 'Light Crossbow', 'Heavy Crossbow', 'Dagger', 'Handaxe', 'Javelin', 'Kama', 'Nunchaku', 'Quarterstaff', 'Sai', 'Shuriken', 'Siangham', 'Sling']

rogue_weapons = ['Hand Crossbow', 'Sap', 'Short Bow', 'Rapier', 'Short Sword', 'Club', 'Dagger', 'Javelin', 'Light Mace', 'Heavy Mace', 'Short Spear', 'Sickle', 'Spear', 'Spiked Gauntlet', 'Great Club', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Light Crossbow', 'Heavy Crossbow']

familiars = ["Bat", "Cat", "Hawk", "Lizard", "Owl", "Rat", "Raven", "Snake", "Toad", "Weasel"]

wizard_schools = {'Abjuration':2, 'Conjuration':2, 'Divination':1, 'Enchantment':2, 'Evocation':2, 'Illusion':2, 'Necromancy':2, 'Transmutation':2}
wizard_weapons = ['Club', 'Dagger', 'Heavy Crossbow', 'Light Crossbow', 'Quarterstaff']

language_list = ["Abyssal", "Aquan", "Auran", "Celestial", "Draconic", "Dwarven", "Elven", "Giant", "Gnome", "Goblin", "Gnoll", "Halfling", "Ignan", "Infernal", "Orc", "ylvan", "Terran", "Undercommon"]

weapon_data = {
"Gauntlet": {"Cost": 2, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Dagger": {"Cost": 2, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Spiked Gauntlet": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Light Mace": {"Cost": 5, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "One"},
"Sickle": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Club": {"Cost": 0, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Bludgeoning", "Handed": "One"},
"Heavy Mace": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "One"},
"Morningstar": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning and Piercing", "Handed": "One"},
"Short Spear": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Long Spear": {"Cost": 5, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 9, "Type": "Piercing", "Handed": "Two"},
"Quarterstaff": {"Cost": 0, "Damage (S)": "2d6", "Damage (M)": "2d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "Two"},
"Spear": {"Cost": 2, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Piercing", "Handed": "Two"},
"Heavy Crossbow": {"Cost": 50, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Piercing", "Handed": "One"},
"Light Crossbow": {"Cost": 35, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Javelin": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Sling": {"Cost": 0, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Throwing Axe": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Hammer": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Handaxe": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 3, "Type": "Slashing", "Handed": "One"},
"Kukri": {"Cost": 8, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Pick": {"Cost": 4, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 4, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Sap": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Short Sword": {"Cost": 10, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Battleaxe": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Flail": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Long Sword": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Heavy Pick": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 4, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Rapier": {"Cost": 20, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Scimitar": {"Cost": 15, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Trident": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Warhammer": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Falchion": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Glaive": {"Cost": 8, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Greataxe": {"Cost": 20, "Damage (S)": "1d10", "Damage (M)": "1d12", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Great Club": {"Cost": 5, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "Two"},
"Heavy Flail": {"Cost": 15, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Greatsword": {"Cost": 50, "Damage (S)": "1d10", "Damage (M)": "2d6", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Guisarme": {"Cost": 9, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Halberd": {"Cost": 10, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 12, "Type": "Piercing or Slashing", "Handed": "Two"},
"Lance": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Ranseur": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Piercing", "Handed": "Two"},
"Scythe": {"Cost": 18, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 4, "Weight": 10, "Type": "Piercing or Slashing", "Handed": "Two"},
"Long Bow": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 3, "Type": "Piercing", "Handed": "Two"},
"Short Bow": {"Cost": 30, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 2, "Type": "Piercing", "Handed": "Two"},
"Kama": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Nunchaku": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Sai": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Siangham": {"Cost": 3, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Bastard Sword": {"Cost": 35, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Dwarven Waraxe": {"Cost": 30, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 8, "Type": "Slashing", "Handed": "One"},
"Whip": {"Cost": 1, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Orc Doubleaxe": {"Cost": 60, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 3, "Weight": 15, "Type": "Slashing", "Handed": "Two"},
"Spiked Chain": {"Cost": 25, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Dire Flail": {"Cost": 90, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Gnome Hooked Hammer": {"Cost": 20, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3.5, "Weight": 6, "Type": "Bludgeoning and piercing", "Handed": "Two"},
"Two Bladed Sword": {"Cost": 100, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Dwarven Urgrosh": {"Cost": 50, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3, "Weight": 12, "Type": "Slashing or Piercing", "Handed": "Two"},
"Bolas": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Hand Crossbow": {"Cost": 100, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Heavy Repeating Crossbow": {"Cost": 400, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 12, "Type": "Piercing", "Handed": "One"},
"Light Repeating Crossbow": {"Cost": 250, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Net": {"Cost": 20, "Damage (S)": "0", "Damage (M)": "0", "Critical": 0, "Weight": 6, "Type": "None", "Handed": "Two"},
"Shuriken": {"Cost": 1, "Damage (S)": "1", "Damage (M)": "1d2", "Critical": 2, "Weight": 0.5, "Type": "Piercing", "Handed": "One"},
"Unarmed": {"Cost": 0, "Damage (S)": "1", "Damage (M)": "1", "Critical": 0, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"}
}
armor_data = {
"None": {"Cost": 0, "Armor Bonus": 0, "Max Dex Bonus": 100, "Armor Check": 0, "Arcane Spell Failure": 0, "Weight": 0, "Class": "None"},
"Padded": {"Cost": 5, "Armor Bonus": 1, "Max Dex Bonus": 8, "Armor Check": 0, "Arcane Spell Failure": 5, "Weight": 10, "Class": "Light"},
"Leather": {"Cost": 10, "Armor Bonus": 2, "Max Dex Bonus": 6, "Armor Check": 0, "Arcane Spell Failure": 10, "Weight": 15, "Class": "Light"},
"Padded Leather": {"Cost": 25, "Armor Bonus": 3, "Max Dex Bonus": 5, "Armor Check": -1, "Arcane Spell Failure": 15, "Weight": 20, "Class": "Light"},
"Chain Shirt": {"Cost": 100, "Armor Bonus": 4, "Max Dex Bonus": 4, "Armor Check": -2, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Light"},
"Hide": {"Cost": 15, "Armor Bonus": 3, "Max Dex Bonus": 4, "Armor Check": 3, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Medium"},
"Scalemail": {"Cost": 50, "Armor Bonus": 4, "Max Dex Bonus": 3, "Armor Check": 4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Chainmail": {"Cost": 150, "Armor Bonus": 5, "Max Dex Bonus": 2, "Armor Check": 5, "Arcane Spell Failure": 30, "Weight": 40, "Class": "Medium"},
"Breastplate": {"Cost": 200, "Armor Bonus": 5, "Max Dex Bonus": 3, "Armor Check": -4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Splintmail": {"Cost": 200, "Armor Bonus": 6, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 45, "Class": "Heavy"},
"Bandedmail": {"Cost": 250, "Armor Bonus": 6, "Max Dex Bonus": 1, "Armor Check": 6, "Arcane Spell Failure": 35, "Weight": 35, "Class": "Heavy"},
"Half Plate": {"Cost": 600, "Armor Bonus": 7, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 50, "Class": "Heavy"},
"Buckler": {"Cost": 15, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Wooden": {"Cost": 3, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Steel": {"Cost": 9, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 6, "Class": "Light"},
"Heavy Wooden": {"Cost": 7, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 10, "Class": "Heavy"},
"Heavy Steel": {"Cost": 20, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 15, "Class": "Heavy"}
}

barbarian_armor = ['Padded Leather', 'Padded Leather', 'Chain Shirt', 'Hide', 'Scalemail', 'Chainmail', 'Breastplate']

bard_weapons = ['Whip', 'Long Sword', 'Rapier', 'Sap', 'Short Sword', 'Short Bow', 'Dagger', 'Gauntlet', 'Light Mace', 'Sickle', 'Club', 'Heavy Mace', 'Morningstar', 'Short Spear', 'Long Spear', 'Quarterstaff', 'Spear', 'Heavy Crossbow', 'Light Crossbow', 'Javelin', 'Sling']

dwarf_first_names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik",
"Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
dwarf_last_names = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
dwarf_clans = ["Balderk", "Dankil", "Gorunn", " Holderhek", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
dwarf_skin_tone = ['Deep Tan', 'Pale', 'Beige', 'Light Brown']
dwarf_hair_color = ['Black', 'Brown', 'Grey']
dwarf_hair_type = ['Curly', 'Wavy', 'Straight']
dwarf_eye_color = ['Brown', 'Black', 'Deep Grey']

elf_first_names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias",
"Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
elf_last_names = ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Naïlo", "Siannodel", "Xiloscient"]
elf_skin_tone = ['Light Pale', 'Pale', 'Dark Pale']
elf_hair_color = ['Black', 'Brown', 'Grey']
elf_hair_type= ['Curly', 'Wavy', 'Straight']
elf_eye_color = ['Light Green', 'Green', 'Dark Green', 'Green Grey']

halfling_first_names = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
halfling_last_names = ["Brushgather", "Goodbarrel", "Greenbottle", "Highhill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"]
halfling_skin_tones = ['Light Pale', 'Pale', 'Pink']


gnome_first_names = ["Boddynock", "Dimble", "Fonkin", "Gimble", "Glim", "Gerbo", "Jebeddo", "Namfoodle", "Roondar", "Seebo", "Zook"]
gnome_last_names = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]
gnome_clans = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]
gnome_nick_names = ["Aleslosh", "Ashhearth", "Badger", "Cloak", "Doublelock", "Filchbatter", "Fnipper", "Oneshoe", "Sparklegem", "Stumbleduck"]
gnome_eye_color = ['Light Blue', 'Blue', 'Dark Blue', 'Blue Grey']

orc_first_names = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront", "Shump", "Thokk"]
human_first_names = {
"Calishite": {"Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir"},
"Chondathan": {"Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd"},
"Damaran": {"Bor", "Fodel", "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor"},
"Illuskan": {"Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth"},
"Mulan": {"Aoth", "Bareris", "Ehput Ki", "Kethoth", "Mumed", "Ramas", "So Kehur", "Thazar De", "Urhur"},
"Rashemi": {"Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar", "Vladislak"},
"Shou": {"Chien", "Huang", "Kao", "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum", "Tan", "Wan"},
"Turami": {"Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"}
}
human_last_names = {
"Calishite": {"Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein"},
"Chondathan": {"Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag"},
"Damaran": {"Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag"},
"Illuskan": {"Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind", "Windrivver"},
"Mulan": {"Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"},
"Rashemi": {"Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"},
"Shou": {"An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui", "Wen"},
"Turami": {"Agosto", "Astorio", "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"}
}
human_tribes = ["Calishite", "Chondathan", "Damaran", "Illuskan", "Mulan", "Rashemi", "Shou", "Turami"]
"St. Cuthbert": ["Destruction", "Law", "Protection", "Strength"],
"Vecna": ["Evil", "Knowledge", "Magic"],
"Wee Jas": ["Death", "Law", "Magic"],
"Yondalla": ["Good", "Law", "Protection"],
}
religion_weapons = {"Boccob": "Quarterstaff", "Corellon Larethian": "Long Sword", "Ehlonna": "Long Bow", "Erythnul": "Morningstar", "Fharlanghn": "Quarterstaff", "Garl Glittergold": "Battleaxe", "Gruumsh": "Spear", "Heironeous": "Long Sword", "Hextor": "Flail", "Kord": "Greatsword", "Moradin": "Warhammer", "Nerull": "Scythe", "Obad Hai": "Quarterstaff", "Olidammara": "Rapier", "Pelor": "Heavy Mace", "St. Cuthbert": "Light Mace", "Vecna": "Dagger", "Wee Jas": "Dagger", "Yondalla": "Short Sword"}
religion_alignments = {"Boccob": 5, "Corellon Larethian": 7, "Ehlonna": 4, "Erythnul": 9, "Fharlanghn": 5, "Garl Glittergold": 4, "Gruumsh": 9, "Heironeous": 1, "Hextor": 3, "Kord": 7, "Moradin": 1, "Nerull": 6, "Obad Hai": 5, "Olidammara": 8, "Pelor": 4, "St. Cuthbert": 2, "Vecna": 6, "Wee Jas": 2, "Yondalla": 1}
religion_table = {1: "Lawful Good", 2: "Lawful Neutral", 3: "Lawful Evil", 4: "Neutral Good", 5: "Neutral Neutral", 6: "Neutral Evil", 7: "Chaotic Good", 8: "Chaotic Neutral", 9: "Chaotic Evil"}

familiars = ["Bat", "Cat", "Hawk", "Lizard", "Owl", "Rat", "Raven", "Snake", "Toad", "Weasel"]

language_list = ["Abyssal", "Aquan", "Auran", "Celestial", "Draconic", "Dwarven", "Elven", "Giant", "Gnome", "Goblin", "Gnoll", "Halfling", "Ignan", "Infernal", "Orc", "ylvan", "Terran", "Undercommon"]

weapon_data = {
"Gauntlet": {"Cost": 2, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Dagger": {"Cost": 2, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Spiked Gauntlet": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Light Mace": {"Cost": 5, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "One"},
"Sickle": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Club": {"Cost": 0, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Bludgeoning", "Handed": "One"},
"Heavy Mace": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "One"},
"Morningstar": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning and Piercing", "Handed": "One"},
"Short Spear": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Long Spear": {"Cost": 5, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 9, "Type": "Piercing", "Handed": "Two"},
"Quarterstaff": {"Cost": 0, "Damage (S)": "2d6", "Damage (M)": "2d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "Two"},
"Spear": {"Cost": 2, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Piercing", "Handed": "Two"},
"Heavy Crossbow": {"Cost": 50, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Piercing", "Handed": "One"},
"Light Crossbow": {"Cost": 35, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Javelin": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Sling": {"Cost": 0, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Throwing Axe": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Hammer": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Handaxe": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 3, "Type": "Slashing", "Handed": "One"},
"Kukri": {"Cost": 8, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Pick": {"Cost": 4, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 4, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Sap": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Short Sword": {"Cost": 10, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Battleaxe": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Flail": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Long Sword": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Heavy Pick": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 4, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Rapier": {"Cost": 20, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Scimitar": {"Cost": 15, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Trident": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Warhammer": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Falchion": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Glaive": {"Cost": 8, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Greataxe": {"Cost": 20, "Damage (S)": "1d10", "Damage (M)": "1d12", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Great Club": {"Cost": 5, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "Two"},
"Heavy Flail": {"Cost": 15, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Greatsword": {"Cost": 50, "Damage (S)": "1d10", "Damage (M)": "2d6", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Guisarme": {"Cost": 9, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Halberd": {"Cost": 10, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 12, "Type": "Piercing or Slashing", "Handed": "Two"},
"Lance": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Ranseur": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Piercing", "Handed": "Two"},
"Scythe": {"Cost": 18, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 4, "Weight": 10, "Type": "Piercing or Slashing", "Handed": "Two"},
"Long Bow": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 3, "Type": "Piercing", "Handed": "Two"},
"Short Bow": {"Cost": 30, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 2, "Type": "Piercing", "Handed": "Two"},
"Kama": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Nunchaku": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Sai": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Siangham": {"Cost": 3, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Bastard Sword": {"Cost": 35, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Dwarven Waraxe": {"Cost": 30, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 8, "Type": "Slashing", "Handed": "One"},
"Whip": {"Cost": 1, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Orc Doubleaxe": {"Cost": 60, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 3, "Weight": 15, "Type": "Slashing", "Handed": "Two"},
"Spiked Chain": {"Cost": 25, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Dire Flail": {"Cost": 90, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Gnome Hooked Hammer": {"Cost": 20, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3.5, "Weight": 6, "Type": "Bludgeoning and piercing", "Handed": "Two"},
"Two Bladed Sword": {"Cost": 100, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Dwarven Urgrosh": {"Cost": 50, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3, "Weight": 12, "Type": "Slashing or Piercing", "Handed": "Two"},
"Bolas": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Hand Crossbow": {"Cost": 100, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Heavy Repeating Crossbow": {"Cost": 400, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 12, "Type": "Piercing", "Handed": "One"},
"Light Repeating Crossbow": {"Cost": 250, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Net": {"Cost": 20, "Damage (S)": "0", "Damage (M)": "0", "Critical": 0, "Weight": 6, "Type": "None", "Handed": "Two"},
"Shuriken": {"Cost": 1, "Damage (S)": "1", "Damage (M)": "1d2", "Critical": 2, "Weight": 0.5, "Type": "Piercing", "Handed": "One"},
"Unarmed": {"Cost": 0, "Damage (S)": "1", "Damage (M)": "1", "Critical": 0, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"}
}
armor_data = {
"None": {"Cost": 0, "Armor Bonus": 0, "Max Dex Bonus": 100, "Armor Check": 0, "Arcane Spell Failure": 0, "Weight": 0, "Class": "None"},
"Padded": {"Cost": 5, "Armor Bonus": 1, "Max Dex Bonus": 8, "Armor Check": 0, "Arcane Spell Failure": 5, "Weight": 10, "Class": "Light"},
"Leather": {"Cost": 10, "Armor Bonus": 2, "Max Dex Bonus": 6, "Armor Check": 0, "Arcane Spell Failure": 10, "Weight": 15, "Class": "Light"},
"Padded Leather": {"Cost": 25, "Armor Bonus": 3, "Max Dex Bonus": 5, "Armor Check": -1, "Arcane Spell Failure": 15, "Weight": 20, "Class": "Light"},
"Chain Shirt": {"Cost": 100, "Armor Bonus": 4, "Max Dex Bonus": 4, "Armor Check": -2, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Light"},
"Hide": {"Cost": 15, "Armor Bonus": 3, "Max Dex Bonus": 4, "Armor Check": 3, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Medium"},
"Scalemail": {"Cost": 50, "Armor Bonus": 4, "Max Dex Bonus": 3, "Armor Check": 4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Chainmail": {"Cost": 150, "Armor Bonus": 5, "Max Dex Bonus": 2, "Armor Check": 5, "Arcane Spell Failure": 30, "Weight": 40, "Class": "Medium"},
"Breastplate": {"Cost": 200, "Armor Bonus": 5, "Max Dex Bonus": 3, "Armor Check": -4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Splintmail": {"Cost": 200, "Armor Bonus": 6, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 45, "Class": "Heavy"},
"Bandedmail": {"Cost": 250, "Armor Bonus": 6, "Max Dex Bonus": 1, "Armor Check": 6, "Arcane Spell Failure": 35, "Weight": 35, "Class": "Heavy"},
"Half Plate": {"Cost": 600, "Armor Bonus": 7, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 50, "Class": "Heavy"},
"Buckler": {"Cost": 15, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Wooden": {"Cost": 3, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Steel": {"Cost": 9, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 6, "Class": "Light"},
"Heavy Wooden": {"Cost": 7, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 10, "Class": "Heavy"},
"Heavy Steel": {"Cost": 20, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 15, "Class": "Heavy"}
}

bard_weapons = ['Whip', 'Long Sword', 'Rapier', 'Sap', 'Short Sword', 'Short Bow', 'Dagger', 'Gauntlet', 'Light Mace', 'Sickle', 'Club', 'Heavy Mace', 'Morningstar', 'Short Spear', 'Long Spear', 'Quarterstaff', 'Spear', 'Heavy Crossbow', 'Light Crossbow', 'Javelin', 'Sling']

dwarf_first_names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik",
"Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
dwarf_last_names = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
dwarf_clans = ["Balderk", "Dankil", "Gorunn", " Holderhek", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
dwarf_skin_tone = ['Deep Tan', 'Pale', 'Beige', 'Light Brown']
dwarf_hair_color = ['Black', 'Brown', 'Grey']
dwarf_hair_type = ['Curly', 'Wavy', 'Straight']
dwarf_eye_color = ['Brown', 'Black', 'Deep Grey']

elf_first_names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias",
"Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
elf_last_names = ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Naïlo", "Siannodel", "Xiloscient"]
elf_skin_tone = ['Light Pale', 'Pale', 'Dark Pale']
elf_hair_color = ['Black', 'Brown', 'Grey']
elf_hair_type= ['Curly', 'Wavy', 'Straight']
elf_eye_color = ['Light Green', 'Green', 'Dark Green', 'Green Grey']

halfling_first_names = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
halfling_last_names = ["Brushgather", "Goodbarrel", "Greenbottle", "Highhill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"]
gnome_first_names = ["Boddynock", "Dimble", "Fonkin", "Gimble", "Glim", "Gerbo", "Jebeddo", "Namfoodle", "Roondar", "Seebo", "Zook"]
gnome_last_names = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]
gnome_clans = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]
gnome_nick_names = ["Aleslosh", "Ashhearth", "Badger", "Cloak", "Doublelock", "Filchbatter", "Fnipper", "Oneshoe", "Sparklegem", "Stumbleduck"]
orc_first_names = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront", "Shump", "Thokk"]
human_first_names = {
"Calishite": {"Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir"},
"Chondathan": {"Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd"},
"Damaran": {"Bor", "Fodel", "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor"},
"Illuskan": {"Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth"},
"Mulan": {"Aoth", "Bareris", "Ehput Ki", "Kethoth", "Mumed", "Ramas", "So Kehur", "Thazar De", "Urhur"},
"Rashemi": {"Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar", "Vladislak"},
"Shou": {"Chien", "Huang", "Kao", "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum", "Tan", "Wan"},
"Turami": {"Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"}
}
human_last_names = {
"Calishite": {"Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein"},
"Chondathan": {"Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag"},
"Damaran": {"Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag"},
"Illuskan": {"Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind", "Windrivver"},
"Mulan": {"Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"},
"Rashemi": {"Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"},
"Shou": {"An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui", "Wen"},
"Turami": {"Agosto", "Astorio", "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"}
}
human_tribes = ["Calishite", "Chondathan", "Damaran", "Illuskan", "Mulan", "Rashemi", "Shou", "Turami"]
"St. Cuthbert": ["Destruction", "Law", "Protection", "Strength"],
"Vecna": ["Evil", "Knowledge", "Magic"],
"Wee Jas": ["Death", "Law", "Magic"],
"Yondalla": ["Good", "Law", "Protection"],
}
religion_weapons = {"Boccob": "Quarterstaff", "Corellon Larethian": "Long Sword", "Ehlonna": "Long Bow", "Erythnul": "Morningstar", "Fharlanghn": "Quarterstaff", "Garl Glittergold": "Battleaxe", "Gruumsh": "Spear", "Heironeous": "Long Sword", "Hextor": "Flail", "Kord": "Greatsword", "Moradin": "Warhammer", "Nerull": "Scythe", "Obad Hai": "Quarterstaff", "Olidammara": "Rapier", "Pelor": "Heavy Mace", "St. Cuthbert": "Light Mace", "Vecna": "Dagger", "Wee Jas": "Dagger", "Yondalla": "Short Sword"}
religion_alignments = {"Boccob": 5, "Corellon Larethian": 7, "Ehlonna": 4, "Erythnul": 9, "Fharlanghn": 5, "Garl Glittergold": 4, "Gruumsh": 9, "Heironeous": 1, "Hextor": 3, "Kord": 7, "Moradin": 1, "Nerull": 6, "Obad Hai": 5, "Olidammara": 8, "Pelor": 4, "St. Cuthbert": 2, "Vecna": 6, "Wee Jas": 2, "Yondalla": 1}
religion_table = {1: "Lawful Good", 2: "Lawful Neutral", 3: "Lawful Evil", 4: "Neutral Good", 5: "Neutral Neutral", 6: "Neutral Evil", 7: "Chaotic Good", 8: "Chaotic Neutral", 9: "Chaotic Evil"}

familiars = ["Bat", "Cat", "Hawk", "Lizard", "Owl", "Rat", "Raven", "Snake", "Toad", "Weasel"]

language_list = ["Abyssal", "Aquan", "Auran", "Celestial", "Draconic", "Dwarven", "Elven", "Giant", "Gnome", "Goblin", "Gnoll", "Halfling", "Ignan", "Infernal", "Orc", "ylvan", "Terran", "Undercommon"]

weapon_data = {
"Gauntlet": {"Cost": 2, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Dagger": {"Cost": 2, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Spiked Gauntlet": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Light Mace": {"Cost": 5, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "One"},
"Sickle": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Club": {"Cost": 0, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Bludgeoning", "Handed": "One"},
"Heavy Mace": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "One"},
"Morningstar": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 8, "Type": "Bludgeoning and Piercing", "Handed": "One"},
"Short Spear": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Long Spear": {"Cost": 5, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 9, "Type": "Piercing", "Handed": "Two"},
"Quarterstaff": {"Cost": 0, "Damage (S)": "2d6", "Damage (M)": "2d6", "Critical": 2, "Weight": 4, "Type": "Bludgeoning", "Handed": "Two"},
"Spear": {"Cost": 2, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Piercing", "Handed": "Two"},
"Heavy Crossbow": {"Cost": 50, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Piercing", "Handed": "One"},
"Light Crossbow": {"Cost": 35, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Javelin": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Sling": {"Cost": 0, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Throwing Axe": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Hammer": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Handaxe": {"Cost": 6, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 3, "Type": "Slashing", "Handed": "One"},
"Kukri": {"Cost": 8, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Light Pick": {"Cost": 4, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 4, "Weight": 3, "Type": "Piercing", "Handed": "One"},
"Sap": {"Cost": 1, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Short Sword": {"Cost": 10, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Battleaxe": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Flail": {"Cost": 8, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Long Sword": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Heavy Pick": {"Cost": 8, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 4, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Rapier": {"Cost": 20, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Scimitar": {"Cost": 15, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 4, "Type": "Slashing", "Handed": "One"},
"Trident": {"Cost": 15, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 4, "Type": "Piercing", "Handed": "One"},
"Warhammer": {"Cost": 12, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 5, "Type": "Bludgeoning", "Handed": "One"},
"Falchion": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Glaive": {"Cost": 8, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Greataxe": {"Cost": 20, "Damage (S)": "1d10", "Damage (M)": "1d12", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Great Club": {"Cost": 5, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 8, "Type": "Bludgeoning", "Handed": "Two"},
"Heavy Flail": {"Cost": 15, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Greatsword": {"Cost": 50, "Damage (S)": "1d10", "Damage (M)": "2d6", "Critical": 2, "Weight": 8, "Type": "Slashing", "Handed": "Two"},
"Guisarme": {"Cost": 9, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Slashing", "Handed": "Two"},
"Halberd": {"Cost": 10, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 12, "Type": "Piercing or Slashing", "Handed": "Two"},
"Lance": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Ranseur": {"Cost": 10, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 12, "Type": "Piercing", "Handed": "Two"},
"Scythe": {"Cost": 18, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 4, "Weight": 10, "Type": "Piercing or Slashing", "Handed": "Two"},
"Long Bow": {"Cost": 75, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 3, "Weight": 3, "Type": "Piercing", "Handed": "Two"},
"Short Bow": {"Cost": 30, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 3, "Weight": 2, "Type": "Piercing", "Handed": "Two"},
"Kama": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Nunchaku": {"Cost": 2, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"},
"Sai": {"Cost": 1, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 1, "Type": "Bludgeoning", "Handed": "One"},
"Siangham": {"Cost": 3, "Damage (S)": "1d4", "Damage (M)": "1d6", "Critical": 2, "Weight": 1, "Type": "Piercing", "Handed": "One"},
"Bastard Sword": {"Cost": 35, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 6, "Type": "Slashing", "Handed": "One"},
"Dwarven Waraxe": {"Cost": 30, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 3, "Weight": 8, "Type": "Slashing", "Handed": "One"},
"Whip": {"Cost": 1, "Damage (S)": "1d2", "Damage (M)": "1d3", "Critical": 2, "Weight": 2, "Type": "Slashing", "Handed": "One"},
"Orc Doubleaxe": {"Cost": 60, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 3, "Weight": 15, "Type": "Slashing", "Handed": "Two"},
"Spiked Chain": {"Cost": 25, "Damage (S)": "1d6", "Damage (M)": "2d4", "Critical": 3, "Weight": 10, "Type": "Piercing", "Handed": "Two"},
"Dire Flail": {"Cost": 90, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Bludgeoning", "Handed": "Two"},
"Gnome Hooked Hammer": {"Cost": 20, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3.5, "Weight": 6, "Type": "Bludgeoning and piercing", "Handed": "Two"},
"Two Bladed Sword": {"Cost": 100, "Damage (S)": "2d6", "Damage (M)": "2d8", "Critical": 2, "Weight": 10, "Type": "Slashing", "Handed": "Two"},
"Dwarven Urgrosh": {"Cost": 50, "Damage (S)": "2d5", "Damage (M)": "2d7", "Critical": 3, "Weight": 12, "Type": "Slashing or Piercing", "Handed": "Two"},
"Bolas": {"Cost": 5, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Bludgeoning", "Handed": "One"},
"Hand Crossbow": {"Cost": 100, "Damage (S)": "1d3", "Damage (M)": "1d4", "Critical": 2, "Weight": 2, "Type": "Piercing", "Handed": "One"},
"Heavy Repeating Crossbow": {"Cost": 400, "Damage (S)": "1d8", "Damage (M)": "1d10", "Critical": 2, "Weight": 12, "Type": "Piercing", "Handed": "One"},
"Light Repeating Crossbow": {"Cost": 250, "Damage (S)": "1d6", "Damage (M)": "1d8", "Critical": 2, "Weight": 6, "Type": "Piercing", "Handed": "One"},
"Net": {"Cost": 20, "Damage (S)": "0", "Damage (M)": "0", "Critical": 0, "Weight": 6, "Type": "None", "Handed": "Two"},
"Shuriken": {"Cost": 1, "Damage (S)": "1", "Damage (M)": "1d2", "Critical": 2, "Weight": 0.5, "Type": "Piercing", "Handed": "One"},
"Unarmed": {"Cost": 0, "Damage (S)": "1", "Damage (M)": "1", "Critical": 0, "Weight": 0, "Type": "Bludgeoning", "Handed": "One"}
}
armor_data = {
"None": {"Cost": 0, "Armor Bonus": 0, "Max Dex Bonus": 100, "Armor Check": 0, "Arcane Spell Failure": 0, "Weight": 0, "Class": "None"},
"Padded": {"Cost": 5, "Armor Bonus": 1, "Max Dex Bonus": 8, "Armor Check": 0, "Arcane Spell Failure": 5, "Weight": 10, "Class": "Light"},
"Leather": {"Cost": 10, "Armor Bonus": 2, "Max Dex Bonus": 6, "Armor Check": 0, "Arcane Spell Failure": 10, "Weight": 15, "Class": "Light"},
"Padded Leather": {"Cost": 25, "Armor Bonus": 3, "Max Dex Bonus": 5, "Armor Check": -1, "Arcane Spell Failure": 15, "Weight": 20, "Class": "Light"},
"Chain Shirt": {"Cost": 100, "Armor Bonus": 4, "Max Dex Bonus": 4, "Armor Check": -2, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Light"},
"Hide": {"Cost": 15, "Armor Bonus": 3, "Max Dex Bonus": 4, "Armor Check": 3, "Arcane Spell Failure": 20, "Weight": 25, "Class": "Medium"},
"Scalemail": {"Cost": 50, "Armor Bonus": 4, "Max Dex Bonus": 3, "Armor Check": 4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Chainmail": {"Cost": 150, "Armor Bonus": 5, "Max Dex Bonus": 2, "Armor Check": 5, "Arcane Spell Failure": 30, "Weight": 40, "Class": "Medium"},
"Breastplate": {"Cost": 200, "Armor Bonus": 5, "Max Dex Bonus": 3, "Armor Check": -4, "Arcane Spell Failure": 25, "Weight": 30, "Class": "Medium"},
"Splintmail": {"Cost": 200, "Armor Bonus": 6, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 45, "Class": "Heavy"},
"Bandedmail": {"Cost": 250, "Armor Bonus": 6, "Max Dex Bonus": 1, "Armor Check": 6, "Arcane Spell Failure": 35, "Weight": 35, "Class": "Heavy"},
"Half Plate": {"Cost": 600, "Armor Bonus": 7, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 50, "Class": "Heavy"},
"Buckler": {"Cost": 15, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Wooden": {"Cost": 3, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
"Light Steel": {"Cost": 9, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 6, "Class": "Light"},
"Heavy Wooden": {"Cost": 7, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 10, "Class": "Heavy"},
"Heavy Steel": {"Cost": 20, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 15, "Class": "Heavy"}
}

dwarf_first_names = ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik",
"Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"]
dwarf_last_names = ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
dwarf_clans = ["Balderk", "Dankil", "Gorunn", " Holderhek", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"]
elf_first_names = ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias",
"Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"]
elf_last_names = ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Naïlo", "Siannodel", "Xiloscient"]
halfling_first_names = ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"]
halfling_last_names = ["Brushgather", "Goodbarrel", "Greenbottle", "Highhill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"]
gnome_first_name = ["Boddynock", "Dimble", "Fonkin", "Gimble", "Glim", "Gerbo", "Jebeddo", "Namfoodle", "Roondar", "Seebo", "Zook"]
gnome_last_names = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]
gnome_clans = ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"]
gnome_nick_names = ["Aleslosh", "Ashhearth", "Badger", "Cloak", "Doublelock", "Filchbatter", "Fnipper", "Oneshoe", "Sparklegem", "Stumbleduck"]
orc_first_names = ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront", "Shump", "Thokk"]
human_first_names = {
"Calishite": {"Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir"},
"Chondathan": {"Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd"},
"Damaran": {"Bor", "Fodel", "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor"},
"Illuskan": {"Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth"},
"Mulan": {"Aoth", "Bareris", "Ehput Ki", "Kethoth", "Mumed", "Ramas", "So Kehur", "Thazar De", "Urhur"},
"Rashemi": {"Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar", "Vladislak"},
"Shou": {"Chien", "Huang", "Kao", "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum", "Tan", "Wan"},
"Turami": {"Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"}
}
human_last_names = {
"Calishite": {"Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein"},
"Chondathan": {"Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag"},
"Damaran": {"Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag"},
"Illuskan": {"Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind", "Windrivver"},
"Mulan": {"Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"},
"Rashemi": {"Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"},
"Shou": {"An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui", "Wen"},
"Turami": {"Agosto", "Astorio", "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"}
}
human_tribes = ["Calishite", "Chondathan", "Damaran", "Illuskan", "Mulan", "Rashemi", "Shou", "Turami"]
