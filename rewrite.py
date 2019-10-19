import random
import data as d


class Player:
    def __init__(self, user_race, user_class):
        self.user_class = user_class
        self.user_race = user_race
        self.languages = []
        self.feats = []
        self.skills = []
        self.domains = []
        self.school = None
        self.forbidden_schools = []
        self.stats = {}
        self.stat_mods = {}
        self.alignment = None
        self.familiar = None
        self.armor = 'None'
        self.shield = 'None'
        self.weapon = 'Unarmed'
        self.deity = None
        self.name = None
        self.age = None
        self.height = None
        self.weight = None
        self.size = None
        self.skin_tone = None
        self.hair_color = None
        self.hair_type = None
        self.eye_color = None
        self.health = None
        self.gold = None
        self.armor_class = None
        self.arcane_failure = None
        self.favored_enemy = None

    def setup(self):
        while not self.user_race or not self.user_class:
            user_input = str.title(input(f'Select a Race\n{", ".join(list(d.races.keys()))}\nand class\n{", ".join(list(d.classes.keys()))}\n[Enter] for random\n'))
            if 'Half ' in user_input:
                user_input = user_input.replace('Half ', 'Half-')
            self.user_race = [item for item in user_input.split(' ') if item in d.races.keys()] or [random.choice(d.races.keys())]
            self.user_class = [item for item in user_input.split(' ') if item in d.classes.keys()] or [random.choice(d.classes.keys())]
        self.user_class = self.user_class[0]
        self.user_race = self.user_race[0]
        self.generate_character()

    @staticmethod
    def roll_dice(roll):
        values = [int(s) for s in roll.split('d') if s.isdigit()]
        rolls = sorted([random.randint(1, values[1]) for _ in range(values[0])])
        return sum(rolls[len(values) == 3*values[-1]:])

    def generate_character(self):
        self.languages = ['Common']
        for item in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            self.stats[item] = self.roll_dice('4d6d1')
        for item in self.stats.keys():
            if item in d.races[self.user_race]:
                self.stats[item] += d.races[self.user_race][item]
            self.stat_mods[item] = (self.stats[item] - 10) // 2
        if 'language' in d.races[self.user_race]:
            self.languages += [d.races[self.user_race]['language']]
        self.alignment = random.choice(d.align_chart)
        self.skin_tone = random.choice(d.skin_tones)
        self.hair_color = random.choice(d.hair_colors)
        self.hair_type = random.choice(d.hair_types)
        self.eye_color = random.choice(d.eye_colors)
        self.age = d.races[self.user_race]['age'][0] + self.roll_dice(d.races[self.user_race]['age'][1])
        self.height = d.races[self.user_race]['height'][0] + self.roll_dice(d.races[self.user_race]['height'][1])
        self.weight = d.races[self.user_race]['weight'][0] + (self.roll_dice(d.races[self.user_race]['weight'][1]) * (self.height - d.races[self.user_race]['height'][0]))
        self.size = d.races[self.user_race]['size']
        self.deity = random.choice(list(d.deities.keys()))
        self.gold = self.roll_dice(d.classes[self.user_class]['gold']) * 10
        skill_points = max(d.classes[self.user_class]['xp'] + self.stat_mods['int'], 1)
        self.health = d.classes[self.user_class]['health'] + self.stat_mods['con']

        if self.user_race is 'Dwarf':
            self.name = f'{random.choice(d.races["Dwarf"]["first names"])} {random.choice(d.races["Dwarf"]["last names"])}, of the clan {random.choice(d.races["Dwarf"]["clans"])}'

        if self.user_race is 'Elf':
            self.name = f'{random.choice(d.races["Elf"]["first names"])} {random.choice(d.races["Elf"]["last names"])}'

        if self.user_race is 'Halfling':
            self.name = f'{random.choice(d.races["Halfling"]["first names"])} {random.choice(d.races["Halfling"]["last names"])}'

        if self.user_race is 'Gnome':
            self.name = f'{random.choice(d.races["Gnome"]["first names"])} "{random.choice(d.races["Gnome"]["nick names"])}" {random.choice(d.races["Gnome"]["last names"])}, of the clan {random.choice(d.races["Gnome"]["clans"])}'

        if self.user_race is 'Half-Elf':
            tribe = random.choice(d.races["Human"]['tribes'])
            self.name = f'{random.choice(d.races["Human"]["first names"][tribe] + d.races["Elf"]["first names"])} {random.choice(d.races["Human"]["first names"][tribe] + d.races["Elf"]["last names"])}'
            if self.roll_dice('1d2') == 2:
                self.name += ' of the clan ' + tribe

        if self.user_race is 'Half-Orc':
            tribe = random.choice(d.races["Human"]['tribes'])
            if self.roll_dice('1d2') == 2:
                self.name = random.choice(d.races["Orc"]['first names'])
            else:
                self.name = f'{random.choice(d.races["Human"]["first names"][tribe] + d.races["Orc"]["first names"])} {random.choice(d.races["Human"]["first names"][tribe])}'
                if self.roll_dice('1d10') > 7:
                    self.name += f', of the tribe {tribe}'

        if self.user_race is 'Human':
            tribe = random.choice(d.races["Human"]['tribes'])
            self.name = f'{random.choice(d.races["Human"]["first names"][tribe])} {random.choice(d.races["Human"]["first names"][tribe])}, of the clan {tribe}'
            self.languages += [random.choice([item for item in d.languages if item not in self.languages])]

        if self.user_class is 'Barbarian':
            self.deity = random.choice(d.classes[self.user_class]['deities'])
            self.weapon = random.choice([i for i in d.weapons.keys() if d.weapons[i]['Rarity'] in ['Simple Weapons', 'Martial Weapons']])
            self.shield = random.choice(list(d.shields.keys()))
            self.armor = random.choice(d.classes[self.user_class]['armor'])
            self.alignment = random.choice([item for item in d.align_chart if item[0] not in 'Lawful'])

        if self.user_class is 'Bard':
            self.weapon = random.choice(d.classes[self.user_class]['weapons'])
            self.shield = random.choice([i for i in d.shields.keys() if d.shields[i]['Class'] == 'Light'])
            self.armor = random.choice([i for i in d.armor.keys() if d.armor[i]['Class'] == 'Light'])
            self.alignment = random.choice([item for item in d.align_chart if item[0] not in 'Lawful'])
            self.deity = 'Fharlanghn'
            if self.user_race == 'Elf':
                self.deity = 'Corellon Larethian'
            elif 'Chaotic' in self.alignment:
                self.deity = 'Olidammara'
            elif 'Good' in self.alignment:
                self.deity = 'Pelor'
            elif 'Evil' in self.alignment:
                self.deity = 'Erythnul'

        if self.user_class is 'Cleric':
            if 'deity' in d.races[self.user_race] and self.roll_dice('1d2') == 2:
                self.deity = d.races[self.user_race]['deity']
            self.alignment = d.align_chart[random.choice(d.classes[self.user_class]['alignment'][d.deities[self.deity]['alignment']-1])-1]
            self.weapon = d.deities[self.deity]['weapon']
            self.armor = random.choice(d.classes[self.user_class]['armor'])
            self.shield = random.choice(list(d.shields.keys()))
            self.domains = random.sample(d.deities[self.deity]['domains'], 2)
            self.languages += [random.choice(d.classes['Cleric']['languages'])]
            if 'War' in self.domains:
                self.feats += ['Weapon Focus']
            if ['Animal', 'Plant'] in self.domains:
                self.skills += 'Knowledge, Nature'

        if self.user_class is 'Druid':
            if self.roll_dice('1d2') == 2:
                self.shield = 'Light Wooden'
                self.weapon = 'Unarmed'
            else:
                self.shield = 'Heavy Wooden'
                self.weapon = random.choice(d.classes[self.user_class]['weapons'])
            self.armor = random.choice(d.classes[self.user_class]['armor'])
            self.alignment = random.choice([item for item in d.align_chart if 'Neutral' in item])
            self.languages += d.classes[self.user_class]['languages']
            self.familiar = random.choice(d.classes[self.user_class]['companions'])

        if self.user_class is 'Fighter':
            self.weapon = random.choice([i for i in d.weapons.keys() if d.weapons[i]['Rarity'] in ['Simple Weapons', 'Martial Weapons']])
            self.shield = random.choice(list(d.shields.keys()))
            self.armor = random.choice(list(d.armor.keys()))
            self.deity = random.choice(d.classes[self.user_class]['deities'])
            self.feats += [random.choice(d.feats)]

        if self.user_class is 'Monk':
            self.alignment = random.choice([item for item in d.align_chart if item[0] in 'Lawful'])
            self.weapon = random.choice(d.classes[self.user_class]['weapons'])
            if self.roll_dice('1d10') == 10:
                self.armor = random.choice([i for i in d.armor.keys() if d.armor[i]['Class'] == 'Light'])
                self.shield = random.choice([i for i in d.shields.keys() if d.shields[i]['Class'] == 'Light'])
            else:
                self.shield = 'None'
                self.weapon = 'Unarmed'
            if not self.armor:
                self.armor_class = 10 + d.armor['None']['Armor Bonus'] + d.shields[self.shield]['Armor Bonus'] + self.stat_mods['wis']
            self.feats += ['Improved Unarmed Strike', random.choice(['Improved Grapple', 'Stunning Fist'])]

        if self.user_class is 'Paladin':
            self.armor = random.choice(list(d.armor.keys()))
            self.shield = random.choice(list(d.shields.keys()))
            self.weapon = random.choice(list(d.weapons.keys()))
            self.alignment = ('Lawful', 'Good')

        if self.user_class is 'Ranger':
            self.armor = random.choice([i for i in d.armor.keys() if d.armor[i]['Class'] == 'Light'])
            self.shield = random.choice([i for i in d.shields.keys() if d.shields[i]['Class'] == 'Light'])
            self.weapon = random.choice([i for i in d.weapons.keys() if 'Ranged' in d.weapons[i]['Weapon Type']])
            self.favored_enemy = random.choice(d.classes[self.user_class]['favored enemies'])
            self.feats += ['Track']

        if self.user_class is 'Rogue':
            self.armor = random.choice([i for i in d.armor.keys() if d.armor[i]['Class'] == 'Light'])
            self.weapon = random.choice(d.classes[self.user_class]['weapons'])
            self.deity = random.choice(list(d.deities.keys()))

        if self.user_class is 'Sorcerer':
            self.weapon = random.choice([i for i in d.weapons.keys() if 'Simple' in d.weapons[i]['Rarity']])
            if self.roll_dice('1d2') == 2:
                self.deity = None
            self.familiar = random.choice(d.familiars)
            if self.familiar == 'Toad':
                self.health = 7 + self.stat_mods['con']

        if self.user_class is 'Wizard':
            self.weapon = random.choice(d.classes[self.user_class]['weapons'])
            self.feats += ['Scribe Scroll']
            if self.roll_dice('1d10') > 7:
                self.feats += ['Spell Mastery']
            self.familiar = random.choice(d.familiars)
            if self.familiar == 'Toad':
                self.health = 7 + self.stat_mods['con']
            if self.roll_dice('1d10') > 7 and len(self.languages) > 1:
                self.languages.pop()
                self.languages += ['Draconic']
            self.school = random.choice(list(d.classes[self.user_class]['schools']))
            self.forbidden_schools = random.sample([item for item in list(d.classes[self.user_class]['schools']) if item[0] not in self.school], 2 - int(self.school == 'Divination'))

        if self.stat_mods['int'] > 1:
            self.languages += [random.choice([item for item in d.languages if item[0] not in self.languages])]

        if self.user_race == 'Human':
            skill_points += 1
        if skill_points > len(d.classes[self.user_class]['skills']):
            skill_points = len(d.classes[self.user_class]['skills']) - 1
        if self.stats['str'] > 12 and self.roll_dice('1d10') > 8 and skill_points > 0:
            self.skills += ['Power Attack']
            skill_points -= 1
        if self.stats['dex'] > 12 and self.roll_dice('1d10') > 6 and skill_points > 0:
            self.skills += ['Dodge']
            skill_points -= 1
        if self.stats['int'] > 12 and self.roll_dice('1d10') > 4 and skill_points > 0:
            self.skills += ['Combat Experience']
            skill_points -= 1
        if self.stats['dex'] > 14 and self.roll_dice('1d10') > 2 and skill_points > 0:
            self.skills += ['Two Weapon Fighting']
            skill_points -= 1
        self.skills += random.sample([item for item in d.classes[self.user_class]['skills'] if item[0] not in self.skills], skill_points)

        if self.weapon and d.weapons[self.weapon]['Weapon Type'] in ['Two-Handed Melee Weapons', 'Ranged Weapons']:
            self.shield = 'None'

        if not self.armor_class:
            self.armor_class = 10
            if self.armor:
                self.armor_class += d.armor[self.armor]['Armor Bonus']
            if self.shield:
                self.armor_class += d.shields[self.shield]['Armor Bonus']

        if self.alignment == ('Neutral', 'Neutral'):
            self.alignment = ('True', 'Neutral')

        self.arcane_failure = d.armor[self.armor]['Arcane Spell Failure'] + d.shields[self.shield]['Arcane Spell Failure']

        if sum([self.stats[item] for item in self.stats.keys()]) > 98:
            print('\n\n\n')
            for item in self.__dict__:
                if self.__dict__[item]:
                    print(f'{item}: {self.__dict__[item]}')
            print('\n\n\n')


if __name__ == '__main__':
    m_counter = 0
    while True:
        for u_class in d.class_list:
            for u_race in d.race_list:
                a = Player(user_class=[u_class], user_race=[u_race])
                a.setup()
                m_counter += 1
                if m_counter % 5000 == 0:
                    print('ding', m_counter)
    a = Player()
    a.setup()
