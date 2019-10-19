race_list = ["Dwarf", "Elf", "Halfling", "Human", "Gnome", "Half-Elf", "Half-Orc"]
class_list = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Sorcerer", "Rogue", "Wizard"]

align_chart = list(zip(["Lawful", "Neutral", "Chaotic"] * 3, [item for item in [(i, i, i) for i in ["Good", "Neutral", "Evil"]] for item in item]))

weapons = {
    'Gauntlet': {'Cost': '2 gp', 'Dmg (S)': '1d2', 'Dmg (M)': '1d3', 'Critical': '×2', 'Range Increment': '—', 'Weight': '1 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Unarmed Attacks', 'Rarity': 'Simple Weapons'},
    'Unarmed': {'Cost': '—', 'Dmg (S)': '1d2', 'Dmg (M)': '1d3', 'Critical': '×2', 'Range Increment': '—', 'Weight': '—', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Unarmed Attacks', 'Rarity': 'Simple Weapons'},
    'Dagger': {'Cost': '2 gp', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '19-20/×2', 'Range Increment': '10 ft.', 'Weight': '1 lb.', 'Damage Type': 'Piercing or slashing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Gauntlet, spiked': {'Cost': '5 gp', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '×2', 'Range Increment': '—', 'Weight': '1 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Mace, light': {'Cost': '5 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '—', 'Weight': '4 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Sickle': {'Cost': '6 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '—', 'Weight': '2 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Club': {'Cost': '—', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '10 ft.', 'Weight': '3 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Mace, heavy': {'Cost': '12 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×2', 'Range Increment': '—', 'Weight': '8 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Morningstar': {'Cost': '8 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×2', 'Range Increment': '—', 'Weight': '6 lb.', 'Damage Type': 'Bludgeoning and piercing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Shortspear': {'Cost': '1 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '20 ft.', 'Weight': '3 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Longspear': {'Cost': '5 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×3', 'Range Increment': '—', 'Weight': '9 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Quarterstaff': {'Cost': '—', 'Dmg (S)': '1d4/1d4', 'Dmg (M)': '1d6/1d6', 'Critical': '×2', 'Range Increment': '—', 'Weight': '4 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Spear': {'Cost': '2 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×3', 'Range Increment': '20 ft.', 'Weight': '6 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Simple Weapons'},
    'Crossbow, heavy': {'Cost': '50 gp', 'Dmg (S)': '1d8', 'Dmg (M)': '1d10', 'Critical': '19-20/×2', 'Range Increment': '120 ft.', 'Weight': '8 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Simple Weapons'},
    'Crossbow, light': {'Cost': '35 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '19-20/×2', 'Range Increment': '80 ft.', 'Weight': '4 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Simple Weapons'},
    'Dart': {'Cost': '5 sp', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '×2', 'Range Increment': '20 ft.', 'Weight': '1/2 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Simple Weapons'},
    'Javelin': {'Cost': '1 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '30 ft.', 'Weight': '2 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Simple Weapons'},
    'Sling': {'Cost': '—', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '×2', 'Range Increment': '50 ft.', 'Weight': '0 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Simple Weapons'},
    'Axe, throwing': {'Cost': '8 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '10 ft.', 'Weight': '2 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Hammer, light': {'Cost': '1 gp', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '×2', 'Range Increment': '20 ft.', 'Weight': '2 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Handaxe': {'Cost': '6 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×3', 'Range Increment': '—', 'Weight': '3 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Kukri': {'Cost': '8 gp', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '18-20/×2', 'Range Increment': '—', 'Weight': '2 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Pick, light': {'Cost': '4 gp', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '×4', 'Range Increment': '—', 'Weight': '3 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Sap': {'Cost': '1 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '—', 'Weight': '2 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Sword, short': {'Cost': '10 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '19-20/×2', 'Range Increment': '—', 'Weight': '2 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Battleaxe': {'Cost': '10 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×3', 'Range Increment': '—', 'Weight': '6 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Flail': {'Cost': '8 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×2', 'Range Increment': '—', 'Weight': '5 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Longsword': {'Cost': '15 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '19-20/×2', 'Range Increment': '—', 'Weight': '4 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Pick, heavy': {'Cost': '8 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×4', 'Range Increment': '—', 'Weight': '6 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Rapier': {'Cost': '20 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '18-20/×2', 'Range Increment': '—', 'Weight': '2 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Scimitar': {'Cost': '15 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '18-20/×2', 'Range Increment': '—', 'Weight': '4 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Trident': {'Cost': '15 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×2', 'Range Increment': '10 ft.', 'Weight': '4 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Warhammer': {'Cost': '12 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×3', 'Range Increment': '—', 'Weight': '5 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Falchion': {'Cost': '75 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '2d4', 'Critical': '18-20/×2', 'Range Increment': '—', 'Weight': '8 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Glaive': {'Cost': '8 gp', 'Dmg (S)': '1d8', 'Dmg (M)': '1d10', 'Critical': '×3', 'Range Increment': '—', 'Weight': '10 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Greataxe': {'Cost': '20 gp', 'Dmg (S)': '1d10', 'Dmg (M)': '1d12', 'Critical': '×3', 'Range Increment': '—', 'Weight': '12 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Greatclub': {'Cost': '5 gp', 'Dmg (S)': '1d8', 'Dmg (M)': '1d10', 'Critical': '×2', 'Range Increment': '—', 'Weight': '8 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Flail, heavy': {'Cost': '15 gp', 'Dmg (S)': '1d8', 'Dmg (M)': '1d10', 'Critical': '19-20/×2', 'Range Increment': '—', 'Weight': '10 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Greatsword': {'Cost': '50 gp', 'Dmg (S)': '1d10', 'Dmg (M)': '2d6', 'Critical': '19-20/×2', 'Range Increment': '—', 'Weight': '8 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Guisarme': {'Cost': '9 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '2d4', 'Critical': '×3', 'Range Increment': '—', 'Weight': '12 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Halberd': {'Cost': '10 gp', 'Dmg (S)': '1d8', 'Dmg (M)': '1d10', 'Critical': '×3', 'Range Increment': '—', 'Weight': '12 lb.', 'Damage Type': 'Piercing or slashing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Lance': {'Cost': '10 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×3', 'Range Increment': '—', 'Weight': '10 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Ranseur': {'Cost': '10 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '2d4', 'Critical': '×3', 'Range Increment': '—', 'Weight': '12 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Scythe': {'Cost': '18 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '2d4', 'Critical': '×4', 'Range Increment': '—', 'Weight': '10 lb.', 'Damage Type': 'Piercing or slashing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Martial Weapons'},
    'Longbow': {'Cost': '75 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×3', 'Range Increment': '100 ft.', 'Weight': '3 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Martial Weapons'},
    'Longbow, composite': {'Cost': '100 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '×3', 'Range Increment': '110 ft.', 'Weight': '3 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Martial Weapons'},
    'Shortbow': {'Cost': '30 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×3', 'Range Increment': '60 ft.', 'Weight': '2 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Martial Weapons'},
    'Shortbow, composite': {'Cost': '75 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×3', 'Range Increment': '70 ft.', 'Weight': '2 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Martial Weapons'},
    'Kama': {'Cost': '2 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '—', 'Weight': '2 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Nunchaku': {'Cost': '2 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '—', 'Weight': '2 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Sai': {'Cost': '1 gp', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '×2', 'Range Increment': '10 ft.', 'Weight': '1 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Siangham': {'Cost': '3 gp', 'Dmg (S)': '1d4', 'Dmg (M)': '1d6', 'Critical': '×2', 'Range Increment': '—', 'Weight': '1 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Light Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Sword, bastard': {'Cost': '35 gp', 'Dmg (S)': '1d8', 'Dmg (M)': '1d10', 'Critical': '19-20/×2', 'Range Increment': '—', 'Weight': '6 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Waraxe, dwarven': {'Cost': '30 gp', 'Dmg (S)': '1d8', 'Dmg (M)': '1d10', 'Critical': '×3', 'Range Increment': '—', 'Weight': '8 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Whip': {'Cost': '1 gp', 'Dmg (S)': '1d2', 'Dmg (M)': '1d3', 'Critical': '×2', 'Range Increment': '—', 'Weight': '2 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'One-Handed Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Axe, orc double': {'Cost': '60 gp', 'Dmg (S)': '1d6/1d6', 'Dmg (M)': '1d8/1d8', 'Critical': '×3', 'Range Increment': '—', 'Weight': '15 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Chain, spiked': {'Cost': '25 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '2d4', 'Critical': '×2', 'Range Increment': '—', 'Weight': '10 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Flail, dire': {'Cost': '90 gp', 'Dmg (S)': '1d6/1d6', 'Dmg (M)': '1d8/1d8', 'Critical': '×2', 'Range Increment': '—', 'Weight': '10 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Hammer, gnome hooked': {'Cost': '20 gp', 'Dmg (S)': '1d6/1d4', 'Dmg (M)': '1d8/1d6', 'Critical': '×3/×4', 'Range Increment': '—', 'Weight': '6 lb.', 'Damage Type': 'Bludgeoning/Piercing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Sword, two-bladed': {'Cost': '100 gp', 'Dmg (S)': '1d6/1d6', 'Dmg (M)': '1d8/1d8', 'Critical': '19-20/×2', 'Range Increment': '—', 'Weight': '10 lb.', 'Damage Type': 'Slashing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Urgrosh, dwarven': {'Cost': '50 gp', 'Dmg (S)': '1d6/1d4', 'Dmg (M)': '1d8/1d6', 'Critical': '×3', 'Range Increment': '—', 'Weight': '12 lb.', 'Damage Type': 'Slashing or piercing', 'Weapon Type': 'Two-Handed Melee Weapons', 'Rarity': 'Exotic Weapons'},
    'Bolas': {'Cost': '5 gp', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '×2', 'Range Increment': '10 ft.', 'Weight': '2 lb.', 'Damage Type': 'Bludgeoning', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Exotic Weapons'},
    'Crossbow, hand': {'Cost': '100 gp', 'Dmg (S)': '1d3', 'Dmg (M)': '1d4', 'Critical': '19-20/×2', 'Range Increment': '30 ft.', 'Weight': '2 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Exotic Weapons'},
    'Crossbow, repeating heavy': {'Cost': '400 gp', 'Dmg (S)': '1d8', 'Dmg (M)': '1d10', 'Critical': '19-20/×2', 'Range Increment': '120 ft.', 'Weight': '12 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Exotic Weapons'},
    'Crossbow, repeating light': {'Cost': '250 gp', 'Dmg (S)': '1d6', 'Dmg (M)': '1d8', 'Critical': '19-20/×2', 'Range Increment': '80 ft.', 'Weight': '6 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Exotic Weapons'},
    'Net': {'Cost': '20 gp', 'Dmg (S)': '—', 'Dmg (M)': '—', 'Critical': '—', 'Range Increment': '10 ft.', 'Weight': '6 lb.', 'Damage Type': '—', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Exotic Weapons'},
    'Shuriken': {'Cost': '1 gp', 'Dmg (S)': '1', 'Dmg (M)': '1d2', 'Critical': '×2', 'Range Increment': '10 ft.', 'Weight': '1/2 lb.', 'Damage Type': 'Piercing', 'Weapon Type': 'Ranged Weapons', 'Rarity': 'Exotic Weapons'}}

feats = ["Acrobatic", "Agile", "Alertness", "Animal Affinity", "Armor Proficency", "Athletic", "Blind Fight", "Combat Casting", "Combat Reflexes", "Deceitful", "Deft Hands", "Diligent", "Endurance", "Eschew Materials", "Great Fortitude", "Improved Counterspell", "Improved Initiative", "Improved Unarmed Strike", "Investigator", "Iron Will", "Lightning Reflexes", "Magical Aptitude", "Martial Weapon Proficency", "Negotiator", "Nimble Fingers", "Persuasive", "Point Blank Shot", "Run", "Self Sufficent", "Skill Focus", "Spell Focus", "Spell Penetration", "Stealthy", "Toughness", "Track"]

deities = {
    "Boccob": {'domains': ["Knowledge", "Magic", "Trickery"], 'weapon': 'Quarterstaff', 'alignment': 5},
    "Corellon Larethian": {'domains': ["Chaos", "Good", "Protection", "War"], 'weapon': 'Longsword', 'alignment': 7},
    "Ehlonna": {'domains': ["Animal", "Good", "Plant", "Sun"], 'weapon': 'Longbow', 'alignment': 4},
    "Erythnul": {'domains': ["Chaos", "Evil", "Trickery", "War"], 'weapon': 'Morningstar', 'alignment': 9},
    "Fharlanghn": {'domains': ["Luck", "Protection", "Travel"], 'weapon': 'Quarterstaff', 'alignment': 5},
    "Garl Glittergold": {'domains': ["Good", "Protection", "Trickery"], 'weapon': 'Battleaxe', 'alignment': 4},
    "Gruumsh": {'domains': ["Chaos", "Evil", "Strength"], 'weapon': 'Spear', 'alignment': 9},
    "Heironeous": {'domains': ["Good", "Law", "War"], 'weapon': 'Longsword', 'alignment': 1},
    "Hextor": {'domains': ["Destruction", "Evil", "Law", "War"], 'weapon': 'Flail', 'alignment': 3},
    "Kord": {'domains': ["Chaos", "Good Luck", "Strength"], 'weapon': 'Greatsword', 'alignment': 7},
    "Moradin": {'domains': ["Earth", "Good", "Law", "Protection"], 'weapon': 'Warhammer', 'alignment': 1},
    "Nerull": {'domains': ["Death", "Evil", "Trickery"], 'weapon': 'Scythe', 'alignment': 6},
    "Obad Hai": {'domains': ["Air", "Animal", "Earth", "Fire", "Plant", "Water"], 'weapon': 'Quarterstaff', 'alignment': 5},
    "Olidammara": {'domains': ["Chaos", "Luck", "Trickery"], 'weapon': 'Rapier', 'alignment': 8},
    "Pelor": {'domains': ["Good", "Healing", "Strength"], 'weapon': 'Mace, heavy', 'alignment': 4},
    "St. Cuthbert": {'domains': ["Destruction", "Law", "Protection", "Strength"], 'weapon': 'Mace, light', 'alignment': 2},
    "Vecna": {'domains': ["Evil", "Knowledge", "Magic"], 'weapon': 'Dagger', 'alignment': 6},
    "Wee Jas": {'domains': ["Death", "Law", "Magic"], 'weapon': 'Dagger', 'alignment': 2},
    "Yondalla": {'domains': ["Good", "Law", "Protection"], 'weapon': 'Sword, short', 'alignment': 1}
}
classes = {
    'Barbarian': {
        'armor': ['Padded Leather', 'Padded Leather', 'Chain Shirt', 'Hide', 'Scalemail', 'Chainmail', 'Breastplate'],
        'skills': ["Climb", "Craft", "Handle Animal", "Intimidate", "Jump", "Listen", "Ride", "Survival", "Swim"],
        'health': 12,
        'xp': 4,
        'gold': '4d4',
        'deities': ['Kord', 'Obad Hai', 'Erythnul']
    },

    'Bard': {
        'weapons': ['Whip', 'Longsword', 'Rapier', 'Sap', 'Sword, short', 'Shortbow', 'Dagger', 'Gauntlet', 'Mace, light', 'Sickle', 'Club', 'Mace, heavy', 'Morningstar', 'Shortspear', 'Longspear', 'Quarterstaff', 'Spear', 'Crossbow, repeating heavy', 'Crossbow, repeating light', 'Javelin', 'Sling'],
        'skills': ["Appraise", "Balance", "Bluff", "Climb", "Concentration", "Craft", "Decipher Script", "Diplomacy", "Disguise", "Escape Artist", "Gather Information", "Hide", "Intimidate", "Jump", "Knowledge (arcana)", "Knowledge (architecture and engineering)", "Knowledge (dungeoneering)", "Knowledge (geography)", "Knowledge (history)", "Knowledge (local)", "Knowledge (nature)", "Knowledge (nobility and royalty)", "Knowledge (religion)", "Knowledge (the planes)", "Listen", "Move Silently", "Perform", "Profession", "Ride", "Search", "Sense Motive", "Sleight of Hand", "Speak Language", "Spellcraft", "Swim", "Tumble", "Use Magic Device"],
        'health': 6,
        'xp': 6,
        'gold': '4d4'
    },

    'Cleric': {
        'armor': ['Padded', 'Leather', 'Padded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Chainmail', 'Breastplate', 'Splintmail', 'Bandedmail', 'Half Plate'],
        'skills': ["Concentration", "Craft", "Diplomacy", "Heal", "Knowledge (arcana)", "Knowledge (history)", "Knowledge (religion)", "Knowledge (the planes)", "Profession", "Spellcraft"],
        'health': 8,
        'xp': 2,
        'alignment': [[1], [1, 2, 3, 5], [3], [1, 4, 5, 7], [2, 4, 5, 6, 8], [3, 5, 6, 9], [7], [5, 7, 8, 9], [9]],
        'gold': '5d4',
        'languages': ['Celestial', 'Abyssal', 'Infernal']
    },

    'Druid': {
        'weapons': ['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Shortspear', 'Sling', 'Longspear'],
        'companions': ['Badger', 'Camel', 'Dire Rat', 'Dog', 'Riding Dog', 'Eagle', 'Hawk', 'Light Horse', 'Heavy Horse', 'Owl', 'Pony', 'Small Snake', 'Medium Snake', 'Viper', 'Wolf'],
        'health': 8,
        'xp': 4,
        'skills': ["Concentration", "Craft", "Diplomacy", "Handle Animal", "Heal", "Knowledge (nature)", "Listen", "Profession", "Ride", "Spellcraft", "Spot", "Survival", "Swim"],
        'languages': ['Druidic', 'Sylvan'],
        'armor': ['Padded', 'Leather', 'Hide'],
        'alignment': [2, 4, 5, 6, 8],
        'gold': '2d4'

    },

    'Fighter': {
        'skills': ["Climb", "Craft", "Handle Animal", "Intimidate", "Jump", "Ride", "Swim"],
        'deities': ['Heironeous', 'Kord', 'St. Cuthbert', 'Hextor', 'Erythnul'],
        'health': 10,
        'xp': 2,
        'gold': '6d4'

    },

    'Monk': {
        'weapons': ['Club', 'Crossbow, repeating light', 'Crossbow, heavy', 'Dagger', 'Handaxe', 'Javelin', 'Kama', 'Nunchaku', 'Quarterstaff', 'Sai', 'Shuriken', 'Siangham', 'Sling'],
        'health': 8,
        'xp': 4,
        'feats': ['Improved Grapple', 'Stunning Fist'],
        'skills': ["Balance", "Climb", "Concentration", "Craft", "Diplomacy", "Escape Artist", "Hide", "Jump", "Knowledge (arcana)", "Knowledge (religion)", "Listen", "Move Silently", "Perform", "Profession", "Sense Motive", "Spot", "Swim", "Tumble"],
        'gold': '5d4'

    },

    'Paladin': {
        'skills': ["Concentration", "Craft", "Diplomacy", "Handle Animal", "Heal", "Knowledge (nobility and royalty)", "Knowledge (religion)", "Profession", "Ride", "Sense Motive", "Spot", "Swim", "Tumble"],
        'health': 10,
        'xp': 2,
        'gold': '6d4'
    },

    'Ranger': {
        'favored enemies': ['Aberration', 'Animal', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Giant', 'Humanoid (aquatic)', 'Humanoid (dwarf)', 'Humanoid (elf)', 'Humanoid (goblinoid)', 'Humanoid (gnoll)', 'Humanoid (gnome)', 'Humanoid (halfling)', 'Humanoid (human)', 'Humanoid (orc)', 'Humanoid (reptilian)', 'Magical beast', 'Monstrous humanoid', 'Ooze', 'Outsider (air)', 'Outsider (chaotic)', 'Outsider (earth)', 'Outsider (evil)', 'Outsider (fire)', 'Outsider (good)', 'Outsider (lawful)', 'Outsider (native)', 'Outsider (water)', 'Plant', 'Undead', 'Vermin'],
        'skills': ["Climb", "Concentration", "Craft", "Handle Animal", "Heal", "Hide", "Jump", "Knowledge (local)", "Listen", "Move Silently", "Profession", "Ride", "Search", "Spot", "Survival", "Swim", "Use Rope"],
        'health': 8,
        'xp': 6,
        'gold': '6d4'

    },

    'Rogue': {
        'weapons': ['Crossbow, hand', 'Sap', 'Shortbow', 'Rapier', 'Sword, short', 'Club', 'Dagger', 'Javelin', 'Mace, light', 'Mace, heavy', 'Shortspear', 'Sickle', 'Spear', 'Gauntlet, spiked', 'Greatclub', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Crossbow, repeating light', 'Crossbow, repeating heavy'],
        'health': 6,
        'xp': 8,
        'skills': ["Appraise", "Balance", "Bluff", "Climb", "Craft", "Decipher Script", "Diplomacy", "Disable Device", "Disguise", "Escape Artist", "Forgery", "Gather Information", "Hide", "Intimidate", "Jump", "Knowledge (local)", "Listen", "Move Silently", "Open Lock", "Perform", "Profession", "Search", "Sense Motive", "Sleight of Hand", "Spot", "Swim", "Tumble", "Use Magic Device", "Use Rope"],
        'gold': '5d4'
    },

    'Sorcerer': {
        'skills': ["Bluff", "Concentration", "Craft", "Knowledge (arcana)", "Profession", "Spellcraft"],
        'health': 4,
        'xp': 2,
        'gold': '3d4'

    },

    'Wizard': {
        'weapons': ['Club', 'Dagger', 'Crossbow, repeating heavy', 'Crossbow, repeating light', 'Quarterstaff'],
        'health': 4,
        'xp': 2,
        'skills': ["Concentration", "Craft", "Decipher Script", "Knowledge (Arcana)", "Knowledge (Architecture and Engineering)", "Knowledge (Dungeoneering)", "Knowledge (Geography)", "Knowledge (History)", "Knowledge (Local)", "Knowledge (Nature)", "Knowledge (Nobility and Royalty)", "Knowledge (Religion)", "Knowledge (The Planes)", "Spellcraft", "Profession"],
        'schools': ['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'],
        'gold': '3d4'
    }
}
familiars = ["Bat", "Cat", "Hawk", "Lizard", "Owl", "Rat", "Raven", "Snake", "Toad", "Weasel"]

languages = ["Abyssal", "Aquan", "Auran", "Celestial", "Draconic", "Dwarven", "Elven", "Giant", "Gnome", "Goblin", "Gnoll", "Halfling", "Ignan", "Infernal", "Orc", "ylvan", "Terran", "Undercommon"]


armor = {
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
    "Half Plate": {"Cost": 600, "Armor Bonus": 7, "Max Dex Bonus": 0, "Armor Check": 7, "Arcane Spell Failure": 40, "Weight": 50, "Class": "Heavy"}}

shields = {
    "None": {"Cost": 0, "Armor Bonus": 0, "Max Dex Bonus": 100, "Armor Check": 0, "Arcane Spell Failure": 0, "Weight": 0, "Class": "None"},
    "Buckler": {"Cost": 15, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
    "Light Wooden": {"Cost": 3, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 5, "Class": "Light"},
    "Light Steel": {"Cost": 9, "Armor Bonus": 1, "Armor Check": 1, "Arcane Spell Failure": 5, "Weight": 6, "Class": "Light"},
    "Heavy Wooden": {"Cost": 7, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 10, "Class": "Heavy"},
    "Heavy Steel": {"Cost": 20, "Armor Bonus": 2, "Armor Check": 12, "Arcane Spell Failure": 15, "Weight": 15, "Class": "Heavy"}
}

skin_tones = ['Black', 'Brown', 'Beige', 'White', 'Pink', 'Tan', 'Olive', 'Grey']
hair_colors = ['Black', 'Brown', 'Blond', 'Red', 'White', 'Grey']
hair_types = ['Curly', 'Wavy', 'Straight', 'Flowing', 'Frizzy', 'Spiky', 'Touseled', 'Unkempt']
eye_colors = ['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel']

races = {
    'Human': {
        'first names': {
            "Calishite": ["Aseir", "Bardeid", "Haseid", "Khemed", "Mehmen", "Sudeiman", "Zasheir"],
            "Chondathan": ["Darvin", "Dorn", "Evendur", "Gorstag", "Grim", "Helm", "Malark", "Morn", "Randal", "Stedd"],
            "Damaran": ["Bor", "Fodel", "Glar", "Grigor", "Igan", "Ivor", "Kosef", "Mival", "Orel", "Pavel", "Sergor"],
            "Illuskan": ["Ander", "Blath", "Bran", "Frath", "Geth", "Lander", "Luth", "Malcer", "Stor", "Taman", "Urth"],
            "Mulan": ["Aoth", "Bareris", "Ehput Ki", "Kethoth", "Mumed", "Ramas", "So Kehur", "Thazar De", "Urhur"],
            "Rashemi": ["Borivik", "Faurgar", "Jandar", "Kanithar", "Madislak", "Ralmevik", "Shaumar", "Vladislak"],
            "Shou": ["Chien", "Huang", "Kao", "Kung", "Lao", "Ling", "Mei", "Pin", "Shin", "Sum", "Tan", "Wan"],
            "Turami": ["Anton", "Diero", "Marcon", "Pieron", "Rimardo", "Romero", "Salazar", "Umbero"]
        },
        'last_names': {
            "Calishite": ["Basha", "Dumein", "Jassan", "Khalid", "Mostana", "Pashar", "Rein"],
            "Chondathan": ["Amblecrown", "Buckman", "Dundragon", "Evenwood", "Greycastle", "Tallstag"],
            "Damaran": ["Bersk", "Chernin", "Dotsk", "Kulenov", "Marsk", "Nemetsk", "Shemov", "Starag"],
            "Illuskan": ["Brightwood", "Helder", "Hornraven", "Lackman", "Stormwind", "Windrivver"],
            "Mulan": ["Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"],
            "Rashemi": ["Ankhalab", "Anskuld", "Fezim", "Hahpet", "Nathandem", "Sepret", "Uuthrakt"],
            "Shou": ["An", "Chen", "Chi", "Fai", "Jiang", "Jun", "Lian", "Long", "Meng", "On", "Shan", "Shui", "Wen"],
            "Turami": ["Agosto", "Astorio", "Calabra", "Domine", "Falone", "Marivaldi", "Pisacar", "Ramondo"]
        },
        'tribes': ["Calishite", "Chondathan", "Damaran", "Illuskan", "Mulan", "Rashemi", "Shou", "Turami"],
        'age': (15, '1d6'),
        'height': (58, '2d4'),
        'weight': (120, '2d6'),
        'size': 'Medium',
        'deity': 'Pelor'
    },

    'Elf': {
        'first names': ["Adran", "Aelar", "Aramil", "Arannis", "Aust", "Beiro", "Berrian", "Carric", "Enialis", "Erdan", "Erevan", "Galinndan", "Hadarai", "Heian", "Himo", "Immeral", "Ivellios", "Laucian", "Mindartis", "Paelias",
                        "Peren", "Quarion", "Riardon", "Rolen", "Soveliss", "Thamior", "Tharivol", "Theren", "Varis"],
        'last names': ["Amakiir", "Amastacia", "Galanodel", "Holimion", "Ilphelkiir", "Liadon", "Meliamne", "Naïlo", "Siannodel", "Xiloscient"],
        'age': (110, '6d6'),
        'height': (58, '2d6'),
        'weight': (85, '1d6'),
        'size': 'Medium',
        'deity': 'Corellon Larethian',
        'dex': 2,
        'con': -2,
        'language': 'Elven'
    },

    'Gnome': {
        'first names': ["Boddynock", "Dimble", "Fonkin", "Gimble", "Glim", "Gerbo", "Jebeddo", "Namfoodle", "Roondar", "Seebo", "Zook"],
        'last names': ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"],
        'clans': ["Beren", "Daergel", "Folkor", "Garrick", "Nackle", "Murnig", "Ningel", "Raulnor", "Scheppen", "Turen"],
        'nick names': ["Aleslosh", "Ashhearth", "Badger", "Cloak", "Doublelock", "Filchbatter", "Fnipper", "Oneshoe", "Sparklegem", "Stumbleduck"],
        'age': (40, '6d6'),
        'height': (36, '2d4'),
        'weight': (40, '1d6'),
        'size': 'Small',
        'deity': 'Garl Glittergold',
        'con': 2,
        'str': -2,
        'language': 'Gnomish'
    },

    'Orc': {
        'first names': ["Dench", "Feng", "Gell", "Henk", "Holg", "Imsh", "Keth", "Krusk", "Ront", "Shump", "Thokk"],
        'age': (15, '1d6'),
        'height': (58, '2d4'),
        'weight': (120, '2d6'),
        'size': 'Medium',
        'deity': 'Gruumsh',
        'language': 'Orc'
    },

    'Halfling': {
        'first names': ["Alton", "Ander", "Cade", "Corrin", "Eldon", "Errich", "Finnan", "Garret", "Lindal", "Lyle", "Merric", "Milo", "Osborn", "Perrin", "Reed", "Roscoe", "Wellby"],
        'last names': ["Brushgather", "Goodbarrel", "Greenbottle", "Highhill", "Hilltopple", "Leagallow", "Tealeaf", "Thorngage", "Tosscobble", "Underbough"],
        'age': (20, '3d6'),
        'height': (32, '2d4'),
        'weight': (30, '1d1'),
        'size': 'Small',
        'deity': 'Yondalla',
        'dex': 2,
        'str': -2,
        'language': 'Halfling'
    },

    'Dwarf': {
        'first names': ["Adrik", "Alberich", "Baern", "Barendd", "Brottor", "Bruenor", "Dain", "Darrak", "Delg", "Eberk", "Einkil", "Fargrim", "Flint", "Gardain", "Harbek", "Kildrak", "Morgran", "Orsik", "Oskar", "Rangrim", "Rurik",
                             "Taklinn", "Thoradin", "Thorin", "Tordek", "Traubon", "Travok", "Ulfgar", "Veit", "Vondal"],
        'last names': ["Balderk", "Battlehammer", "Brawnanvil", "Dankil", "Fireforge", "Frostbeard", "Gorunn", "Holderhek", "Ironfist", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"],
        'clans': ["Balderk", "Dankil", "Gorunn", " Holderhek", "Loderr", "Lutgehr", "Rumnaheim", "Strakeln", "Torunn", "Ungart"],
        'age': (40, '5d6'),
        'height': (45, '2d4'),
        'weight': (130, '2d6'),
        'size': 'Medium',
        'deity': 'Moradin',
        'con': 2,
        'cha': -2,
        'language': 'Dwarven'

    },
    'Half-Elf': {
        'age': (20, '2d6'),
        'height': (55, '2d8'),
        'weight': (100, '2d4'),
        'size': 'Medium',
        'language': 'Elf'
    },
    'Half-Orc': {
        'age': (14, '1d6'),
        'height': (58, '2d12'),
        'weight': (150, '2d6'),
        'size': 'Medium',
        'int': 2,
        'cha': -2,
        'str': -2,
        'language': 'Orc'
    },
}
