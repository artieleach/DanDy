import random, re
from data import *
from console import clear
input_class = ''
input_race = ''


def list_to_string(list):
	return ', '.join(str(x) for x in list)


def get_info():  # grabs info from the user
	clear()
	user_input = str.title(input('Select a Race\n({})\n\n[Enter] for random'.format(list_to_string(race_list))))
	if len(user_input.split()) == 3:
		input_race = '{} {}'.format(user_input.split()[0], user_input.split()[1])
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
	return str(input_race + '.' + input_class)

				
def generate(user_race, user_class):  # uses input to create character
	ud = {}
		
	def roll_dice(roll):
		values = [int(x) for x in re.findall(r'\d+', roll)]
		drop = 0
		if 'D' in roll:
			drop = values[2]
		top_rolls = sorted(list(random.randint(1, values[1]) for _ in range(values[0])))
		return sum(top_rolls[drop:])
	
	def pb(skill):
		return (ud[skill] - 10) // 2
		
	def add_list(list, source, times=1):
		if 'x' in ud[list]:
			ud[list].pop(0)
		for i in range(times):
			ud[list].append(random.choice(source))
		while len(ud[list]) != len(set(ud[list])):
			ud[list].pop()
			ud[list].append(random.choice(source))
		return
		
	ud['Languages'] = ['Common']
	ud['Feats'] = ['x']
	ud['Skills'] = ['x']
	ud['Domains'] = ['x']
	ud['Forbidden Schools'] = ['x']
	ud['str'] = roll_dice('4d6D1')
	ud['dex'] = roll_dice('4d6D1')
	ud['con'] = roll_dice('4d6D1')
	ud['int'] = roll_dice('4d6D1')
	ud['wis'] = roll_dice('4d6D1')
	ud['cha'] = roll_dice('4d6D1')
	ud['Alignment'] = random.choice(alignment1) + random.choice(alignment2)
	ud['School'] = ''
	ud['Familiar'] = ''
	ud['Armor'] = 'None'
	ud['Shield'] = 'None'
	ud['Weapon'] = 'Unarmed'
	ud['Religion'] = 'None'
	
	if user_race == 'Dwarf':
		ud['Name'] = '{} {}, of the clan {}'.format(random.choice(dwarf_first_names), random.choice(dwarf_last_names), random.choice(dwarf_clans))
		if random.random() > 0.8:
			ud['Religion'] = 'Moradin'
		ud['Age'] = int(random.normalvariate(80, 10))
		ud['Height'] = roll_dice('2d4') + 45
		ud['Weight'] = 130 + roll_dice('2d6') * (ud['Height']-45)
		ud['con'] += 2
		ud['cha'] -= 2
		ud['Languages'].append('Dwarven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(dwarf_skin_tones)
		ud['Hair Color'] = random.choice(dwarf_hair_colors)
		ud['Hair Type'] = random.choice(dwarf_hair_types)
		ud['Eye Color'] = random.choice(dwarf_eye_colors)
		
	if user_race == 'Elf':
		ud['Name'] = '{} {}'.format(random.choice(elf_first_names), random.choice(elf_last_names))
		if random.random() > 0.8:
			ud['Religion'] = 'Corellon Larethian'
		ud['Age'] = int(random.normalvariate(140, 10))
		ud['Height'] = roll_dice('2d6') + 58
		ud['Weight'] = 85 + roll_dice('1d6') * (ud['Height']-58)
		ud['dex'] += 2
		ud['con'] -= 2
		ud['Languages'].append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(elf_skin_tones)
		ud['Hair Color'] = random.choice(elf_hair_colors)
		ud['Hair Type'] = random.choice(elf_hair_types)
		ud['Eye Color'] = random.choice(elf_eye_colors)

	if user_race == 'Halfling':
		ud['Name'] = '{} {}'.format(random.choice(halfling_first_names), random.choice(halfling_last_names))
		ud['Alignment'] = random.choice(alignment1) + random.choice(alignment2)
		ud['Age'] = int(random.normalvariate(25, 2))
		ud['Height'] = roll_dice('2d4') + 32
		ud['Weight'] = 30 + roll_dice('1d1') * (ud['Height']-32)  # i decided to use 1d1 instead of removing the * to keep this consistent with the rest of the races
		ud['dex'] += 2
		ud['str'] -= 2
		ud['Languages'].append('Halfling')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(halfling_skin_tones)
		ud['Hair Color'] = 'Black'
		ud['Hair Type'] = 'Straight'
		ud['Eye Color'] = random.choice(['Brown', 'Black'])
			
	if user_race == 'Gnome':
		ud['Name'] = '{} "{}" {}, of the clan {}'.format(random.choice(gnome_first_names), random.choice(gnome_nick_names), random.choice(gnome_last_names), random.choice(gnome_clans))
		ud['Alignment'] = random.choice(alignment1) + random.choice(alignment2+['Good'])  # good is listed twice, since gnomes tend to be good.
		ud['Age'] = int(random.normalvariate(140, 20))
		ud['Height'] = roll_dice('2d4') + 36
		ud['Weight'] = 40 + roll_dice('1d6') * (ud['Height']-36)
		ud['con'] += 2
		ud['str'] -= 2
		ud['Languages'].append('Gnome')
		ud['Size'] = 2
		ud['Skin Tone'] = random.choice(['Deep Tan', 'Woody Brown'])
		ud['Hair Color'] = random.choice(['Blonde', 'White', 'Grey'])
		ud['Hair Type'] = random.choice(['Curly', 'Wavy', 'Straight'])
		ud['Eye Color'] = random.choice(gnome_eye_colors)
		
	if user_race == 'Half Elf':
		ud['Tribe'] = random.choice(human_tribes)
		ud['Name'] = '{} {}'.format(random.choice(list(human_first_names[ud['Tribe']])+list(elf_first_names)), random.choice(list(human_first_names[ud['Tribe']])+list(elf_last_names)))
		if random.random() > 0.5:
			ud['Name'] += ' of the clan ' + ud['Tribe']
		ud['Age'] = int(random.normalvariate(80, 20))
		ud['Height'] = roll_dice('2d8') + 55
		ud['Weight'] = 100 + roll_dice('2d4') * (ud['Height']-55)
		ud['Languages'].append('Elven')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(half_elf_skin_tones)
		ud['Hair Color'] = random.choice(half_elf_hair_colors)
		ud['Hair Type'] = random.choice(half_elf_hair_types)
		ud['Eye Color'] = random.choice(half_elf_eye_colors)
		
	if user_race == 'Half Orc':
		ud['Tribe'] = random.choice(human_tribes)
		if random.random() > 0.5:
			ud['Name'] = random.choice(orc_first_names)
		else:
			ud['Name'] = '{} {}'.format(random.choice(list(human_first_names[ud['Tribe']])), random.choice(list(human_last_names[ud['Tribe']])))
		if random.random() > 0.7:
			ud['Alignment'] = random.choice(alignment1) + 'Evil'
		if random.random() > 0.8:
			ud['Name'] = '{} of the tribe {}'.format(ud['Name'], ud['Tribe'])
		ud['Age'] = int(random.normalvariate(25, 5))
		ud['Height'] = roll_dice('2d12') + 58
		ud['Weight'] = 150 + roll_dice('2d6') * (ud['Height']-58)
		ud['int'] -= 2
		ud['cha'] -= 2
		ud['str'] += 2
		ud['Languages'].append('Orc')
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(half_orc_skin_tones)
		ud['Hair Color'] = random.choice(half_orc_hair_colors)
		ud['Hair Type'] = random.choice(half_orc_hair_types)
		ud['Eye Color'] = random.choice(half_orc_eye_colors)
		
	if user_race == 'Human':
		ud['Tribe'] = random.choice(human_tribes)
		ud['Age'] = int(random.normalvariate(25, 4))
		ud['Height'] = roll_dice('2d4') + 58
		ud['Weight'] = 120 + roll_dice('2d6') * (ud['Height']-58)
		ud['Name'] = '{} {} of the clan {}'.format(random.choice(list(human_first_names[ud['Tribe']])), random.choice(list(human_last_names[ud['Tribe']])), ud['Tribe'])
		ud['Size'] = 1
		ud['Skin Tone'] = random.choice(human_skin_tones)
		ud['Hair Color'] = random.choice(human_hair_colors)
		ud['Hair Type'] = random.choice(human_hair_types)
		ud['Eye Color'] = random.choice(human_eye_colors)
		add_list('Languages', language_list)
	
	skill_points = class_xp[user_class] + pb('int')
	ud['Health'] = class_health[user_class] + pb('con')
	
	if user_class == 'Barbarian':
		ud['Weapon'] = random.choice(melee_weapons)
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(barbarian_armor)
		ud['Alignment'] = random.choice(alignment1[0:2]) + random.choice(alignment2)
		ud['Religion'] = random.choice(['Kord', 'Obad Hai', 'Erythnul']+religions)
		ud['Gold'] = roll_dice('4d4')*10

	if user_class == 'Bard':
		ud['Weapon'] = random.choice(bard_weapons)
		ud['Shield'] = random.choice(list(armor_data.keys())[12:16])
		ud['Armor'] = random.choice(list(armor_data.keys()))
		ud['Alignment'] = random.choice(alignment1[1:3]) + random.choice(alignment2)
		if 'Chaotic' in ud['Alignment']:
			ud['Religion'] = 'Olidammara'
		elif random.random() > 0.5:
			ud['Religion'] = random.choice(['Pelor', 'Corellon Larethian'])
		ud['Gold'] = roll_dice('4d4')*10
		
	if user_class == 'Cleric':
		ud['Religion'] = random.choice(religions)  # if anyone can tell me a more efficent way to write 'move one tile over on a 3x3 grid' i will be forever in your debt
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
		ud['Armor'] = random.choice(cleric_armor)
		ud['Shield'] = random.choice(shields)
		add_list('Domains', religion_domains[ud['Religion']], 2)
		ud['Languages'].append(random.choice(['Celestial', 'Abyssal', 'Infernal']))
		if 'War' in ud['Domains']:
			ud['Feats'].append('Weapon Focus')
		ud['Gold'] = roll_dice('5d4')*10
		
	if user_class == 'Druid':
		if random.random() > 0.5:
			ud['Shield'] = 'Light Wooden'
			ud['Weapon'] = 'Unarmed'
		else:
			ud['Shield'] = 'Heavy Wooden'
			ud['Weapon'] = random.choice(druid_weapons)
		ud['Armor'] = random.choice(['Padded', 'Leather', 'Hide'])
		ud['Religion'] = random.choice(religions)
		ud['Alignment'] = religion_table[int(random.choice('24568'))]
		ud['Languages'].append('Druidic')
		ud['Languages'].append('Sylvan')
		ud['Animal Companion'] = random.choice(druid_companions)
		ud['Gold'] = roll_dice('2d4')*10
		
	if user_class == 'Fighter':
		ud['Weapon'] = random.choice(list(weapon_data.keys()))
		ud['Shield'] = random.choice(shields)
		ud['Armor'] = random.choice(armor)
		ud['Religion'] = random.choice(fighter_religions)
		ud['Gold'] = roll_dice('6d4')*10
		add_list('Feats', feat_list)
		
	if user_class == 'Monk':
		ud['Alignment'] = 'Lawful ' + random.choice(alignment2)
		if random.random() > 0.9:
			ud['Shield'] = random.choice(list(armor_data.keys())[12:16])
			ud['Weapon'] = random.choice(monk_weapons)
			ud['Armor']  = random.choice(list(armor_data.keys())[0:12])
		ud['Religion'] = random.choice(['Heironeous', 'St. Cuthbert', 'Hextor'] + religions)
		if ud['Armor'] == 'None':
			ud['ac'] = 10 + armor_data[ud['Armor']]['Armor Bonus'] + armor_data[ud['Shield']]['Armor Bonus'] + pb('wis')
		ud['Feats'].append('Improved Unarmed Strike')
		ud['Feats'].append(random.choice(['Improved Grapple', 'Stunning Fist']))
		ud['Gold'] = roll_dice('5d4')*10
		
	if user_class == 'Paladin':
		ud['Armor'] = random.choice(armor)
		ud['Shield'] = random.choice(shields)
		ud['Weapon'] = random.choice(list(weapon_data.keys()))
		ud['Alignment'] = 'Lawful Good'
		ud['Religion'] = random.choice(['Heironeous', 'Pelor']+religions)
		ud['Gold'] = roll_dice('6d4')*10
		
	if user_class == 'Ranger':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Shield'] = shields[random.randint(0, 3)]
		ud['Weapon'] = random.choice(ranged_weapons)
		ud['Favored Enemy'] = random.choice(ranger_favored_enemies)
		ud['Feats'].append('Track')
		ud['Religion'] = random.choice(['Ehlonna', 'Obad Hai'] + religions)
		ud['Gold'] = roll_dice('6d4')*10
		
	if user_class == 'Rogue':
		ud['Armor'] = armor[random.randint(0, 3)]
		ud['Weapon'] = random.choice(rogue_weapons)
		ud['Religion'] = random.choice(religions)
		ud['Gold'] = roll_dice('5d4')*10
		
	if user_class == 'Sorcerer':
		ud['Weapon'] = random.choice(melee_weapons+ranged_weapons)
		if random.random() > 0.5:
			ud['Religion'] = random.choice(religions)
		ud['Familiar'] = random.choice(familiars)
		if ud['Familiar'] == 'Toad':
			ud['Health'] = 7 + pb('con')
		ud['Gold'] = roll_dice('3d4')*10
		
	if user_class == 'Wizard':
		ud['Weapon'] = random.choice(wizard_weapons)
		ud['Feats'].append('Scribe Scroll')
		if random.random() > 0.8:
			ud['Feats'].append('Spell Mastery')
		ud['Religion'] = random.choice(['Nerull', 'Boccob']+religions)
		ud['Familiar'] = random.choice(familiars)
		if ud['Familiar'] == 'Toad':
			ud['Health'] = 7 + pb('con')
		if random.random() > 0.7:
			ud['Languages'].pop()
			ud['Languages'].append('Draconic')
		ud['School'] = random.choice(list(wizard_schools.keys()))
		add_list('Forbidden Schools', list(wizard_schools.keys()), wizard_schools[ud['School']])
		ud['Gold'] = roll_dice('3d4')*10
		
	if pb('int') > 1:
		add_list('Languages', language_list)
	
	ud.setdefault('ac', 10 + armor_data[ud['Armor']]['Armor Bonus'] + armor_data[ud['Shield']]['Armor Bonus'])
	
	if skill_points < 1:
		skill_points = 1
	if user_race == 'Human':
		skill_points += 1
	if skill_points > len(skill_list[user_class]):
		skill_points = len(skill_list[input_class]) - 1
	if ud['str'] > 12 and random.random() > 0.4 and skill_points > 0:
		ud['Skills'].append('Power Attack')
		skill_points -= 1
	if ud['dex'] > 12 and random.random() > 0.3 and skill_points > 0:
		ud['Skills'].append('Dodge')
		skill_points -= 1
	if ud['int'] > 12 and random.random() > 0.4 and skill_points > 0:
		ud['Skills'].append('Combat Experience')
		skill_points -= 1
	if ud['dex'] > 14 and random.random() > 0.2 and skill_points > 0:
		ud['Skills'].append('Two Weapon Fighting')
		skill_points -= 1
	if weapon_data[ud['Weapon']]['Handed'] != 1:
		ud['Shield'] = 'None'
	
	add_list('Skills', skill_list[user_class], skill_points)
	add_list('Feats', feat_list)
	
	if ud['Alignment'] == 'Neutral Neutral':
		ud['Alignment'] = 'True Neutral'
			
	ud['af'] = armor_data[ud['Armor']]['Arcane Spell Failure']
	
	clear()
	
	print('Name: {}'.format(ud['Name']))
	print('Age: {} \n'.format(ud['Age']))
	print('Character Type: {} {}'.format(user_race, user_class))
	print('Alignment: {}'.format(ud['Alignment']))
	print('Languages: {}'.format(list_to_string(ud['Languages'])))
	print('Feat(s): {} \n'.format(list_to_string(ud['Feats'])))

	print('School: {}\nForbidden Schools: {}\nFamiliar: {}\n\n'.format(ud['School'], list_to_string(ud['Forbidden Schools']), ud['Familiar'])*int(user_class == 'Wizard'), end='')
	print('Familiar: {}\n\n'.format(ud['Familiar'])*(int(user_class == 'wizard' or user_class == 'Sorcerer')), end='')
	
	print('Domains: {}\n\n'.format(list_to_string(ud['Domains']))*int(user_class == 'Cleric'), end='')
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
	print('Religion: {}\n'.format(ud['Religion']))
	print('Load: {} lbs'.format(weapon_data[ud['Weapon']]['Weight'] + int(armor_data[ud['Armor']]['Weight']) // ud['Size']))
	print('Skills: {}'.format(list_to_string(ud['Skills'])))
	print('Gold: {}gp'.format(ud['Gold']))
	print('Items: Backpack with waterskin, one day’s trail rations, bedroll, sack, flint and steel')
	return

if __name__ == '__main__':
	character_info = str.split(get_info(), '.')
	generate(character_info[0], character_info[1])

