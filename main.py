import random
from Data import *
from console import clear
input_class = str()
input_race = str()

def list_to_string(list):
	return ', '.join(str(x) for x in list)

def get_info(): #grabs info from the user
	clear()
	user_input = str.title(input('Select a Race\n({})\n\n[Enter] for random'.format(list_to_string(race_list))))
	if len(user_input.split()) == 3:
		input_race = user_input.split()[0] + ' ' + user_input.split()[1]
		input_class = user_input.split()[2]
	elif len(user_input.split()) == 2:
		if 'Half ' in user_input:
			input_race = user_input
			clear()
			input_class = str.title(input('Select a Class\n({})'.format(list_to_string(class_list))))
		else:
			input_race = user_input.split()[0]
			input_class = user_input.split()[1]
	elif len(user_input.split()) == 1:
		input_race = user_input
		clear()
		input_class = str.title(input('Select a Class\n({})'.format(list_to_string(class_list))))
	else:
		input_race = random.choice(race_list)
		input_class = random.choice(class_list)
	if input_race not in race_list or input_class not in class_list: get_info()
	return str((input_race + '.' + input_class))
	
		
def generate(user_race, user_class): #uses inout to create character
	user_skills = []
	user_feats = []
	user_domains = []
	user_forbidden_schools = []
	user_languages = ['Common']
	ud = {}
	
	def pb(skill): """returns the Point Bonus of a skill"""
		return (ud[skill] - 10) // 2
	
	def add_lang(): """adds another language to user_languages, and ensures it isn't a duplicate"""
		user_languages.append(random.choice(language_list))
		while len(user_languages) != len(set(user_languages)):
			del user_languages[-1]
			user_languages.append(random.choice(language_list))
			
	
	def add_feat(): """adds another feat to user_feats, and ensures it isn't a duplicate"""
		user_feats.append(random.choice(feats))
		while len(user_feats) != len(set(user_feats)):
			del user_feats[-1]
			user_feats.append(random.choice(feats))
	
	if user_race == 'Dwarf':
		ud['Name'] = random.choice(dwarf_first_names) + ' ' + random.choice(dwarf_last_names) + ', of the clan ' + random.choice(dwarf_clans)
		if random.random() > 0.8:
			ud['Religion'] = 'Moradin'
		ud['Age'] = random.randint(40, 140)
		ud['Height'] = random.randint(48, 56)
		ud['Weight'] = 130 + (ud['Height'] - 57) * random.randint(2, 12)
		ud['con'] = random.randint(10, 20)
		ud['cha'] = random.randint(6, 16)
		user_languages.append('Dwarven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(dwarf_skin_tone)
		ud['Hair Color'] = random.choice(dwarf_hair_color)
		ud['Hair Type'] = random.choice(dwarf_hair_type)
		ud['Eye Color'] = random.choice(dwarf_eye_color)
		
	if user_race == 'Elf':
		ud['Name'] = random.choice(elf_first_names) + ' ' + random.choice(elf_last_names)
		if random.random() > 0.8:
			ud['Religion'] = 'Corellon Larethian'
		ud['Age'] = random.randint(110, 180)
		ud['Height'] = random.randint(55, 65)
		ud['Weight'] = 85 + (ud['Height'] - 52) * random.randint(1, 6)
		ud['dex'] = random.randint(10, 20)
		ud['con'] = random.randint(6, 16)
		user_languages.append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Dark Pale'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Light Green', 'Green', 'Dark Green', 'Green Grey'])
		
	if user_race == 'Halfling':
		ud['Name'] = random.choice(halfling_first_names) + ' ' + random.choice(halfling_last_names)
		if random.random() > 0.7:
			ud['Alignment'] = 'Neutral ' + random.choice(alignment2)
		ud['Age'] = random.randint(22, 30)
		ud['Height'] = random.randint(30, 32)
		ud['Weight'] = random.randint(34, 40)
		ud['dex'] = random.randint(10, 20)
		ud['str'] = random.randint(6, 16)
		user_languages.append('Halfling')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Pink'])
		ud['Hair Color'] = 'Black'
		ud['Hair Type'] = 'Straight'
		ud['Eye Color'] = random.choice(['Brown', 'Black'])
			
	if user_race == 'Gnome':
		ud['Name'] = random.choice(gnome_first_name) + ' ' + random.choice(gnome_nick_names) + ' ' + random.choice(gnome_last_names) + ' of the clan ' + random.choice(gnome_clans)
		if random.random() > 0.4:
			ud['Alignment'] = random.choice(alignment1) + 'Good'
		ud['Age'] = random.randint(40, 250)
		ud['Height'] = random.randint(36, 42)
		ud['Weight'] = random.randint(40, 45)
		ud['con'] = random.randint(10, 20)
		ud['str'] = random.randint(6, 16)
		user_languages.append('Gnome')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(['Deep Tan', 'Woody Brown'])
		ud['Hair Color'] = random.choice(['Blonde', 'White', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Light Blue', 'Blue', 'Dark Blue', 'Blue Grey'])
		
	if user_race == 'Half Elf':
		ud['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			ud['Name'] = random.sample(human_first_names[ud['Tribe']], 1)
		else:
			ud['Name'] = random.sample(elf_first_names, 1)
		if random.random() > 0.5:
			ud['Name'] += random.sample(human_first_names[ud['Tribe']], 1)
		else:
			ud['Name'] += random.sample(elf_last_names, 1)
		ud['Name'] = ' '.join(str(x) for x in ud['Name'])
		if random.random() > 0.5:
			ud['Name'] += ' of the clan ' + ud['Tribe']
		ud['Age'] = random.randint(20, 180)
		ud['Height'] = random.randint(68, 73)
		ud['Weight'] = random.randint(100, 180)
		user_languages.append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Brown', 'Beige', 'White', 'Pink'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
	if user_race == 'Half Orc':
		ud['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			ud['Name'] = random.sample(orc_first_names, 1)
		else:
			ud['Name'] = random.sample(human_first_names[ud['Tribe']], 1)
		if random.random() > 0.7:
			ud['Alignment'] = random.choice(alignment1) + 'Evil'
			ud['Name'] += random.sample(human_first_names[ud['Tribe']], 1)
		ud['Name'] = ' '.join(str(x) for x in ud['Name'])
		if random.random() > 0.8:
			ud['Name'] += ' of the clan ' + random.choice(human_tribes)
		ud['Age'] = random.randint(15, 40)
		ud['Height'] = random.randint(72, 84)
		ud['Weight'] = random.randint(180, 250)
		ud['int'] = random.randint(6, 16)
		ud['cha'] = random.randint(6, 16)
		ud['str'] = random.randint(10, 20)
		user_languages.append('Orc')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Black', 'Brown', 'Grey', 'White'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
		
	if user_race == 'Human':
		ud['Tribe'] = random.choice(human_tribes)
		ud['Age'] = random.randint(18, 30)
		ud['Height'] = random.randint(60, 80)
		ud['Weight'] = 120 + (ud['Height'] - 58) * random.randint(2, 8)
		ud['Name'] = ' '.join(str(x) for x in random.sample(human_first_names[ud['Tribe']], 1) + random.sample(human_last_names[ud['Tribe']], 1)) + ', of the clan ' + ud['Tribe']
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Black', 'Brown', 'Beige', 'White', 'Pink'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		add_lang()
	
	"""since some races have modifiers for stats, so those are set  with thw other race data. to save space, the following statements writes all of the stats that werent previously set"""
	ud.setdefault('str', random.randint(8, 18))
	ud.setdefault('dex', random.randint(8, 18))
	ud.setdefault('con', random.randint(8, 18))
	ud.setdefault('cha', random.randint(8, 18))
	ud.setdefault('int', random.randint(8, 18))
	ud.setdefault('wis', random.randint(8, 18))
	#these variables are needed for class stuff, so theyre set beforehand
	skill_points = class_xp[user_class] + pb('int')
	ud['Health'] = class_health[user_class] + pb('con')
	
	if user_class == 'Barbarian':
		ud['Weapon'] = random.choice(melee_weapons)
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(['Padded Leather', 'Padded Leather', 'Chain Shirt', 'Hide', 'Scalemail', 'Chainmail', 'Breastplate'])
		ud['Alignment'] = random.choice(alignment1[0:2]) + random.choice(alignment2)
		if random.random() > 0.3:
			ud['Religion'] = 'Kord'
			if random.random() > 0.6:
				ud['Religion'] = 'Obad Hai'
				if random.random() > 0.9:
					ud['Religion'] = 'Erythnul'
		ud['Gold'] = random.randint(40, 160)
	
	if user_class == 'Bard':
		ud['Weapon'] = random.choice(['Whip', 'Long Sword', 'Rapier', 'Sap', 'Short Sword', 'Short Bow', 'Dagger', 'Gauntlet', 'Light Mace', 'Sickle', 'Club', 'Heavy Mace', 'Morningstar', 'Short Spear', 'Long Spear', 'Quarterstaff', 'Spear', 'Heavy Crossbow', 'Light Crossbow', 'Javelin', 'Sling'])
		ud['Shield'] = shields[random.randint(0, 3)]
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Chain Shirt'])
		ud['Alignment'] = random.choice(['Neutral ', 'Chaotic ']) + random.choice(alignment2)
		if 'Chaotic' in ud['Alignment']:
			ud['Religion'] = 'Olidammara'
		elif random.random() > 0.5:
			ud['Religion'] = 'Pelor'
		elif random.random() > 0.5:
			ud['Religion'] = 'Corellon Larethian'
		ud['Gold'] = random.randint(40, 160)

"""in dnd, the religion of a cleric can be one "tile" away from their god's religion. this segment figures which alignment to land on. 1 is lawful good, 9 is chaotic evil"""

	if user_class == 'Cleric':
		ud['Religion'] = random.choice(religions)
		x = religion_alignments[ud['Religion']]
		if x % 3 != 0 and (x + 1) < 10 and random.random() > 0.5:
			x += 1
		elif (x + 3) < 10 and random.random() > 0.5:
			x += 3
		else:
			if x % 3 != 0 and (x - 1) > 0 and random.random() > 0.5:
				x -= 1
			elif (x - 3) > 0 and random.random() > 0.5:
				x -= 3
		ud['Alignment'] = religion_table[x]
		ud['Weapon'] = religion_weapons[ud['Religion']]
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Chainmail', 'Breastplate', 'Splintmail', 'Bandedmail', 'Half Plate'])
		ud['Shield'] = random.choice(shields)
		user_domains = random.sample(religion_domains[ud['Religion']], 2)
		user_languages.append(random.choice(['Celestial', 'Abyssal', 'Infernal']))
		if 'War' in user_domains:
			user_feats.append('Weapon Focus')
		ud['Gold'] = random.randint(50, 200)
		
	if user_class == 'Druid':
		if random.random() > 0.5:
			ud['Shield'] = 'Light Wooden'
			ud['Weapon'] = 'Unarmed'
		else:
			ud['Shield'] = 'Heavy Wooden'
			ud['Weapon'] = random.choice(['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Short Spear', 'Sling', 'Spear'])
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Hide'])
		if random.random() > 0.8:
			if random.random() > 0.5:
				ud['Religion'] = 'Obad Hai'
			else:
				ud['Religion'] = 'Ehlonna'
				ud['Alignment'] = random.choice(['Neutral Good', 'Chaotic Neutral', 'Neutral Evil', 'Lawful Neutral', 'Neutral Neutral'])
		user_languages.append('Druidic')
		user_languages.append('Sylvan')
		ud['Animal Companion'] = random.choice(['Badger', 'Camel', 'Dire Rat', 'Dog', 'Riding Dog', 'Eagle', 'Hawk', 'Light Horse', 'Heavy Horse', 'Owl', 'Pony', 'Small Snake', 'Medium Snake', 'Viper', 'Wolf'])
		ud['Gold'] = random.randint(20, 80)
		
	if user_class == 'Fighter':
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(melee_weapons)
		else:
			ud['Weapon'] = random.choice(ranged_weapons)
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(armor)
		ud['Religion'] = random.choice(['Heironeous', 'Kord', 'St. Cuthbert', 'Hextor', 'Erythnul'])
		ud['Gold'] = random.randint(60, 240)
		add_feat()
		
	if user_class == 'Monk':
		if random.random() > 0.9:
			ud['Armor'] = armor[random.randint(0, 5)]
		if random.random() > 0.9:
			ud['Shield'] = shields[random.randint(0, 4)]
			ud['Weapon'] = random.choice(['Club', 'Light Crossbow', 'Heavy Crossbow', 'Dagger', 'Handaxe', 'Javelin', 'Kama', 'Nunchaku', 'Quarterstaff', 'Sai', 'Shuriken', 'Siangham', 'Sling'])
			ud['Alignment'] = 'Lawful '+ random.choice(alignment2)
		if random.random() > 0.3:
			ud['Religion'] = random.choice(['Heironeous', 'St. Cuthbert', 'Hextor'])
		else:
			ud['Religion'] = random.choice(religions)
		ud['ac'] = pb('wis') + 10
		user_feats.append('Improved Unarmed Strike')
		user_feats.append(random.choice(['Improved Grapple', 'Stunning Fist']))
		ud['Gold'] = random.randint(5, 20)
		
	if user_class == 'Paladin':
		ud['Armor'] = random.choice(armor)
		ud['Shield'] = random.choice(shields)
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(ranged_weapons)
		else:
			ud['Weapon'] = random.choice(melee_weapons)
		ud['Alignment'] = 'Lawful Good'
		if random.random() > 0.7:
			ud['Religion'] = 'Heironeous'
		elif random.random() > 0.6:
			ud['Religion'] = 'Pelor'
		ud['Gold'] = random.randint(60, 240)
		
	if user_class == 'Ranger':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Shield'] = shields[random.randint(0, 3)]
		ud['Weapon'] = random.choice(ranged_weapons)
		ud['Favored Enemy'] = random.choice(['Aberration', 'Animal', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Giant', 'Humanoid (aquatic)', 'Humanoid (dwarf)', 'Humanoid (elf)', 'Humanoid (goblinoid)', 'Humanoid (gnoll)', 'Humanoid (gnome)', 'Humanoid (halfling)', 'Humanoid (human)', 'Humanoid (orc)', 'Humanoid (reptilian)', 'Magical beast', 'Monstrous humanoid', 'Ooze', 'Outsider (air)', 'Outsider (chaotic)', 'Outsider (earth)', 'Outsider (evil)', 'Outsider (fire)', 'Outsider (good)', 'Outsider (lawful)', 'Outsider (native)', 'Outsider (water)', 'Plant', 'Undead', 'Vermin'])
		user_feats.append('Track')
		if random.random() > 0.7:
			if random.random() > 0.5:
				ud['Religion'] = 'Ehlonna'
			else:
				ud['Religion'] = 'Obad Hai'
		elif random.random() > 0.6:
			ud['Religion'] = random.choice(religions)
		ud['Gold'] = random.randint(60, 240)
		
	if user_class == 'Rogue':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Weapon'] = random.choice(['Hand Crossbow', 'Sap', 'Short Bow', 'Rapier', 'Short Sword', 'Club', 'Dagger', 'Javelin', 'Light Mace', 'Heavy Mace', 'Short Spear', 'Sickle', 'Spear', 'Spiked Gauntlet', 'Great Club', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Light Crossbow', 'Heavy Crossbow'])
		ud['Religion'] = random.choice(religions)
		ud['Gold'] = random.randint(50, 200)
		
	if user_class == 'Sorcerer':
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(ranged_weapons)
		else:
			ud['Weapon'] = random.choice(melee_weapons)
		if random.random() > 0.5:
			ud['Religion'] = random.choice(religions)
			ud['Familiar'] = random.choice(familiars)
			if ud['Familiar'] == 'Toad':ud['Health'] = 7 + pb('con')
		ud['Gold'] = random.randint(30, 180)
		
	if user_class == 'Wizard':
		ud['Weapon'] = random.choice(['Club', 'Dagger', 'Heavy Crossbow', 'Light Crossbow', 'Quarterstaff'])
		user_feats.append('Scribe Scroll')
		if random.random() > 0.8:
			user_feats.append('Spell Mastery')
		if random.random() > 0.6:
			ud['Religion'] = 'Boccob'
			ud['Alignment'] = random.choice(alignment1) + random.choice(['Good', 'Neutral'])
		elif random.random() > 0.3:
			ud['Religion'] = 'Nerull'
		ud['Familiar'] = random.choice(familiars)
		if ud['Familiar'] == 'Toad':ud['Health'] = 7 + pb('con')
		if random.random() > 0.7:
			del (user_languages[1])
			user_languages.append('Draconic')
		ud['School'] = random.choice(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'])
		if ud['School'] != 'Divination':
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
			while ud['School'] in user_forbidden_schools:
				del user_forbidden_schools[-2]
				user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
		else:
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
			while ud['School'] in user_forbidden_schools:
				del user_forbidden_schools[-1]
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
		ud['Gold'] = random.randint(30, 120)
		
	if pb('int') > 1:add_lang()
	
	ud.setdefault('Armor', 'None')
	ud.setdefault('Shield', 'None')
	ud.setdefault('Weapon', 'Unarmed')
	
	if skill_points < 1:
		skill_points = 1
	if user_race == 'Human':
		skill_points += 1
	if skill_points > len(skill_list[user_class]):
		skill_points = len(skill_list[input_class]) - 1
	if ud['str'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Power Attack']
		skill_points -= 1
	if ud['dex'] > 12 and random.random() > 0.3 and skill_points > 0:
		user_skills += ['Dodge']
		skill_points -= 1
	if ud['int'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Combat Experience']
		skill_points -= 1
	if ud['dex'] > 14 and random.random() > 0.2 and skill_points > 0:
		user_skills += ['Two Weapon Fighting']
		skill_points -= 1
	if weapon_data[ud['Weapon']]['Handed'] != 1:
		ud['Shield'] = 'None'
	
	user_skills += random.sample(skill_list[user_class], skill_points)
	
	add_feat()	
	
"""like the stats befre, these values may be set above, if they are not, theyre set here."""
	ud.setdefault('Alignment', random.choice(alignment1) + random.choice(alignment2))
	ud.setdefault('School', '')
	ud.setdefault('Familiar', '')
	ud.setdefault('ac', 10 + armor_data[ud['Armor']]['Armor Bonus'] + armor_data[ud['Shield']]['Armor Bonus'])
	
	if ud['Alignment'] == 'Neutral Neutral':ud['Alignment'] = 'True Neutral' 
			
	ud['af'] = armor_data[ud['Armor']]['Arcane Spell Failure']
	
	clear() 
	#the main print dialog.
	print('Name: {}'.format(ud['Name']))
	print('Age: {} \n'.format(ud['Age']))
	print('Character Type: {} {}'.format(user_race, user_class))
	print('Alignment: {}'.format(ud['Alignment']))
	print('Languages: {}'.format(list_to_string(user_languages)))
	print('Feat(s): {} \n'.format(list_to_string(user_feats)))

	print('School: {}\nForbidden Schools: {}\nFamiliar: {}\n\n'.format(ud['School'], list_to_string(user_forbidden_schools), ud['Familiar'])*int(len(ud['School']) != 0), end='')
	
	print('Domains: {}\n\n'.format(list_to_string(user_domains))*int(len(user_domains) != 0), end='')
	
	print('Weapon: {} ({} Handed | Damage: {}, {} | Critical Multiplier: {}x)'.format(ud['Weapon'], weapon_data[ud['Weapon']]['Handed'], weapon_data[ud['Weapon']]['Damage (M)'], weapon_data[ud['Weapon']]['Type'], weapon_data[ud['Weapon']]['Critical']))
	
	print('Armor: {}'.format(ud['Armor']))
	print('Shield: {}'.format(ud['Shield']))
	print('Armor Class: {}\nArcane Spell Failure Chance: {}%'.format(ud['ac'], ud['af']))
	print('\nHealth Points: {}\n'.format(ud['Health']))
	#i am so happy with ho this looks.
	print('Strength:     {0:2d} ({1:+d})'.format(ud['str'], pb('str')))
	print('Dexterity:    {0:2d} ({1:+d})'.format(ud['dex'], pb('dex')))
	print('Constitution: {0:2d} ({1:+d})'.format(ud['con'], pb('con')))
	print('Intelligence: {0:2d} ({1:+d})'.format(ud['int'], pb('int')))
	print('Wisdom:       {0:2d} ({1:+d})'.format(ud['wis'], pb('wis')))
	print('Charisma:     {0:2d} ({1:+d})'.format(ud['cha'], pb('cha')))	
	
	print("\nSize: {}, Height: {}'{}, Weight: {} lbs.".format(str(ud['Size']), ud['Height'] // 12, ud['Height'] % 12, ud['Weight']))
	print('Physical Descriptions: {} {} Hair, {} Skin, {} Eyes\n'.format(ud['Hair Color'], ud['Hair Type'], ud['Skin Tone'], ud['Eye Color']))
	if 'Religion' in ud:print('Religion: {}\n'.format(ud['Religion']))
	print('Load: {} lbs'.format(weapon_data[ud['Weapon']]['Weight'] + int(armor_data[ud['Armor']]['Weight']) // ud['Size']))
	print('Skills: {}'.format(list_to_string(user_skills)))
	print('Gold: {}'.format(ud['Gold']))
	print('Items: Backpack with waterskin, one day’s trail rations, bedroll, sack, flint and steel') 
	"""so it turns out in the 3.5 handbook, the items that each character starts with is exactly the same. """
	return

if __name__ == '__main__':
	x = str.split(get_info(), '.')
	generate(x[0], x[1])


			
	
	def add_feat(): #adds another feat to user_feats, and ensures it isn't a duplicate
		user_feats.append(random.choice(feats))
		while len(user_feats) != len(set(user_feats)):
			del user_feats[-1]
			user_feats.append(random.choice(feats))
	
	if user_race == 'Dwarf':
		ud['Name'] = random.choice(dwarf_first_names) + ' ' + random.choice(dwarf_last_names) + ', of the clan ' + random.choice(dwarf_clans)
		if random.random() > 0.8:
			ud['Religion'] = 'Moradin'
		ud['Age'] = random.randint(40, 140)
		ud['Height'] = random.randint(48, 56)
		ud['Weight'] = 130 + (ud['Height'] - 57) * random.randint(2, 12)
		ud['con'] = random.randint(10, 20)
		ud['cha'] = random.randint(6, 16)
		user_languages.append('Dwarven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Deep Tan', 'Pale', 'Beige', 'Light Brown'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Brown', 'Black', 'Deep Grey'])
		
	if user_race == 'Elf':
		ud['Name'] = random.choice(elf_first_names) + ' ' + random.choice(elf_last_names)
		if random.random() > 0.8:
			ud['Religion'] = 'Corellon Larethian'
		ud['Age'] = random.randint(110, 180)
		ud['Height'] = random.randint(55, 65)
		ud['Weight'] = 85 + (ud['Height'] - 52) * random.randint(1, 6)
		ud['dex'] = random.randint(10, 20)
		ud['con'] = random.randint(6, 16)
		user_languages.append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Dark Pale'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Light Green', 'Green', 'Dark Green', 'Green Grey'])
		
	if user_race == 'Halfling':
		ud['Name'] = random.choice(halfling_first_names) + ' ' + random.choice(halfling_last_names)
		if random.random() > 0.7:
			ud['Alignment'] = 'Neutral ' + random.choice(alignment2)
		ud['Age'] = random.randint(22, 30)
		ud['Height'] = random.randint(30, 32)
		ud['Weight'] = random.randint(34, 40)
		ud['dex'] = random.randint(10, 20)
		ud['str'] = random.randint(6, 16)
		user_languages.append('Halfling')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Pink'])
		ud['Hair Color'] = 'Black'
		ud['Hair Type'] = 'Straight'
		ud['Eye Color'] = random.choice(['Brown', 'Black'])
			
	if user_race == 'Gnome':
		ud['Name'] = random.choice(gnome_first_name) + ' ' + random.choice(gnome_nick_names) + ' ' + random.choice(gnome_last_names) + ' of the clan ' + random.choice(gnome_clans)
		if random.random() > 0.4:
			ud['Alignment'] = random.choice(alignment1) + 'Good'
		ud['Age'] = random.randint(40, 250)
		ud['Height'] = random.randint(36, 42)
		ud['Weight'] = random.randint(40, 45)
		ud['con'] = random.randint(10, 20)
		ud['str'] = random.randint(6, 16)
		user_languages.append('Gnome')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(['Deep Tan', 'Woody Brown'])
		ud['Hair Color'] = random.choice(['Blonde', 'White', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Light Blue', 'Blue', 'Dark Blue', 'Blue Grey'])
		
	if user_race == 'Half Elf':
		ud['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			ud['Name'] = random.sample(human_first_names[ud['Tribe']], 1)
		else:
			ud['Name'] = random.sample(elf_first_names, 1)
		if random.random() > 0.5:
			ud['Name'] += random.sample(human_first_names[ud['Tribe']], 1)
		else:
			ud['Name'] += random.sample(elf_last_names, 1)
		ud['Name'] = ' '.join(str(x) for x in ud['Name'])
		if random.random() > 0.5:
			ud['Name'] += ' of the clan ' + random.choice(human_tribes)
		ud['Age'] = random.randint(20, 180)
		ud['Height'] = random.randint(68, 73)
		ud['Weight'] = random.randint(100, 180)
		user_languages.append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Brown', 'Beige', 'White', 'Pink'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
	if user_race == 'Half Orc':
		ud['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			ud['Name'] = random.sample(orc_first_names, 1)
		else:
			ud['Name'] = random.sample(human_first_names[ud['Tribe']], 1)
		if random.random() > 0.7:
			ud['Alignment'] = random.choice(alignment1) + 'Evil'
			ud['Name'] += random.sample(human_first_names[ud['Tribe']], 1)
		ud['Name'] = ' '.join(str(x) for x in ud['Name'])
		if random.random() > 0.8:
			ud['Name'] += ' of the clan ' + random.choice(human_tribes)
		ud['Age'] = random.randint(15, 40)
		ud['Height'] = random.randint(72, 84)
		ud['Weight'] = random.randint(180, 250)
		ud['int'] = random.randint(6, 16)
		ud['cha'] = random.randint(6, 16)
		ud['str'] = random.randint(10, 20)
		user_languages.append('Orc')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Black', 'Brown', 'Grey', 'White'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
		
	if user_race == 'Human':
		ud['Tribe'] = random.choice(human_tribes)
		ud['Age'] = random.randint(18, 30)
		ud['Height'] = random.randint(60, 80)
		ud['Weight'] = 120 + (ud['Height'] - 58) * random.randint(2, 8)
		ud['Name'] = ' '.join(str(x) for x in random.sample(human_first_names[ud['Tribe']], 1) + random.sample(human_last_names[ud['Tribe']], 1)) + ', of the clan ' + ud['Tribe']
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Black', 'Brown', 'Beige', 'White', 'Pink'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		add_lang()
	
	#since some races have modifiers for stats, so those are set  with thw other race data. to save space, the following statements writes all of the stats that werent previously set
	ud.setdefault('str', random.randint(8, 18))
	ud.setdefault('dex', random.randint(8, 18))
	ud.setdefault('con', random.randint(8, 18))
	ud.setdefault('cha', random.randint(8, 18))
	ud.setdefault('int', random.randint(8, 18))
	ud.setdefault('wis', random.randint(8, 18))
	#these variables are needed for class stuff, so theyre set beforehand
	skill_points = class_xp[user_class] + pb('int')
	ud['Health'] = class_health[user_class] + pb('con')
	
	if user_class == 'Barbarian':
		ud['Weapon'] = random.choice(melee_weapons)
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(['Padded Leather', 'Padded Leather', 'Chain Shirt', 'Hide', 'Scalemail', 'Chainmail', 'Breastplate'])
		ud['Alignment'] = random.choice(alignment1[0:2]) + random.choice(alignment2)
		if random.random() > 0.3:
			ud['Religion'] = 'Kord'
			if random.random() > 0.6:
				ud['Religion'] = 'Obad Hai'
				if random.random() > 0.9:
					ud['Religion'] = 'Erythnul'
		ud['Gold'] = random.randint(40, 160)
	
	if user_class == 'Bard':
		ud['Weapon'] = random.choice(['Whip', 'Long Sword', 'Rapier', 'Sap', 'Short Sword', 'Short Bow', 'Dagger', 'Gauntlet', 'Light Mace', 'Sickle', 'Club', 'Heavy Mace', 'Morningstar', 'Short Spear', 'Long Spear', 'Quarterstaff', 'Spear', 'Heavy Crossbow', 'Light Crossbow', 'Javelin', 'Sling'])
		ud['Shield'] = shields[random.randint(0, 3)]
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Chain Shirt'])
		ud['Alignment'] = random.choice(['Neutral ', 'Chaotic ']) + random.choice(alignment2)
		if 'Chaotic' in ud['Alignment']:
			ud['Religion'] = 'Olidammara'
		elif random.random() > 0.5:
			ud['Religion'] = 'Pelor'
		elif random.random() > 0.5:
			ud['Religion'] = 'Corellon Larethian'
		ud['Gold'] = random.randint(40, 160)
		
	if user_class == 'Cleric':
		ud['Religion'] = random.choice(religions)
		x = religion_alignments[ud['Religion']] #in dnd, the religion of a cleric can be one "tile" away from their god's religion. this segment figures which alignment to land on
		if x % 3 != 0 and (x + 1) < 10 and random.random() > 0.5:
			x += 1
		elif (x + 3) < 10 and random.random() > 0.5:
			x += 3
		else:
			if x % 3 != 0 and (x - 1) > 0 and random.random() > 0.5:
				x -= 1
			elif (x - 3) > 0 and random.random() > 0.5:
				x -= 3
		ud['Alignment'] = religion_table[x]
		ud['Weapon'] = religion_weapons[ud['Religion']]
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Chainmail', 'Breastplate', 'Splintmail', 'Bandedmail', 'Half Plate'])
		ud['Shield'] = random.choice(shields)
		user_domains = random.sample(religion_domains[ud['Religion']], 2)
		user_languages.append(random.choice(['Celestial', 'Abyssal', 'Infernal']))
		if 'War' in user_domains:
			user_feats.append('Weapon Focus')
		ud['Gold'] = random.randint(50, 200)
		
	if user_class == 'Druid':
		if random.random() > 0.5:
			ud['Shield'] = 'Light Wooden'
			ud['Weapon'] = 'Unarmed'
		else:
			ud['Shield'] = 'Heavy Wooden'
			ud['Weapon'] = random.choice(['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Short Spear', 'Sling', 'Spear'])
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Hide'])
		if random.random() > 0.8:
			if random.random() > 0.5:
				ud['Religion'] = 'Obad Hai'
			else:
				ud['Religion'] = 'Ehlonna'
				ud['Alignment'] = random.choice(['Neutral Good', 'Chaotic Neutral', 'Neutral Evil', 'Lawful Neutral', 'Neutral Neutral'])
		user_languages.append('Druidic')
		user_languages.append('Sylvan')
		ud['Animal Companion'] = random.choice(['Badger', 'Camel', 'Dire Rat', 'Dog', 'Riding Dog', 'Eagle', 'Hawk', 'Light Horse', 'Heavy Horse', 'Owl', 'Pony', 'Small Snake', 'Medium Snake', 'Viper', 'Wolf'])
		ud['Gold'] = random.randint(20, 80)
		
	if user_class == 'Fighter':
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(melee_weapons)
		else:
			ud['Weapon'] = random.choice(ranged_weapons)
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(armor)
		ud['Religion'] = random.choice(['Heironeous', 'Kord', 'St. Cuthbert', 'Hextor', 'Erythnul'])
		ud['Gold'] = random.randint(60, 240)
		add_feat()
		
	if user_class == 'Monk':
		if random.random() > 0.9:
			ud['Armor'] = armor[random.randint(0, 5)]
		if random.random() > 0.9:
			ud['Shield'] = shields[random.randint(0, 4)]
			ud['Weapon'] = random.choice(['Club', 'Light Crossbow', 'Heavy Crossbow', 'Dagger', 'Handaxe', 'Javelin', 'Kama', 'Nunchaku', 'Quarterstaff', 'Sai', 'Shuriken', 'Siangham', 'Sling'])
			ud['Alignment'] = 'Lawful '+ random.choice(alignment2)
		if random.random() > 0.3:
			ud['Religion'] = random.choice(['Heironeous', 'St. Cuthbert', 'Hextor'])
		else:
			ud['Religion'] = random.choice(religions)
		ud['ac'] = pb('wis') + 10
		user_feats.append('Improved Unarmed Strike')
		user_feats.append(random.choice(['Improved Grapple', 'Stunning Fist']))
		ud['Gold'] = random.randint(5, 20)
		
	if user_class == 'Paladin':
		ud['Armor'] = random.choice(armor)
		ud['Shield'] = random.choice(shields)
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(ranged_weapons)
		else:
			ud['Weapon'] = random.choice(melee_weapons)
		ud['Alignment'] = 'Lawful Good'
		if random.random() > 0.7:
			ud['Religion'] = 'Heironeous'
		elif random.random() > 0.6:
			ud['Religion'] = 'Pelor'
		ud['Gold'] = random.randint(60, 240)
		
	if user_class == 'Ranger':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Shield'] = shields[random.randint(0, 3)]
		ud['Weapon'] = random.choice(ranged_weapons)
		ud['Favored Enemy'] = random.choice(['Aberration', 'Animal', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Giant', 'Humanoid (aquatic)', 'Humanoid (dwarf)', 'Humanoid (elf)', 'Humanoid (goblinoid)', 'Humanoid (gnoll)', 'Humanoid (gnome)', 'Humanoid (halfling)', 'Humanoid (human)', 'Humanoid (orc)', 'Humanoid (reptilian)', 'Magical beast', 'Monstrous humanoid', 'Ooze', 'Outsider (air)', 'Outsider (chaotic)', 'Outsider (earth)', 'Outsider (evil)', 'Outsider (fire)', 'Outsider (good)', 'Outsider (lawful)', 'Outsider (native)', 'Outsider (water)', 'Plant', 'Undead', 'Vermin'])
		user_feats.append('Track')
		if random.random() > 0.7:
			if random.random() > 0.5:
				ud['Religion'] = 'Ehlonna'
			else:
				ud['Religion'] = 'Obad Hai'
		elif random.random() > 0.6:
			ud['Religion'] = random.choice(religions)
		ud['Gold'] = random.randint(60, 240)
		
	if user_class == 'Rogue':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Weapon'] = random.choice(['Hand Crossbow', 'Sap', 'Short Bow', 'Rapier', 'Short Sword', 'Club', 'Dagger', 'Javelin', 'Light Mace', 'Heavy Mace', 'Short Spear', 'Sickle', 'Spear', 'Spiked Gauntlet', 'Great Club', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Light Crossbow', 'Heavy Crossbow'])
		ud['Religion'] = random.choice(religions)
		ud['Gold'] = random.randint(50, 200)
		
	if user_class == 'Sorcerer':
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(ranged_weapons)
		else:
			ud['Weapon'] = random.choice(melee_weapons)
		if random.random() > 0.5:
			ud['Religion'] = random.choice(religions)
			ud['Familiar'] = random.choice(familiars)
			if ud['Familiar'] == 'Toad':ud['Health'] = 7 + pb('con')
		ud['Gold'] = random.randint(30, 180)
		
	if user_class == 'Wizard':
		ud['Weapon'] = random.choice(['Club', 'Dagger', 'Heavy Crossbow', 'Light Crossbow', 'Quarterstaff'])
		user_feats.append('Scribe Scroll')
		if random.random() > 0.8:
			user_feats.append('Spell Mastery')
		if random.random() > 0.6:
			ud['Religion'] = 'Boccob'
			ud['Alignment'] = random.choice(alignment1) + random.choice(['Good', 'Neutral'])
		elif random.random() > 0.3:
			ud['Religion'] = 'Nerull'
		ud['Familiar'] = random.choice(familiars)
		if ud['Familiar'] == 'Toad':ud['Health'] = 7 + pb('con')
		if random.random() > 0.7:
			del (user_languages[1])
			user_languages.append('Draconic')
		ud['School'] = random.choice(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'])
		if ud['School'] != 'Divination':
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
			while ud['School'] in user_forbidden_schools:
				del user_forbidden_schools[-2]
				user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
		else:
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
			while ud['School'] in user_forbidden_schools:
				del user_forbidden_schools[-1]
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
		ud['Gold'] = random.randint(30, 120)
		
	if pb('int') > 1:add_lang()
	
	ud.setdefault('Armor', 'None')
	ud.setdefault('Shield', 'None')
	ud.setdefault('Weapon', 'Unarmed')
	
	if skill_points < 1:
		skill_points = 1
	if user_race == 'Human':
		skill_points += 1
	if skill_points > len(skill_list[user_class]):
		skill_points = len(skill_list[input_class]) - 1
	if ud['str'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Power Attack']
		skill_points -= 1
	if ud['dex'] > 12 and random.random() > 0.3 and skill_points > 0:
		user_skills += ['Dodge']
		skill_points -= 1
	if ud['int'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Combat Experience']
		skill_points -= 1
	if ud['dex'] > 14 and random.random() > 0.2 and skill_points > 0:
		user_skills += ['Two Weapon Fighting']
		skill_points -= 1
	if weapon_data[ud['Weapon']]['Handed'] != 1:
		ud['Shield'] = 'None'
	
	user_skills += random.sample(skill_list[user_class], skill_points)
	
	add_feat()	
	
	#like the stats befre, these values may be set above, if they are not, theyre set here.	
	ud.setdefault('Alignment', random.choice(alignment1) + random.choice(alignment2))
	ud.setdefault('School', '')
	ud.setdefault('Familiar', '')
	ud.setdefault('ac', 10 + armor_data[ud['Armor']]['Armor Bonus'] + armor_data[ud['Shield']]['Armor Bonus'])
	
	if ud['Alignment'] == 'Neutral Neutral':ud['Alignment'] = 'True Neutral' 
			
	ud['af'] = armor_data[ud['Armor']]['Arcane Spell Failure']
	
	clear() 
	#the main print dialog.
	print('Name: {}'.format(ud['Name']))
	print('Age: {} \n'.format(ud['Age']))
	print('Character Type: {} {}'.format(user_race, user_class))
	print('Alignment: {}'.format(ud['Alignment']))
	print('Languages: {}'.format(ls(user_languages)))
	print('Feat(s): {} \n'.format(ls(user_feats)))

	print('School: {}\nForbidden Schools: {}\nFamiliar: {}\n\n'.format(ud['School'], ls(user_forbidden_schools), ud['Familiar'])*int(len(ud['School']) != 0), end='')
	
	print('Domains: {}\n\n'.format(ls(user_domains))*int(len(user_domains) != 0), end='')
	
	print('Weapon: {} ({} Handed | Damage: {}, {} | Critical Multiplier: {}x)'.format(ud['Weapon'], weapon_data[ud['Weapon']]['Handed'], weapon_data[ud['Weapon']]['Damage (M)'], weapon_data[ud['Weapon']]['Type'], weapon_data[ud['Weapon']]['Critical']))
	
	print('Armor: {}'.format(ud['Armor']))
	print('Shield: {}'.format(ud['Shield']))
	print('Armor Class: {}\nArcane Spell Failure Chance: {}%'.format(ud['ac'], ud['af']))
	print('\nHealth Points: {}\n'.format(ud['Health']))
	#i am so happy with ho this looks.
	print('Strength:     {0:2d} ({1:+d})'.format(ud['str'], pb('str')))
	print('Dexterity:    {0:2d} ({1:+d})'.format(ud['dex'], pb('dex')))
	print('Constitution: {0:2d} ({1:+d})'.format(ud['con'], pb('con')))
	print('Intelligence: {0:2d} ({1:+d})'.format(ud['int'], pb('int')))
	print('Wisdom:       {0:2d} ({1:+d})'.format(ud['wis'], pb('wis')))
	print('Charisma:     {0:2d} ({1:+d})'.format(ud['cha'], pb('cha')))	
	
	print("\nSize: {}, Height: {}'{}, Weight: {} lbs.".format(str(ud['Size']), ud['Height'] // 12, ud['Height'] % 12, ud['Weight']))
	print('Physical Descriptions: {} {} Hair, {} Skin, {} Eyes\n'.format(ud['Hair Color'], ud['Hair Type'], ud['Skin Tone'], ud['Eye Color']))
	if 'Religion' in ud:print('Religion: {}\n'.format(ud['Religion']))
	print('Load: {} lbs'.format(weapon_data[ud['Weapon']]['Weight'] + int(armor_data[ud['Armor']]['Weight']) // ud['Size']))
	print('Skills: {}'.format(ls(user_skills)))
	print('Gold: {}'.format(ud['Gold']))
	print('Items: Backpack with waterskin, one day’s trail rations, bedroll, sack, flint and steel') #so it turns out in the 3.5 handbook, the items that each character starts with is exactly the same. 
	return

if __name__ == '__main__':
	x = str.split(get_info(), '.')
	generate(x[0], x[1])


			
	
	def add_feat():
		user_feats.append(random.choice(feats))
		while len(user_feats) != len(set(user_feats)):
			del user_feats[-1]
			user_feats.append(random.choice(feats))
	
	if user_race == 'Dwarf':
		ud['Name'] = random.choice(dwarf_first_names) + ' ' + random.choice(dwarf_last_names) + ', of the clan ' + random.choice(dwarf_clans)
		if random.random() > 0.8:
			ud['Religion'] = 'Moradin'
		ud['Age'] = random.randint(40, 140)
		ud['Height'] = random.randint(48, 56)
		ud['Weight'] = 130 + (ud['Height'] - 57) * random.randint(2, 12)
		ud['con'] = random.randint(10, 20)
		ud['cha'] = random.randint(6, 16)
		user_languages.append('Dwarven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Deep Tan', 'Pale', 'Beige', 'Light Brown'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Brown', 'Black', 'Deep Grey'])
		
	if user_race == 'Elf':
		ud['Name'] = random.choice(elf_first_names) + ' ' + random.choice(elf_last_names)
		if random.random() > 0.8:
			ud['Religion'] = 'Corellon Larethian'
		ud['Age'] = random.randint(110, 180)
		ud['Height'] = random.randint(55, 65)
		ud['Weight'] = 85 + (ud['Height'] - 52) * random.randint(1, 6)
		ud['dex'] = random.randint(10, 20)
		ud['con'] = random.randint(6, 16)
		user_languages.append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Dark Pale'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Light Green', 'Green', 'Dark Green', 'Green Grey'])
		
	if user_race == 'Halfling':
		ud['Name'] = random.choice(halfling_first_names) + ' ' + random.choice(halfling_last_names)
		if random.random() > 0.7:
			ud['Alignment'] = 'Neutral ' + random.choice(alignment2)
		ud['Age'] = random.randint(22, 30)
		ud['Height'] = random.randint(30, 32)
		ud['Weight'] = random.randint(34, 40)
		ud['dex'] = random.randint(10, 20)
		ud['str'] = random.randint(6, 16)
		user_languages.append('Halfling')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Pink'])
		ud['Hair Color'] = 'Black'
		ud['Hair Type'] = 'Straight'
		ud['Eye Color'] = random.choice(['Brown', 'Black'])
			
	if user_race == 'Gnome':
		ud['Name'] = random.choice(gnome_first_name) + ' ' + random.choice(gnome_nick_names) + ' ' + random.choice(gnome_last_names) + ' of the clan ' + random.choice(gnome_clans)
		if random.random() > 0.4:
			ud['Alignment'] = random.choice(alignment1) + 'Good'
		ud['Age'] = random.randint(40, 250)
		ud['Height'] = random.randint(36, 42)
		ud['Weight'] = random.randint(40, 45)
		ud['con'] = random.randint(10, 20)
		ud['str'] = random.randint(6, 16)
		user_languages.append('Gnome')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(['Deep Tan', 'Woody Brown'])
		ud['Hair Color'] = random.choice(['Blonde', 'White', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Light Blue', 'Blue', 'Dark Blue', 'Blue Grey'])
		
	if user_race == 'Half Elf':
		ud['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			ud['Name'] = random.sample(human_first_names[ud['Tribe']], 1)
		else:
			ud['Name'] = random.sample(elf_first_names, 1)
		if random.random() > 0.5:
			ud['Name'] += random.sample(human_first_names[ud['Tribe']], 1)
		else:
			ud['Name'] += random.sample(elf_last_names, 1)
		ud['Name'] = ' '.join(str(x) for x in ud['Name'])
		if random.random() > 0.5:
			ud['Name'] += ' of the clan ' + random.choice(human_tribes)
		ud['Age'] = random.randint(20, 180)
		ud['Height'] = random.randint(68, 73)
		ud['Weight'] = random.randint(100, 180)
		user_languages.append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Brown', 'Beige', 'White', 'Pink'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
	if user_race == 'Half Orc':
		ud['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			ud['Name'] = random.sample(orc_first_names, 1)
		else:
			ud['Name'] = random.sample(human_first_names[ud['Tribe']], 1)
		if random.random() > 0.7:
			ud['Alignment'] = random.choice(alignment1) + 'Evil'
			ud['Name'] += random.sample(human_first_names[ud['Tribe']], 1)
		ud['Name'] = ' '.join(str(x) for x in ud['Name'])
		if random.random() > 0.8:
			ud['Name'] += ' of the clan ' + random.choice(human_tribes)
		ud['Age'] = random.randint(15, 40)
		ud['Height'] = random.randint(72, 84)
		ud['Weight'] = random.randint(180, 250)
		ud['int'] = random.randint(6, 16)
		ud['cha'] = random.randint(6, 16)
		ud['str'] = random.randint(10, 20)
		user_languages.append('Orc')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Black', 'Brown', 'Grey', 'White'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
		
	if user_race == 'Human':
		ud['Tribe'] = random.choice(human_tribes)
		ud['Age'] = random.randint(18, 30)
		ud['Height'] = random.randint(60, 80)
		ud['Weight'] = 120 + (ud['Height'] - 58) * random.randint(2, 8)
		ud['Name'] = ' '.join(str(x) for x in random.sample(human_first_names[ud['Tribe']], 1) + random.sample(human_last_names[ud['Tribe']], 1)) + ', of the clan ' + ud['Tribe']
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Black', 'Brown', 'Beige', 'White', 'Pink'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		add_lang()
		
	ud.setdefault('str', random.randint(8, 18))
	ud.setdefault('dex', random.randint(8, 18))
	ud.setdefault('con', random.randint(8, 18))
	ud.setdefault('cha', random.randint(8, 18))
	ud.setdefault('int', random.randint(8, 18))
	ud.setdefault('wis', random.randint(8, 18))
	
	skill_points = class_xp[user_class] + pb('int')
	ud['Health'] = class_health[user_class] + pb('con')
	
	if user_class == 'Barbarian':
		ud['Weapon'] = random.choice(melee_weapons)
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(['Padded Leather', 'Padded Leather', 'Chain Shirt', 'Hide', 'Scalemail', 'Chainmail', 'Breastplate'])
		ud['Alignment'] = random.choice(alignment1[0:2]) + random.choice(alignment2)
		if random.random() > 0.3:
			ud['Religion'] = 'Kord'
			if random.random() > 0.6:
				ud['Religion'] = 'Obad Hai'
				if random.random() > 0.9:
					ud['Religion'] = 'Erythnul'
		ud['Gold'] = random.randint(40, 160)
	
	if user_class == 'Bard':
		ud['Weapon'] = random.choice(['Whip', 'Long Sword', 'Rapier', 'Sap', 'Short Sword', 'Short Bow', 'Dagger', 'Gauntlet', 'Light Mace', 'Sickle', 'Club', 'Heavy Mace', 'Morningstar', 'Short Spear', 'Long Spear', 'Quarterstaff', 'Spear', 'Heavy Crossbow', 'Light Crossbow', 'Javelin', 'Sling'])
		ud['Shield'] = shields[random.randint(0, 3)]
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Chain Shirt'])
		ud['Alignment'] = random.choice(['Neutral ', 'Chaotic ']) + random.choice(alignment2)
		if 'Chaotic' in ud['Alignment']:
			ud['Religion'] = 'Olidammara'
		elif random.random() > 0.5:
			ud['Religion'] = 'Pelor'
		elif random.random() > 0.5:
			ud['Religion'] = 'Corellon Larethian'
		ud['Gold'] = random.randint(40, 160)
		
	if user_class == 'Cleric':
		ud['Religion'] = random.choice(religions)
		x = religion_alignments[ud['Religion']]
		if x % 3 != 0 and (x + 1) < 10 and random.random() > 0.5:
			x += 1
		elif (x + 3) < 10 and random.random() > 0.5:
			x += 3
		else:
			if x % 3 != 0 and (x - 1) > 0 and random.random() > 0.5:
				x -= 1
			elif (x - 3) > 0 and random.random() > 0.5:
				x -= 3
		ud['Alignment'] = religion_table[x]
		ud['Weapon'] = religion_weapons[ud['Religion']]
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Chainmail', 'Breastplate', 'Splintmail', 'Bandedmail', 'Half Plate'])
		ud['Shield'] = random.choice(shields)
		user_domains = random.sample(religion_domains[ud['Religion']], 2)
		user_languages.append(random.choice(['Celestial', 'Abyssal', 'Infernal']))
		if 'War' in user_domains:
			user_feats.append('Weapon Focus')
		ud['Gold'] = random.randint(50, 200)
		
	if user_class == 'Druid':
		if random.random() > 0.5:
			ud['Shield'] = 'Light Wooden'
			ud['Weapon'] = 'Unarmed'
		else:
			ud['Shield'] = 'Heavy Wooden'
			ud['Weapon'] = random.choice(['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Short Spear', 'Sling', 'Spear'])
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Hide'])
		if random.random() > 0.8:
			if random.random() > 0.5:
				ud['Religion'] = 'Obad Hai'
			else:
				ud['Religion'] = 'Ehlonna'
				ud['Alignment'] = random.choice(['Neutral Good', 'Chaotic Neutral', 'Neutral Evil', 'Lawful Neutral', 'Neutral Neutral'])
		user_languages.append('Druidic')
		user_languages.append('Sylvan')
		ud['Animal Companion'] = random.choice(['Badger', 'Camel', 'Dire Rat', 'Dog', 'Riding Dog', 'Eagle', 'Hawk', 'Light Horse', 'Heavy Horse', 'Owl', 'Pony', 'Small Snake', 'Medium Snake', 'Viper', 'Wolf'])
		ud['Gold'] = random.randint(20, 80)
		
	if user_class == 'Fighter':
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(melee_weapons)
		else:
			ud['Weapon'] = random.choice(ranged_weapons)
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(armor)
		ud['Religion'] = random.choice(['Heironeous', 'Kord', 'St. Cuthbert', 'Hextor', 'Erythnul'])
		ud['Gold'] = random.randint(60, 240)
		add_feat()
		
	if user_class == 'Monk':
		if random.random() > 0.9:
			ud['Armor'] = armor[random.randint(0, 5)]
		if random.random() > 0.9:
			ud['Shield'] = shields[random.randint(0, 4)]
			ud['Weapon'] = random.choice(['Club', 'Light Crossbow', 'Heavy Crossbow', 'Dagger', 'Handaxe', 'Javelin', 'Kama', 'Nunchaku', 'Quarterstaff', 'Sai', 'Shuriken', 'Siangham', 'Sling'])
			ud['Alignment'] = 'Lawful '+ random.choice(alignment2)
		if random.random() > 0.3:
			ud['Religion'] = random.choice(['Heironeous', 'St. Cuthbert', 'Hextor'])
		else:
			ud['Religion'] = random.choice(religions)
		ud['ac'] = pb('wis') + 10
		user_feats.append('Improved Unarmed Strike')
		user_feats.append(random.choice(['Improved Grapple', 'Stunning Fist']))
		ud['Gold'] = random.randint(5, 20)
		
	if user_class == 'Paladin':
		ud['Armor'] = random.choice(armor)
		ud['Shield'] = random.choice(shields)
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(ranged_weapons)
		else:
			ud['Weapon'] = random.choice(melee_weapons)
		ud['Alignment'] = 'Lawful Good'
		if random.random() > 0.7:
			ud['Religion'] = 'Heironeous'
		elif random.random() > 0.6:
			ud['Religion'] = 'Pelor'
		ud['Gold'] = random.randint(60, 240)
		
	if user_class == 'Ranger':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Shield'] = shields[random.randint(0, 3)]
		ud['Weapon'] = random.choice(ranged_weapons)
		ud['Favored Enemy'] = random.choice(['Aberration', 'Animal', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Giant', 'Humanoid (aquatic)', 'Humanoid (dwarf)', 'Humanoid (elf)', 'Humanoid (goblinoid)', 'Humanoid (gnoll)', 'Humanoid (gnome)', 'Humanoid (halfling)', 'Humanoid (human)', 'Humanoid (orc)', 'Humanoid (reptilian)', 'Magical beast', 'Monstrous humanoid', 'Ooze', 'Outsider (air)', 'Outsider (chaotic)', 'Outsider (earth)', 'Outsider (evil)', 'Outsider (fire)', 'Outsider (good)', 'Outsider (lawful)', 'Outsider (native)', 'Outsider (water)', 'Plant', 'Undead', 'Vermin'])
		user_feats.append('Track')
		if random.random() > 0.7:
			if random.random() > 0.5:
				ud['Religion'] = 'Ehlonna'
			else:
				ud['Religion'] = 'Obad Hai'
		elif random.random() > 0.6:
			ud['Religion'] = random.choice(religions)
		ud['Gold'] = random.randint(60, 240)
		
	if user_class == 'Rogue':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Weapon'] = random.choice(['Hand Crossbow', 'Sap', 'Short Bow', 'Rapier', 'Short Sword', 'Club', 'Dagger', 'Javelin', 'Light Mace', 'Heavy Mace', 'Short Spear', 'Sickle', 'Spear', 'Spiked Gauntlet', 'Great Club', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Light Crossbow', 'Heavy Crossbow'])
		ud['Religion'] = random.choice(religions)
		ud['Gold'] = random.randint(50, 200)
		
	if user_class == 'Sorcerer':
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(ranged_weapons)
		else:
			ud['Weapon'] = random.choice(melee_weapons)
		if random.random() > 0.5:
			ud['Religion'] = random.choice(religions)
			ud['Familiar'] = random.choice(familiars)
			if ud['Familiar'] == 'Toad':ud['Health'] = 7 + pb('con')
		ud['Gold'] = random.randint(30, 180)
		
	if user_class == 'Wizard':
		ud['Weapon'] = random.choice(['Club', 'Dagger', 'Heavy Crossbow', 'Light Crossbow', 'Quarterstaff'])
		user_feats.append('Scribe Scroll')
		if random.random() > 0.8:
			user_feats.append('Spell Mastery')
		if random.random() > 0.6:
			ud['Religion'] = 'Boccob'
			ud['Alignment'] = random.choice(alignment1) + random.choice(['Good', 'Neutral'])
		elif random.random() > 0.3:
			ud['Religion'] = 'Nerull'
		ud['Familiar'] = random.choice(familiars)
		if ud['Familiar'] == 'Toad':ud['Health'] = 7 + pb('con')
		if random.random() > 0.7:
			del (user_languages[1])
			user_languages.append('Draconic')
		ud['School'] = random.choice(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'])
		if ud['School'] != 'Divination':
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
			while ud['School'] in user_forbidden_schools:
				del user_forbidden_schools[-2]
				user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
		else:
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
			while ud['School'] in user_forbidden_schools:
				del user_forbidden_schools[-1]
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
		ud['Gold'] = random.randint(30, 120)
		
	if pb('int') > 1:add_lang()
	
	ud.setdefault('Armor', 'None')
	ud.setdefault('Shield', 'None')
	ud.setdefault('Weapon', 'Unarmed')
	
	if skill_points < 1:
		skill_points = 1
	if user_race == 'Human':
		skill_points += 1
	if skill_points > len(skill_list[user_class]):
		skill_points = len(skill_list[input_class]) - 1
	if ud['str'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Power Attack']
		skill_points -= 1
	if ud['dex'] > 12 and random.random() > 0.3 and skill_points > 0:
		user_skills += ['Dodge']
		skill_points -= 1
	if ud['int'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Combat Experience']
		skill_points -= 1
	if ud['dex'] > 14 and random.random() > 0.2 and skill_points > 0:
		user_skills += ['Two Weapon Fighting']
		skill_points -= 1
	if weapon_data[ud['Weapon']]['Handed'] != 1:
		ud['Shield'] = 'None'
	
	user_skills += random.sample(skill_list[user_class], skill_points)
	
	user_feats.append(random.choice(feats))
	while len(user_feats) != len(set(user_feats)):
		del user_feats[-1]
		user_feats.append(random.choice(feats))
		
	ud.setdefault('Alignment', random.choice(alignment1) + random.choice(alignment2))
	ud.setdefault('School', '')
	ud.setdefault('Familiar', '')
	ud.setdefault('ac', 10 + armor_data[ud['Armor']]['Armor Bonus'] + armor_data[ud['Shield']]['Armor Bonus'])
	
	if ud['Alignment'] == 'Neutral Neutral':ud['Alignment'] = 'True Neutral'
			
	ud['af'] = armor_data[ud['Armor']]['Arcane Spell Failure']
	
	clear()
	print('Name: {}'.format(ud['Name']))
	print('Age: {} \n'.format(ud['Age']))
	print('Character Type: {} {}'.format(user_race, user_class))
	print('Alignment: {}'.format(ud['Alignment']))
	print('Languages: {}'.format(ls(user_languages)))
	print('Feat(s): {} \n'.format(ls(user_feats)))

	print('School: {}\nForbidden Schools: {}\nFamiliar: {}\n\n'.format(ud['School'], ls(user_forbidden_schools), ud['Familiar'])*int(len(ud['School']) != 0), end='')
	
	print('Domains: {}\n\n'.format(ls(user_domains))*int(len(user_domains) != 0), end='')
	
	print('Weapon: {} ({} Handed | Damage: {}, {} | Critical Multiplier: {}x)'.format(ud['Weapon'], weapon_data[ud['Weapon']]['Handed'], weapon_data[ud['Weapon']]['Damage (M)'], weapon_data[ud['Weapon']]['Type'], weapon_data[ud['Weapon']]['Critical']))
	
	print('Armor: {}'.format(ud['Armor']))
	print('Shield: {}'.format(ud['Shield']))
	print('Armor Class: {}\nArcane Spell Failure Chance: {}%'.format(ud['ac'], ud['af']))
	print('\nHealth Points: {}\n'.format(ud['Health']))
	
	print('Strength:     {0:2d} ({1:+d})'.format(ud['str'], pb('str')))
	print('Dexterity:    {0:2d} ({1:+d})'.format(ud['dex'], pb('dex')))
	print('Constitution: {0:2d} ({1:+d})'.format(ud['con'], pb('con')))
	print('Intelligence: {0:2d} ({1:+d})'.format(ud['int'], pb('int')))
	print('Wisdom:       {0:2d} ({1:+d})'.format(ud['wis'], pb('wis')))
	print('Charisma:     {0:2d} ({1:+d})'.format(ud['cha'], pb('cha')))	
	
	print("\nSize: {}, Height: {}'{}, Weight: {} lbs.".format(str(ud['Size']), ud['Height'] // 12, ud['Height'] % 12, ud['Weight']))
	print('Physical Descriptions: {} {} Hair, {} Skin, {} Eyes\n'.format(ud['Hair Color'], ud['Hair Type'], ud['Skin Tone'], ud['Eye Color']))
	if 'Religion' in ud:print('Religion: {}\n'.format(ud['Religion']))
	print('Load: {} lbs'.format(weapon_data[ud['Weapon']]['Weight'] + int(armor_data[ud['Armor']]['Weight']) // ud['Size']))
	print('Skills: {}'.format(ls(user_skills)))
	print('Gold: {}'.format(ud['Gold']))
	print('Items: Backpack with waterskin, one day’s trail rations, bedroll, sack, flint and steel')
	return

if __name__ == '__main__':
	x = str.split(get_info(), '.')
	generate(x[0], x[1])


			
	
	def addfeat():
		user_feats.append(random.choice(feats))
		while len(user_feats) != len(set(user_feats)):
			del user_feats[-1]
			user_feats.append(random.choice(feats))
	
	if user_race == 'Dwarf':
		ud['Name'] = random.choice(dwarf_first_names) + ' ' + random.choice(dwarf_last_names) + ', of the clan ' + random.choice(dwarf_clans)
		if random.random() > 0.8:
			ud['Religion'] = 'Moradin'
		ud['Age'] = random.randint(40, 140)
		ud['Height'] = random.randint(48, 56)
		ud['Weight'] = 130 + (ud['Height'] - 57) * random.randint(2, 12)
		ud['con'] = random.randint(10, 20)
		ud['cha'] = random.randint(6, 16)
		user_languages.append('Dwarven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Deep Tan', 'Pale', 'Beige', 'Light Brown'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Brown', 'Black', 'Deep Grey'])
		
	if user_race == 'Elf':
		ud['Name'] = random.choice(elf_first_names) + ' ' + random.choice(elf_last_names)
		if random.random() > 0.8:
			ud['Religion'] = 'Corellon Larethian'
		ud['Age'] = random.randint(110, 180)
		ud['Height'] = random.randint(55, 65)
		ud['Weight'] = 85 + (ud['Height'] - 52) * random.randint(1, 6)
		ud['dex'] = random.randint(10, 20)
		ud['con'] = random.randint(6, 16)
		user_languages.append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Dark Pale'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Light Green', 'Green', 'Dark Green', 'Green Grey'])
		
	if user_race == 'Halfling':
		ud['Name'] = random.choice(halfling_first_names) + ' ' + random.choice(halfling_last_names)
		if random.random() > 0.7:
			ud['Alignment'] = 'Neutral ' + random.choice(alignment2)
		ud['Age'] = random.randint(22, 30)
		ud['Height'] = random.randint(30, 32)
		ud['Weight'] = random.randint(34, 40)
		ud['dex'] = random.randint(10, 20)
		ud['str'] = random.randint(6, 16)
		user_languages.append('Halfling')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Pink'])
		ud['Hair Color'] = 'Black'
		ud['Hair Type'] = 'Straight'
		ud['Eye Color'] = random.choice(['Brown', 'Black'])
			
	if user_race == 'Gnome':
		ud['Name'] = random.choice(gnome_first_name) + ' ' + random.choice(gnome_nick_names) + ' ' + random.choice(gnome_last_names) + ' of the clan ' + random.choice(gnome_clans)
		if random.random() > 0.4:
			ud['Alignment'] = random.choice(alignment1) + 'Good'
		ud['Age'] = random.randint(40, 250)
		ud['Height'] = random.randint(36, 42)
		ud['Weight'] = random.randint(40, 45)
		ud['con'] = random.randint(10, 20)
		ud['str'] = random.randint(6, 16)
		user_languages.append('Gnome')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(['Deep Tan', 'Woody Brown'])
		ud['Hair Color'] = random.choice(['Blonde', 'White', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Light Blue', 'Blue', 'Dark Blue', 'Blue Grey'])
		
	if user_race == 'Half Elf':
		ud['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			ud['Name'] = random.sample(human_first_names[ud['Tribe']], 1)
		else:
			ud['Name'] = random.sample(elf_first_names, 1)
		if random.random() > 0.5:
			ud['Name'] += random.sample(human_first_names[ud['Tribe']], 1)
		else:
			ud['Name'] += random.sample(elf_last_names, 1)
		ud['Name'] = ' '.join(str(x) for x in ud['Name'])
		if random.random() > 0.5:
			ud['Name'] += ' of the clan ' + random.choice(human_tribes)
		ud['Age'] = random.randint(20, 180)
		ud['Height'] = random.randint(68, 73)
		ud['Weight'] = random.randint(100, 180)
		user_languages.append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Brown', 'Beige', 'White', 'Pink'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
	if user_race == 'Half Orc':
		ud['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			ud['Name'] = random.sample(orc_first_names, 1)
		else:
			ud['Name'] = random.sample(human_first_names[ud['Tribe']], 1)
		if random.random() > 0.7:
			ud['Alignment'] = random.choice(alignment1) + 'Evil'
			ud['Name'] += random.sample(human_first_names[ud['Tribe']], 1)
		ud['Name'] = ' '.join(str(x) for x in ud['Name'])
		if random.random() > 0.8:
			ud['Name'] += ' of the clan ' + random.choice(human_tribes)
		ud['Age'] = random.randint(15, 40)
		ud['Height'] = random.randint(72, 84)
		ud['Weight'] = random.randint(180, 250)
		ud['int'] = random.randint(6, 16)
		ud['cha'] = random.randint(6, 16)
		ud['str'] = random.randint(10, 20)
		user_languages.append('Orc')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Black', 'Brown', 'Grey', 'White'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
		
	if user_race == 'Human':
		ud['Tribe'] = random.choice(human_tribes)
		ud['Age'] = random.randint(18, 30)
		ud['Height'] = random.randint(60, 80)
		ud['Weight'] = 120 + (ud['Height'] - 58) * random.randint(2, 8)
		ud['Name'] = ' '.join(str(x) for x in random.sample(human_first_names[ud['Tribe']], 1) + random.sample(human_last_names[ud['Tribe']], 1)) + ', of the clan ' + ud['Tribe']
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(['Black', 'Brown', 'Beige', 'White', 'Pink'])
		ud['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		addlang()
		
	ud.setdefault('str', random.randint(8, 18))
	ud.setdefault('dex', random.randint(8, 18))
	ud.setdefault('con', random.randint(8, 18))
	ud.setdefault('cha', random.randint(8, 18))
	ud.setdefault('int', random.randint(8, 18))
	ud.setdefault('wis', random.randint(8, 18))
	
	skill_points = class_xp[user_class] + pb('int')
	ud['Health'] = class_health[user_class] + pb('con')
	
	if user_class == 'Barbarian':
		ud['Weapon'] = random.choice(melee_weapons)
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(['Padded Leather', 'Padded Leather', 'Chain Shirt', 'Hide', 'Scalemail', 'Chainmail', 'Breastplate'])
		ud['Alignment'] = random.choice(alignment1[0:2]) + random.choice(alignment2)
		if random.random() > 0.3:
			ud['Religion'] = 'Kord'
			if random.random() > 0.6:
				ud['Religion'] = 'Obad Hai'
				if random.random() > 0.9:
					ud['Religion'] = 'Erythnul'
		ud['Gold'] = random.randint(40, 160)
	
	if user_class == 'Bard':
		ud['Weapon'] = random.choice(['Whip', 'Long Sword', 'Rapier', 'Sap', 'Short Sword', 'Short Bow', 'Dagger', 'Gauntlet', 'Light Mace', 'Sickle', 'Club', 'Heavy Mace', 'Morningstar', 'Short Spear', 'Long Spear', 'Quarterstaff', 'Spear', 'Heavy Crossbow', 'Light Crossbow', 'Javelin', 'Sling'])
		ud['Shield'] = shields[random.randint(0, 3)]
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Chain Shirt'])
		ud['Alignment'] = random.choice(['Neutral ', 'Chaotic ']) + random.choice(alignment2)
		if 'Chaotic' in ud['Alignment']:
			ud['Religion'] = 'Olidammara'
		elif random.random() > 0.5:
			ud['Religion'] = 'Pelor'
		elif random.random() > 0.5:
			ud['Religion'] = 'Corellon Larethian'
		ud['Gold'] = random.randint(40, 160)
		
	if user_class == 'Cleric':
		ud['Religion'] = random.choice(religions)
		x = religion_alignments[ud['Religion']]
		if x % 3 != 0 and (x + 1) < 10 and random.random() > 0.5:
			x += 1
		elif (x + 3) < 10 and random.random() > 0.5:
			x += 3
		else:
			if x % 3 != 0 and (x - 1) > 0 and random.random() > 0.5:
				x -= 1
			elif (x - 3) > 0 and random.random() > 0.5:
				x -= 3
		ud['Alignment'] = religion_table[x]
		ud['Weapon'] = religion_weapons[ud['Religion']]
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Chainmail', 'Breastplate', 'Splintmail', 'Bandedmail', 'Half Plate'])
		ud['Shield'] = random.choice(shields)
		user_domains = random.sample(religion_domains[ud['Religion']], 2)
		user_languages.append(random.choice(['Celestial', 'Abyssal', 'Infernal']))
		if 'War' in user_domains:
			user_feats.append('Weapon Focus')
		ud['Gold'] = random.randint(50, 200)
		
	if user_class == 'Druid':
		if random.random() > 0.5:
			ud['Shield'] = 'Light Wooden'
			ud['Weapon'] = 'Unarmed'
		else:
			ud['Shield'] = 'Heavy Wooden'
			ud['Weapon'] = random.choice(['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Short Spear', 'Sling', 'Spear'])
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Hide'])
		if random.random() > 0.8:
			if random.random() > 0.5:
				ud['Religion'] = 'Obad Hai'
			else:
				ud['Religion'] = 'Ehlonna'
				ud['Alignment'] = random.choice(['Neutral Good', 'Chaotic Neutral', 'Neutral Evil', 'Lawful Neutral', 'Neutral Neutral'])
		user_languages.append('Druidic')
		user_languages.append('Sylvan')
		ud['Animal Companion'] = random.choice(['Badger', 'Camel', 'Dire Rat', 'Dog', 'Riding Dog', 'Eagle', 'Hawk', 'Light Horse', 'Heavy Horse', 'Owl', 'Pony', 'Small Snake', 'Medium Snake', 'Viper', 'Wolf'])
		ud['Gold'] = random.randint(20, 80)
		
	if user_class == 'Fighter':
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(melee_weapons)
		else:
			ud['Weapon'] = random.choice(ranged_weapons)
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(armor)
		ud['Religion'] = random.choice(['Heironeous', 'Kord', 'St. Cuthbert', 'Hextor', 'Erythnul'])
		ud['Gold'] = random.randint(60, 240)
		addfeat()
		
	if user_class == 'Monk':
		if random.random() > 0.9:
			ud['Armor'] = armor[random.randint(0, 5)]
		if random.random() > 0.9:
			ud['Shield'] = shields[random.randint(0, 4)]
			ud['Weapon'] = random.choice(['Club', 'Light Crossbow', 'Heavy Crossbow', 'Dagger', 'Handaxe', 'Javelin', 'Kama', 'Nunchaku', 'Quarterstaff', 'Sai', 'Shuriken', 'Siangham', 'Sling'])
			ud['Alignment'] = 'Lawful '+ random.choice(alignment2)
		if random.random() > 0.3:
			ud['Religion'] = random.choice(['Heironeous', 'St. Cuthbert', 'Hextor'])
		else:
			ud['Religion'] = random.choice(religions)
		ud['ac'] = pb('wis') + 10
		user_feats.append('Improved Unarmed Strike')
		user_feats.append(random.choice(['Improved Grapple', 'Stunning Fist']))
		ud['Gold'] = random.randint(5, 20)
		
	if user_class == 'Paladin':
		ud['Armor'] = random.choice(armor)
		ud['Shield'] = random.choice(shields)
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(ranged_weapons)
		else:
			ud['Weapon'] = random.choice(melee_weapons)
		ud['Alignment'] = 'Lawful Good'
		if random.random() > 0.7:
			ud['Religion'] = 'Heironeous'
		elif random.random() > 0.6:
			ud['Religion'] = 'Pelor'
		ud['Gold'] = random.randint(60, 240)
		
	if user_class == 'Ranger':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Shield'] = shields[random.randint(0, 3)]
		ud['Weapon'] = random.choice(ranged_weapons)
		ud['Favored Enemy'] = random.choice(['Aberration', 'Animal', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Giant', 'Humanoid (aquatic)', 'Humanoid (dwarf)', 'Humanoid (elf)', 'Humanoid (goblinoid)', 'Humanoid (gnoll)', 'Humanoid (gnome)', 'Humanoid (halfling)', 'Humanoid (human)', 'Humanoid (orc)', 'Humanoid (reptilian)', 'Magical beast', 'Monstrous humanoid', 'Ooze', 'Outsider (air)', 'Outsider (chaotic)', 'Outsider (earth)', 'Outsider (evil)', 'Outsider (fire)', 'Outsider (good)', 'Outsider (lawful)', 'Outsider (native)', 'Outsider (water)', 'Plant', 'Undead', 'Vermin'])
		user_feats.append('Track')
		if random.random() > 0.7:
			if random.random() > 0.5:
				ud['Religion'] = 'Ehlonna'
			else:
				ud['Religion'] = 'Obad Hai'
		elif random.random() > 0.6:
			ud['Religion'] = random.choice(religions)
		ud['Gold'] = random.randint(60, 240)
		
	if user_class == 'Rogue':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Weapon'] = random.choice(['Hand Crossbow', 'Sap', 'Short Bow', 'Rapier', 'Short Sword', 'Club', 'Dagger', 'Javelin', 'Light Mace', 'Heavy Mace', 'Short Spear', 'Sickle', 'Spear', 'Spiked Gauntlet', 'Great Club', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Light Crossbow', 'Heavy Crossbow'])
		ud['Religion'] = random.choice(religions)
		ud['Gold'] = random.randint(50, 200)
		
	if user_class == 'Sorcerer':
		if random.random() > 0.5:
			ud['Weapon'] = random.choice(ranged_weapons)
		else:
			ud['Weapon'] = random.choice(melee_weapons)
		if random.random() > 0.5:
			ud['Religion'] = random.choice(religions)
			ud['Familiar'] = random.choice(familiars)
			if ud['Familiar'] == 'Toad':ud['Health'] = 7 + pb('con')
		ud['Gold'] = random.randint(30, 180)
		
	if user_class == 'Wizard':
		ud['Weapon'] = random.choice(['Club', 'Dagger', 'Heavy Crossbow', 'Light Crossbow', 'Quarterstaff'])
		user_feats.append('Scribe Scroll')
		if random.random() > 0.8:
			user_feats.append('Spell Mastery')
		if random.random() > 0.6:
			ud['Religion'] = 'Boccob'
			ud['Alignment'] = random.choice(alignment1) + random.choice(['Good', 'Neutral'])
		elif random.random() > 0.3:
			ud['Religion'] = 'Nerull'
		ud['Familiar'] = random.choice(familiars)
		if ud['Familiar'] == 'Toad':ud['Health'] = 7 + pb('con')
		if random.random() > 0.7:
			del (user_languages[1])
			user_languages.append('Draconic')
		ud['School'] = random.choice(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'])
		if ud['School'] != 'Divination':
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
			while ud['School'] in user_forbidden_schools:
				del user_forbidden_schools[-2]
				user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
		else:
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
			while ud['School'] in user_forbidden_schools:
				del user_forbidden_schools[-1]
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
		ud['Gold'] = random.randint(30, 120)
		
	if pb('int') > 1:addlang()
	
	ud.setdefault('Armor', 'None')
	ud.setdefault('Shield', 'None')
	ud.setdefault('Weapon', 'Unarmed')
	
	if skill_points < 1:
		skill_points = 1
	if user_race == 'Human':
		skill_points += 1
	if skill_points > len(skill_list[user_class]):
		skill_points = len(skill_list[input_class]) - 1
	if ud['str'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Power Attack']
		skill_points -= 1
	if ud['dex'] > 12 and random.random() > 0.3 and skill_points > 0:
		user_skills += ['Dodge']
		skill_points -= 1
	if ud['int'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Combat Experience']
		skill_points -= 1
	if ud['dex'] > 14 and random.random() > 0.2 and skill_points > 0:
		user_skills += ['Two Weapon Fighting']
		skill_points -= 1
	if weapon_data[ud['Weapon']]['Handed'] != 1:
		ud['Shield'] = 'None'
	
	user_skills += random.sample(skill_list[user_class], skill_points)
	
	user_feats.append(random.choice(feats))
	while len(user_feats) != len(set(user_feats)):
		del user_feats[-1]
		user_feats.append(random.choice(feats))
		
	ud.setdefault('Alignment', random.choice(alignment1) + random.choice(alignment2))
	ud.setdefault('School', '')
	ud.setdefault('Familiar', '')
	ud.setdefault('ac', 10 + armor_data[ud['Armor']]['Armor Bonus'] + armor_data[ud['Shield']]['Armor Bonus'])
	
	if ud['Alignment'] == 'Neutral Neutral':ud['Alignment'] = 'True Neutral'
			
	ud['af'] = armor_data[ud['Armor']]['Arcane Spell Failure']
	
	clear()
	print('Name: {}'.format(ud['Name']))
	print('Age: {} \n'.format(ud['Age']))
	print('Character Type: {} {}'.format(user_race, user_class))
	print('Alignment: {}'.format(ud['Alignment']))
	print('Languages: {}'.format(ls(user_languages)))
	print('Feat(s): {} \n'.format(ls(user_feats)))

	print('School: {}\nForbidden Schools: {}\nFamiliar: {}\n\n'.format(ud['School'], ls(user_forbidden_schools), ud['Familiar'])*int(len(ud['School']) != 0), end='')
	
	print('Domains: {}\n\n'.format(ls(user_domains))*int(len(user_domains) != 0), end='')
	
	print('Weapon: {} ({} Handed | Damage: {}, {} | Critical Multiplier: {}x)'.format(ud['Weapon'], weapon_data[ud['Weapon']]['Handed'], weapon_data[ud['Weapon']]['Damage (M)'], weapon_data[ud['Weapon']]['Type'], weapon_data[ud['Weapon']]['Critical']))
	
	print('Armor: {}'.format(ud['Armor']))
	print('Shield: {}'.format(ud['Shield']))
	print('Armor Class: {}\nArcane Spell Failure Chance: {}%'.format(ud['ac'], ud['af']))
	print('\nHealth Points: {}\n'.format(ud['Health']))
	
	print('Strength:     {0:2d} ({1:+d})'.format(ud['str'], pb('str')))
	print('Dexterity:    {0:2d} ({1:+d})'.format(ud['dex'], pb('dex')))
	print('Constitution: {0:2d} ({1:+d})'.format(ud['con'], pb('con')))
	print('Intelligence: {0:2d} ({1:+d})'.format(ud['int'], pb('int')))
	print('Wisdom:       {0:2d} ({1:+d})'.format(ud['wis'], pb('wis')))
	print('Charisma:     {0:2d} ({1:+d})'.format(ud['cha'], pb('cha')))	
	
	print("\nSize: {}, Height: {}'{}, Weight: {} lbs.".format(str(ud['Size']), ud['Height'] // 12, ud['Height'] % 12, ud['Weight']))
	print('Physical Descriptions: {} {} Hair, {} Skin, {} Eyes\n'.format(ud['Hair Color'], ud['Hair Type'], ud['Skin Tone'], ud['Eye Color']))
	if 'Religion' in ud:print('Religion: {}\n'.format(ud['Religion']))
	print('Load: {} lbs'.format(weapon_data[ud['Weapon']]['Weight'] + int(armor_data[ud['Armor']]['Weight']) // ud['Size']))
	print('Skills: {}'.format(ls(user_skills)))
	print('Gold: {}'.format(ud['Gold']))
	print('Items: Backpack with waterskin, one day’s trail rations, bedroll, sack, flint and steel')
	return

if __name__ == '__main__':
	x = str.split(getInfo(), '.')
	generate(x[0], x[1])


		while len(user_languages) != len(set(user_languages)):
			del user_languages[-1]
			user_languages.append(random.choice(language_list))
			
	
	def addfeat():
		user_feats.append(random.choice(feats))
		while len(user_feats) != len(set(user_feats)):
			del user_feats[-1]
			user_feats.append(random.choice(feats))
	
	if user_race == 'Dwarf':
		user_data['Name'] = random.choice(dwarf_first_names) + ' ' + random.choice(dwarf_last_names) + ', of the clan ' + random.choice(dwarf_clans)
		if random.random() > 0.8:
			user_data['Religion'] = 'Moradin'
		user_data['Age'] = random.randrange(40, 140)
		user_data['Height'] = random.randrange(48, 56)
		user_data['Weight'] = 130 + (user_data['Height'] - 57) * random.randrange(2, 12)
		user_data['con'] = random.randrange(10, 20)
		user_data['cha'] = random.randrange(6, 16)
		user_languages.append('Dwarven')
		user_data['Size'] = 1
		user_data['Skin Tone'] = random.choice(['Deep Tan', 'Pale', 'Beige', 'Light Brown'])
		user_data['Hair Color'] = random.choice(['Black', 'Brown', 'Grey'])
		user_data['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		user_data['Eye Color'] = random.choice(['Brown', 'Black', 'Deep Grey'])
		
	if user_race == 'Elf':
		user_data['Name'] = random.choice(elf_first_names) + ' ' + random.choice(elf_last_names)
		if random.random() > 0.8:
			user_data['Religion'] = 'Corellon Larethian'
		user_data['Age'] = random.randrange(110, 180)
		user_data['Height'] = random.randrange(55, 65)
		user_data['Weight'] = 85 + (user_data['Height'] - 52) * random.randrange(1, 6)
		user_data['dex'] = random.randrange(10, 20)
		user_data['con'] = random.randrange(6, 16)
		user_languages.append('Elven')
		user_data['Size'] = 1
		user_data['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Dark Pale'])
		user_data['Hair Color'] = random.choice(['Black', 'Brown', 'Grey'])
		user_data['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		user_data['Eye Color'] = random.choice(['Light Green', 'Green', 'Dark Green', 'Green Grey'])
		
	if user_race == 'Halfling':
		user_data['Name'] = random.choice(halfling_first_names) + ' ' + random.choice(halfling_last_names)
		if random.random() > 0.7:
			user_data['Alignment'] = 'Neutral ' + random.choice(alignment2)
		user_data['Age'] = random.randrange(22, 30)
		user_data['Height'] = random.randrange(30, 32)
		user_data['Weight'] = random.randrange(34, 40)
		user_data['dex'] = random.randrange(10, 20)
		user_data['str'] = random.randrange(6, 16)
		user_languages.append('Halfling')
		user_data['Size'] = 2
		user_data['Skin Tone'] = random.choice(['Light Pale', 'Pale', 'Pink'])
		user_data['Hair Color'] = 'Black'
		user_data['Hair Type'] = 'Straight'
		user_data['Eye Color'] = random.choice(['Brown', 'Black'])
			
	if user_race == 'Gnome':
		user_data['Name'] = random.choice(gnome_first_name) + ' ' + random.choice(gnome_nick_names) + ' ' + random.choice(gnome_last_names) + ' of the clan ' + random.choice(gnome_clans)
		if random.random() > 0.4:
			user_data['Alignment'] = random.choice(alignment1) + 'Good'
		user_data['Age'] = random.randrange(40, 250)
		user_data['Height'] = random.randrange(36, 42)
		user_data['Weight'] = random.randrange(40, 45)
		user_data['con'] = random.randrange(10, 20)
		user_data['str'] = random.randrange(6, 16)
		user_languages.append('Gnome')
		user_data['Size'] = 2
		user_data['Skin Tone'] = random.choice(['Deep Tan', 'Woody Brown'])
		user_data['Hair Color'] = random.choice(['Blonde', 'White', 'Grey'])
		user_data['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		user_data['Eye Color'] = random.choice(['Light Blue', 'Blue', 'Dark Blue', 'Blue Grey'])
		
	if user_race == 'Half Elf':
		user_data['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			user_data['Name'] = random.sample(human_first_names[user_data['Tribe']], 1)
		else:
			user_data['Name'] = random.sample(elf_first_names, 1)
		if random.random() > 0.5:
			user_data['Name'] += random.sample(human_first_names[user_data['Tribe']], 1)
		else:
			user_data['Name'] += random.sample(elf_last_names, 1)
		user_data['Name'] = ' '.join(str(x) for x in user_data['Name'])
		if random.random() > 0.5:
			user_data['Name'] += ' of the clan ' + random.choice(human_tribes)
		user_data['Age'] = random.randrange(20, 180)
		user_data['Height'] = random.randrange(68, 73)
		user_data['Weight'] = random.randrange(100, 180)
		user_languages.append('Elven')
		user_data['Size'] = 1
		user_data['Skin Tone'] = random.choice(['Brown', 'Beige', 'White', 'Pink'])
		user_data['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		user_data['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		user_data['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
	if user_race == 'Half Orc':
		user_data['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			user_data['Name'] = random.sample(orc_first_names, 1)
		else:
			user_data['Name'] = random.sample(human_first_names[user_data['Tribe']], 1)
		if random.random() > 0.7:
			user_data['Alignment'] = random.choice(alignment1) + 'Evil'
			user_data['Name'] += random.sample(human_first_names[user_data['Tribe']], 1)
		user_data['Name'] = ' '.join(str(x) for x in user_data['Name'])
		if random.random() > 0.8:
			user_data['Name'] += ' of the clan ' + random.choice(human_tribes)
		user_data['Age'] = random.randrange(15, 40)
		user_data['Height'] = random.randrange(72, 84)
		user_data['Weight'] = random.randrange(180, 250)
		user_data['int'] = random.randrange(6, 16)
		user_data['cha'] = random.randrange(6, 16)
		user_data['str'] = random.randrange(10, 20)
		user_languages.append('Orc')
		user_data['Size'] = 1
		user_data['Skin Tone'] = random.choice(['Black', 'Brown', 'Grey', 'White'])
		user_data['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		user_data['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		user_data['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		
		
	if user_race == 'Human':
		user_data['Tribe'] = random.choice(human_tribes)
		user_data['Age'] = random.randrange(18, 30)
		user_data['Height'] = random.randrange(60, 80)
		user_data['Weight'] = 120 + (user_data['Height'] - 58) * random.randrange(2, 8)
		user_data['Name'] = ' '.join(str(x) for x in random.sample(human_first_names[user_data['Tribe']], 1) + random.sample(human_last_names[user_data['Tribe']], 1)) + ', of the clan ' + user_data['Tribe']
		user_data['Size'] = 1
		user_data['Skin Tone'] = random.choice(['Black', 'Brown', 'Beige', 'White', 'Pink'])
		user_data['Hair Color'] = random.choice(['Black', 'Brown', 'Blond', 'Red', 'White'])
		user_data['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		user_data['Eye Color'] = random.choice(['Amber', 'Blue', 'Brown', 'Grey', 'Green', 'Hazel'])
		addlang()
		
	user_data.setdefault('str', random.randrange(8, 18))
	user_data.setdefault('dex', random.randrange(8, 18))
	user_data.setdefault('con', random.randrange(8, 18))
	user_data.setdefault('cha', random.randrange(8, 18))
	user_data.setdefault('int', random.randrange(8, 18))
	user_data.setdefault('wis', random.randrange(8, 18))
	
	skill_points = class_xp[user_class] + pb(user_data['int'])
	user_data['Health'] = class_health[user_class] + pb(user_data['con'])
	
	if user_class == 'Barbarian':
		user_data['Weapon'] = random.choice(melee_weapons)
		user_data['Shield'] = random.choice(shields)
		user_data['Armor'] = random.choice(['Padded Leather', 'Padded Leather', 'Chain Shirt', 'Hide', 'Scalemail', 'Chainmail', 'Breastplate'])
		user_data['Alignment'] = random.choice(['Neutral ', 'Chaotic ']) + random.choice(alignment2)
		if random.random() > 0.3:
			user_data['Religion'] = 'Kord'
			if random.random() > 0.6:
				user_data['Religion'] = 'Obad Hai'
				if random.random() > 0.9:
					user_data['Religion'] = 'Erythnul'
		user_data['Gold'] = random.randrange(40, 160)
	
	if user_class == 'Bard':
		user_data['Weapon'] = random.choice(['Whip', 'Long Sword', 'Rapier', 'Sap', 'Short Sword', 'Short Bow', 'Dagger', 'Gauntlet', 'Light Mace', 'Sickle', 'Club', 'Heavy Mace', 'Morningstar', 'Short Spear', 'Long Spear', 'Quarterstaff', 'Spear', 'Heavy Crossbow', 'Light Crossbow', 'Javelin', 'Sling'])
		user_data['Shield'] = shields[random.randrange(0, 3)]
		user_data['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Chain Shirt'])
		user_data['Alignment'] = random.choice(['Neutral ', 'Chaotic ']) + random.choice(alignment2)
		if 'Chaotic' in user_data['Alignment']:
			user_data['Religion'] = 'Olidammara'
		elif random.random() > 0.5:
			user_data['Religion'] = 'Pelor'
		elif random.random() > 0.5:
			user_data['Religion'] = 'Corellon Larethian'
		user_data['Gold'] = random.randrange(40, 160)
		
	if user_class == 'Cleric':
		user_data['Religion'] = random.choice(religions)
		x = religion_alignments[user_data['Religion']]
		if x % 3 != 0 and (x + 1) < 10 and random.random() > 0.5:
			x += 1
		elif (x + 3) < 10 and random.random() > 0.5:
			x += 3
		else:
			if x % 3 != 0 and (x - 1) > 0 and random.random() > 0.5:
				x -= 1
			elif (x - 3) > 0 and random.random() > 0.5:
				x -= 3
		user_data['Alignment'] = religion_table[x]
		user_data['Weapon'] = religion_weapons[user_data['Religion']]
		user_data['Armor'] = random.choice(['Padded', 'Leather', 'Padded Leather', 'Hide', 'Chain Shirt', 'Scalemail', 'Chainmail', 'Breastplate', 'Splintmail', 'Bandedmail', 'Half Plate'])
		user_data['Shield'] = random.choice(shields)
		user_domains = random.sample(religion_domains[user_data['Religion']], 2)
		user_languages.append(random.choice(['Celestial', 'Abyssal', 'Infernal']))
		if 'War' in user_domains:
			user_feats.append('Weapon Focus')
		user_data['Gold'] = random.randrange(50, 200)
		
	if user_class == 'Druid':
		if random.random() > 0.5:
			user_data['Shield'] = 'Light Wooden'
			user_data['Weapon'] = 'Unarmed'
		else:
			user_data['Shield'] = 'Heavy Wooden'
			user_data['Weapon'] = random.choice(['Club', 'Dagger', 'Quarterstaff', 'Scimitar', 'Sickle', 'Short Spear', 'Sling', 'Spear'])
		user_data['Armor'] = random.choice(['Padded', 'Leather', 'Hide'])
		if random.random() > 0.8:
			if random.random() > 0.5:
				user_data['Religion'] = 'Obad Hai'
			else:
				user_data['Religion'] = 'Ehlonna'
				user_data['Alignment'] = random.choice(['Neutral Good', 'Chaotic Neutral', 'Neutral Evil', 'Lawful Neutral', 'Neutral Neutral'])
		user_languages.append('Druidic')
		user_languages.append('Sylvan')
		user_data['Animal Companion'] = random.choice(['Badger', 'Camel', 'Dire Rat', 'Dog', 'Riding Dog', 'Eagle', 'Hawk', 'Light Horse', 'Heavy Horse', 'Owl', 'Pony', 'Small Snake', 'Medium Snake', 'Viper', 'Wolf'])
		user_data['Gold'] = random.randrange(20, 80)
		
	if user_class == 'Fighter':
		if random.random() > 0.5:
			user_data['Weapon'] = random.choice(melee_weapons)
		else:
			user_data['Weapon'] = random.choice(ranged_weapons)
		user_data['Shield'] = random.choice(shields)
		user_data['Armor'] = random.choice(armor)
		user_data['Religion'] = random.choice(['Heironeous', 'Kord', 'St. Cuthbert', 'Hextor', 'Erythnul'])
		user_data['Gold'] = random.randrange(60, 240)
		addfeat()
		
	if user_class == 'Monk':
		if random.random() > 0.9:
			user_data['Armor'] = armor[random.randrange(0, 5)]
		if random.random() > 0.9:
			user_data['Shield'] = shields[random.randrange(0, 4)]
			user_data['Weapon'] = random.choice(['Club', 'Light Crossbow', 'Heavy Crossbow', 'Dagger', 'Handaxe', 'Javelin', 'Kama', 'Nunchaku', 'Quarterstaff', 'Sai', 'Shuriken', 'Siangham', 'Sling'])
			user_data['Alignment'] = random.choice(['Lawful Good', 'Lawful Evil', 'Lawful Neutral'])
		if random.random() > 0.3:
			user_data['Religion'] = random.choice(['Heironeous', 'St. Cuthbert', 'Hextor'])
		else:
			user_data['Religion'] = random.choice(religions)
		user_data['ac'] = pb(user_data['wis']) + 10
		user_feats.append('Improved Unarmed Strike')
		user_feats.append(random.choice(['Improved Grapple', 'Stunning Fist']))
		user_data['Gold'] = random.randrange(5, 20)
		
	if user_class == 'Paladin':
		user_data['Armor'] = random.choice(armor)
		user_data['Shield'] = random.choice(shields)
		if random.random() > 0.5:
			user_data['Weapon'] = random.choice(ranged_weapons)
		else:
			user_data['Weapon'] = random.choice(melee_weapons)
		user_data['Alignment'] = 'Lawful Good'
		if random.random() > 0.7:
			user_data['Religion'] = 'Heironeous'
		elif random.random() > 0.6:
			user_data['Religion'] = 'Pelor'
		user_data['Gold'] = random.randrange(60, 240)
		
	if user_class == 'Ranger':
		user_data['Armor'] = armor[random.randrange(0, 3)]
		user_data['Shield'] = shields[random.randrange(0, 3)]
		user_data['Weapon'] = random.choice(ranged_weapons)
		user_data['Favored Enemy'] = random.choice(['Aberration', 'Animal', 'Construct', 'Dragon', 'Elemental', 'Fey', 'Giant', 'Humanoid (aquatic)', 'Humanoid (dwarf)', 'Humanoid (elf)', 'Humanoid (goblinoid)', 'Humanoid (gnoll)', 'Humanoid (gnome)', 'Humanoid (halfling)', 'Humanoid (human)', 'Humanoid (orc)', 'Humanoid (reptilian)', 'Magical beast', 'Monstrous humanoid', 'Ooze', 'Outsider (air)', 'Outsider (chaotic)', 'Outsider (earth)', 'Outsider (evil)', 'Outsider (fire)', 'Outsider (good)', 'Outsider (lawful)', 'Outsider (native)', 'Outsider (water)', 'Plant', 'Undead', 'Vermin'])
		user_feats.append('Track')
		if random.random() > 0.7:
			if random.random() > 0.5:
				user_data['Religion'] = 'Ehlonna'
			else:
				user_data['Religion'] = 'Obad Hai'
		elif random.random() > 0.6:
			user_data['Religion'] = random.choice(religions)
		user_data['Gold'] = random.randrange(60, 240)
		
	if user_class == 'Rogue':
		user_data['Armor'] = armor[random.randrange(0, 3)]
		user_data['Weapon'] = random.choice(['Hand Crossbow', 'Sap', 'Short Bow', 'Rapier', 'Short Sword', 'Club', 'Dagger', 'Javelin', 'Light Mace', 'Heavy Mace', 'Short Spear', 'Sickle', 'Spear', 'Spiked Gauntlet', 'Great Club', 'Morningstar', 'Quarterstaff', 'Scythe', 'Sling', 'Light Crossbow', 'Heavy Crossbow'])
		user_data['Religion'] = random.choice(religions)
		user_data['Gold'] = random.randrange(50, 200)
		
	if user_class == 'Sorcerer':
		if random.random() > 0.5:
			user_data['Weapon'] = random.choice(ranged_weapons)
		else:
			user_data['Weapon'] = random.choice(melee_weapons)
		if random.random() > 0.5:
			user_data['Religion'] = random.choice(religions)
			user_data['Familiar'] = random.choice(familiars)
			if user_data['Familiar'] == 'Toad':
				del user_data['Health']
				user_data['Health'] = 7 + pb(user_data['con'])
		user_data['Gold'] = random.randrange(30, 180)
		
	if user_class == 'Wizard':
		user_data['Weapon'] = random.choice(['Club', 'Dagger', 'Heavy Crossbow', 'Light Crossbow', 'Quarterstaff'])
		user_feats.append('Scribe Scroll')
		if random.random() > 0.8:
			user_feats.append('Spell Mastery')
		if random.random() > 0.6:
			user_data['Religion'] = 'Boccob'
			user_data['Alignment'] = random.choice(alignment1) + random.choice(['Good', 'Neutral'])
		elif random.random() > 0.3:
			user_data['Religion'] = 'Nerull'
		user_data['Familiar'] = random.choice(familiars)
		if user_data['Familiar'] == 'Toad':
			del user_data['Health']
			user_data['Health'] = 7 + pb(user_data['con'])
		if random.random() > 0.7:
			del (user_languages[1])
			user_languages.append('Draconic')
		user_data['School'] = random.choice(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'])
		if user_data['School'] != 'Divination':
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
			while user_data['School'] in user_forbidden_schools:
				del user_forbidden_schools[-2]
				user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 2)
		else:
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
			while user_data['School'] in user_forbidden_schools:
				del user_forbidden_schools[-1]
			user_forbidden_schools = random.sample(['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation'], 1)
		user_data['Gold'] = random.randrange(30, 120)
		
	if pb(user_data['int']) > 1:addlang()
	
	user_data.setdefault('Armor', 'None')
	user_data.setdefault('Shield', 'None')
	user_data.setdefault('Weapon', 'Unarmed')
	
	if skill_points < 1:
		skill_points = 1
	if user_race == 'Human':
		skill_points += 1
	if skill_points > len(skill_list[user_class]):
		skill_points = len(skill_list[input_class]) - 1
	if user_data['str'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Power Attack']
		skill_points -= 1
	if user_data['dex'] > 12 and random.random() > 0.3 and skill_points > 0:
		user_skills += ['Dodge']
		skill_points -= 1
	if user_data['int'] > 12 and random.random() > 0.4 and skill_points > 0:
		user_skills += ['Combat Experience']
		skill_points -= 1
	if user_data['dex'] > 14 and random.random() > 0.2 and skill_points > 0:
		user_skills += ['Two Weapon Fighting']
		skill_points -= 1
	if weapon_data[user_data['Weapon']]['Handed'] != 1:
		user_data['Shield'] = 'None'
	
	user_skills += random.sample(skill_list[user_class], skill_points)
	
	user_feats.append(random.choice(feats))
	while len(user_feats) != len(set(user_feats)):
		del user_feats[-1]
		user_feats.append(random.choice(feats))
		
	user_data.setdefault('Alignment', random.choice(alignment1) + random.choice(alignment2))
	user_data.setdefault('School', '')
	user_data.setdefault('ac', 10 + armor_data[user_data['Armor']]['Armor Bonus'] + armor_data[user_data['Shield']]['Armor Bonus'])
	

	if user_data['Alignment'] == 'Neutral Neutral':
		del user_data['Alignment']
		user_data['Alignment'] = 'True Neutral'
			
	user_data['af'] = armor_data[user_data['Armor']]['Arcane Spell Failure']
	
	clear()
	print('Name: {}'.format(user_data['Name']))
	print('Age: {} \n'.format(user_data['Age']))
	print('Character Type: {} {}'.format(user_race, user_class))
	print('Alignment: {}'.format(user_data['Alignment']))
	print('Languages: {}'.format(ls(user_languages)))
	print('Feat(s): {} \n'.format(ls(user_feats)))

	print('School: {}\nForbidden Schools: {}\n'.format(user_data['School'], ls(user_forbidden_schools))*int(len(user_data['School']) != 0), end='')
	print('Domains: {}\n'.format(ls(user_domains))*int(len(user_domains) != 0), end='')
	print('Weapon: {} ({} Handed | Damage: {}, {} | Critical Multiplier: {}x)'.format(user_data['Weapon'], weapon_data[user_data['Weapon']]['Handed'], weapon_data[user_data['Weapon']]['Damage (M)'], weapon_data[user_data['Weapon']]['Type'], weapon_data[user_data['Weapon']]['Critical']))
	
	print('Armor: {}'.format(user_data['Armor']))
	print('Shield: {}'.format(user_data['Shield']))
	print('Armor Class: {}\nArcane Spell Failure Chance: {}%'.format(user_data['ac'], user_data['af']))
	print('\nHealth Points: {}\n'.format(user_data['Health']))
	
	print('Strength:     {0:02d} ({1:+d})'.format(user_data['str'], pb(user_data['str'])))
	print('Dexterity:    {0:02d} ({1:+d})'.format(user_data['dex'], pb(user_data['dex'])))
	print('Constitution: {0:02d} ({1:+d})'.format(user_data['con'], pb(user_data['con'])))
	print('Intelligence: {0:02d} ({1:+d})'.format(user_data['int'], pb(user_data['int'])))
	print('Wisdom:       {0:02d} ({1:+d})'.format(user_data['wis'], pb(user_data['wis'])))
	print('Charisma:     {0:02d} ({1:+d})'.format(user_data['cha'], pb(user_data['cha'])))	
	
	print("\nSize: {}, Height: {}'{}, Weight: {} lbs.".format(str(user_data['Size']), user_data['Height'] // 12, user_data['Height'] % 12, user_data['Weight']))
	print('Physical Descriptions: {} {} Hair, {} Skin, {} Eyes\n'.format(user_data['Hair Color'], user_data['Hair Type'], user_data['Skin Tone'], user_data['Eye Color']))
	if 'Religion' in user_data:print('Religion: {}\n'.format(user_data['Religion']))
	print('Load: {} lbs'.format(weapon_data[user_data['Weapon']]['Weight'] + int(armor_data[user_data['Armor']]['Weight']) // user_data['Size']))
	print('Skills: {}'.format(ls(user_skills)))
	print('Gold: {}'.format(user_data['Gold']))
	print('Items: Backpack with waterskin, one day’s trail rations, bedroll, sack, flint and steel')
	return

if __name__ == '__main__':
	x = str.split(getRace(), '.')
	generate(x[0], x[1])

