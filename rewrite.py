"""A simple pure python script to generate a valid 3.5 D&D character.
Planned features include:
    more robust user control
    a webpage output
    fixed skill points
    other finnicky details"""
import random
import data as d


class Player:
    """a simple object which holds all of the player data, and generates a player."""
    def __init__(self):
        self.user_class = None
        self.user_race = None
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
        self.speed = None
        self.spells = []

    def setup(self):
        """Grabs info from the user, then calls the generator function"""
        while not self.user_race or not self.user_class:
            user_input = str.title(input(f'Select a Race\n{", ".join(list(d.races))}\nand class\n{", ".join(list(d.classes))}\n[Enter] for random\n'))
            if 'Half ' in user_input:
                user_input = user_input.replace('Half ', 'Half-')
            self.user_race = [item for item in user_input.split(' ') if item in d.races] or [random.choice(list(d.races))]
            self.user_class = [item for item in user_input.split(' ') if item in d.classes] or [random.choice(list(d.classes))]
        self.user_class = self.user_class[0]
        self.user_race = self.user_race[0]
        self.generate_character()

    @staticmethod
    def roll_dice(roll):
        """rolls X dice of Y value, dropping the Z lowest, accepting the standard format
        of 'XdYdZ'"""
        values = [int(s) for s in roll.split('d') if s.isdigit()]
        rolls = sorted([random.randint(1, values[1]) for _ in range(values[0])])
        return sum(rolls[len(values) == 3*values[-1]:])

    def generate_character(self):
        """Generates a fully featured level 1 character as a Player object, which is really just a
        holder for a dict"""
        self.languages = ['Common']
        for item in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            self.stats[item] = self.roll_dice('4d6d1')
        for stat in self.stats:
            if stat in d.races[self.user_race]:
                self.stats[stat] += d.races[self.user_race][stat]
            self.stats['int'] = max(self.stats['int'], 3)
            self.stat_mods[stat] = (self.stats[stat] - 10) // 2
        if 'languages' in d.races[self.user_race]:
            self.languages += [d.races[self.user_race]['languages'][0]]
        self.alignment = random.choice(d.align_chart)
        self.skin_tone = random.choice(d.skin_tones)
        self.hair_color = random.choice(d.hair_colors)
        self.hair_type = random.choice(d.hair_types)
        self.eye_color = random.choice(d.eye_colors)
        self.age = d.races[self.user_race]['age'][0] + self.roll_dice(d.races[self.user_race]['age'][1])
        self.height = d.races[self.user_race]['height'][0] + self.roll_dice(d.races[self.user_race]['height'][1])
        self.weight = d.races[self.user_race]['weight'][0] + (self.roll_dice(d.races[self.user_race]['weight'][1]) * (self.height - d.races[self.user_race]['height'][0]))
        self.size = d.races[self.user_race]['size']
        self.speed = d.races[self.user_race]['speed']
        self.deity = random.choice(list(d.deities))
        self.gold = self.roll_dice(d.classes[self.user_class]['gold']) * 10
        self.health = d.classes[self.user_class]['health'] + self.stat_mods['con']
        skill_points = max(d.classes[self.user_class]['xp'] + self.stat_mods['int'], 1)
        possible_skills = d.classes[self.user_class]['skills']

        if self.user_race == 'Dwarf':
            self.name = f'{random.choice(d.races["Dwarf"]["first names"])} {random.choice(d.races["Dwarf"]["last names"])}, of the clan {random.choice(d.races["Dwarf"]["clans"])}'

        elif self.user_race == 'Elf':
            self.name = f'{random.choice(d.races["Elf"]["first names"])} {random.choice(d.races["Elf"]["last names"])}'

        elif self.user_race == 'Halfling':
            self.name = f'{random.choice(d.races["Halfling"]["first names"])} {random.choice(d.races["Halfling"]["last names"])}'

        elif self.user_race == 'Gnome':
            self.name = f'{random.choice(d.races["Gnome"]["first names"])} "{random.choice(d.races["Gnome"]["nick names"])}" {random.choice(d.races["Gnome"]["last names"])}, of the clan {random.choice(d.races["Gnome"]["clans"])}'

        elif self.user_race == 'Half-Elf':
            tribe = random.choice(d.races["Human"]['tribes'])
            self.name = f'{random.choice(d.races["Human"]["first names"][tribe] + d.races["Elf"]["first names"])} {random.choice(d.races["Human"]["first names"][tribe] + d.races["Elf"]["last names"])}'
            if self.roll_dice('1d2') == 2:
                self.name += ' of the clan ' + tribe
            self.languages += ['Elf']

        elif self.user_race == 'Half-Orc':
            tribe = random.choice(d.races["Human"]['tribes'])
            if self.roll_dice('1d2') == 2:
                self.name = random.choice(d.races["Half-Orc"]['first names'])
            else:
                self.name = f'{random.choice(d.races["Human"]["first names"][tribe] + d.races["Half-Orc"]["first names"])} {random.choice(d.races["Human"]["first names"][tribe])}'
                if self.roll_dice('1d10') > 7:
                    self.name += f', of the tribe {tribe}'

        else:
            tribe = random.choice(d.races["Human"]['tribes'])
            self.name = f'{random.choice(d.races["Human"]["first names"][tribe])} {random.choice(d.races["Human"]["first names"][tribe])}, of the clan {tribe}'
            self.languages += [random.choice([item for item in d.languages if item not in self.languages])]
            self.feats += [random.choice(d.feats)]
            skill_points += 1

        if self.stat_mods['int'] > 0:
            if 'languages' in d.races[self.user_race]:
                self.languages += random.sample([item for item in d.races[self.user_race]['languages'] if item not in self.languages], min(self.stat_mods['int'], len(d.races[self.user_race]['languages']) - len(self.languages)))
            else:
                self.languages += random.sample([item for item in d.languages if item not in self.languages], self.stat_mods['int'])

        if self.user_class == 'Barbarian':
            self.deity = random.choice(d.classes[self.user_class]['deities'])
            self.weapon = random.choice([i for i in d.weapons if d.weapons[i]['Rarity'] in ['Simple Weapons', 'Martial Weapons']] + ['Waraxe, dwarven', 'Urgrosh, dwarven'] * int(self.user_race == 'Dwarf'))
            self.shield = random.choice(list(d.shields))
            self.armor = random.choice(d.classes[self.user_class]['armor'])
            self.alignment = random.choice([item for item in d.align_chart if item[0] not in 'Lawful'])
            self.speed += 10

        elif self.user_class == 'Bard':
            self.weapon = random.choice(d.classes[self.user_class]['weapons'])
            self.shield = random.choice([i for i in d.shields if d.shields[i]['Class'] == 'Light'])
            self.armor = random.choice([i for i in d.armor if d.armor[i]['Class'] == 'Light'])
            self.alignment = random.choice([item for item in d.align_chart if item[0] not in 'Lawful'])
            self.spells = random.sample(d.classes[self.user_class]['spells'], 4)
            self.deity = 'Fharlanghn'
            if self.user_race == 'Elf':
                self.deity = 'Corellon Larethian'
            elif 'Chaotic' in self.alignment:
                self.deity = 'Olidammara'
            elif 'Good' in self.alignment:
                self.deity = 'Pelor'
            elif 'Evil' in self.alignment:
                self.deity = 'Erythnul'

        elif self.user_class == 'Cleric':
            if 'deity' in d.races[self.user_race] and self.roll_dice('1d2') == 2:
                self.deity = d.races[self.user_race]['deity']
            self.alignment = d.align_chart[random.choice(d.classes[self.user_class]['alignment'][d.deities[self.deity]['alignment']])]
            self.weapon = d.deities[self.deity]['weapon']
            self.armor = random.choice(d.classes[self.user_class]['armor'])
            self.shield = random.choice(list(d.shields))
            self.domains = random.sample([i for i in d.deities[self.deity]['domains'] if i not in ['Lawful', 'Chaotic', 'Good', 'Evil']] + [i for i in self.alignment if i in ['Lawful', 'Chaotic', 'Good', 'Evil']], 2)  # A cleric can select an alignment domain (Chaos, Evil, Good, or Law) only if his alignment matches that domain.
            for item in self.domains:
                self.spells += [d.classes[self.user_class][item]]
            self.languages += [random.choice(d.classes['Cleric']['languages'])]
            if 'War' in self.domains:
                self.feats += ['Weapon Focus']
            if 'Trickery' in self.domains:
                possible_skills.update(['bluff', 'disguise', 'hide'])
            if 'Travel' in self.domains:
                possible_skills.add('Survival')
            if 'Plant' in self.domains or 'Animal' in self.domains:
                possible_skills.add('Knowledge, Nature')
            if 'Knowledge' in self.domains:
                possible_skills.update([f'Knowledge ({i})' for i in ['arcana', 'architecture and engineering', 'dungeoneering', 'geography', 'history', 'local', 'nature', 'nobility and royalty', 'religion', 'the planes']])

        elif self.user_class == 'Druid':
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

        elif self.user_class == 'Fighter':
            self.weapon = random.choice([i for i in d.weapons if d.weapons[i]['Rarity'] in ['Simple Weapons', 'Martial Weapons']] + ['Waraxe, dwarven', 'Urgrosh, dwarven'] * int(self.user_race == 'Dwarf'))
            self.shield = random.choice(list(d.shields))
            self.armor = random.choice(list(d.armor))
            self.deity = random.choice(d.classes[self.user_class]['deities'])
            self.feats += [random.choice(d.feats)]

        elif self.user_class == 'Monk':
            self.alignment = random.choice([item for item in d.align_chart if item[0] in 'Lawful'])
            self.weapon = random.choice(d.classes[self.user_class]['weapons'])
            if self.roll_dice('1d10') == 10:
                self.armor = random.choice([i for i in d.armor if d.armor[i]['Class'] == 'Light'])
                self.shield = random.choice([i for i in d.shields if d.shields[i]['Class'] == 'Light'])
            else:
                self.shield = 'None'
                self.weapon = 'Unarmed'
            if not self.armor:
                self.armor_class = 10 + d.armor['None']['Armor Bonus'] + d.shields[self.shield]['Armor Bonus'] + self.stat_mods['wis']
            self.feats += ['Improved Unarmed Strike', random.choice(['Improved Grapple', 'Stunning Fist'])]

        elif self.user_class == 'Paladin':
            self.armor = random.choice(list(d.armor))
            self.shield = random.choice(list(d.shields))
            self.weapon = random.choice(list(d.weapons))
            self.alignment = ('Lawful', 'Good')

        elif self.user_class == 'Ranger':
            self.armor = random.choice([i for i in d.armor if d.armor[i]['Class'] == 'Light'])
            self.shield = random.choice([i for i in d.shields if d.shields[i]['Class'] == 'Light'])
            self.weapon = random.choice([i for i in d.weapons if 'Ranged' in d.weapons[i]['Weapon Type']])
            self.favored_enemy = random.choice(d.classes[self.user_class]['favored enemies'])
            self.feats += ['Track']

        elif self.user_class == 'Rogue':
            self.armor = random.choice([i for i in d.armor if d.armor[i]['Class'] == 'Light'])
            self.weapon = random.choice(d.classes[self.user_class]['weapons'])
            self.deity = random.choice(list(d.deities))

        elif self.user_class == 'Sorcerer':
            self.weapon = random.choice([i for i in d.weapons if 'Simple' in d.weapons[i]['Rarity']])
            print([i for i in d.weapons if 'Simple' in d.weapons[i]['Rarity']])
            if self.roll_dice('1d2') == 2:
                self.deity = None
            self.familiar = random.choice(d.familiars)
            if self.familiar == 'Toad':
                self.health += 3

        else:
            self.weapon = random.choice(d.classes[self.user_class]['weapons'])
            self.feats += ['Scribe Scroll']
            if self.roll_dice('1d10') > 7:
                self.feats += ['Spell Mastery']
            self.familiar = random.choice(d.familiars)
            if self.familiar == 'Toad':
                self.health += 3
            if self.roll_dice('1d10') > 7 and len(self.languages) > 1:
                self.languages.pop()
                self.languages += ['Draconic']
            self.school = random.choice(list(d.classes[self.user_class]['schools']))
            self.forbidden_schools = random.sample([item for item in list(d.classes[self.user_class]['schools']) if item[0] not in self.school], 2 - int(self.school == 'Divination'))

        if skill_points > len(d.classes[self.user_class]['skills']):
            skill_points = len(d.classes[self.user_class]['skills'])
        if self.stats['str'] > 12:
            possible_skills.add('Power Attack')
        if self.stats['dex'] > 12:
            possible_skills.add('Dodge')
        if self.stats['int'] > 12:
            possible_skills.add('Combat Experience')
        if self.stats['dex'] > 12:
            possible_skills.add('Two Weapon Fighting')
        self.skills += random.sample(possible_skills, skill_points)

        if self.weapon and d.weapons[self.weapon]['Weapon Type'] in ['Two-Handed Melee Weapons', 'Ranged Weapons']:
            self.shield = 'None'

        if not self.armor_class:
            self.armor_class = 10 + d.armor[self.armor]['Armor Bonus'] + d.shields[self.shield]['Armor Bonus']

        if self.alignment == ('Neutral', 'Neutral'):
            self.alignment = ('True', 'Neutral')

        self.arcane_failure = d.armor[self.armor]['Arcane Spell Failure'] + d.shields[self.shield]['Arcane Spell Failure']

        if sum([self.stats[item] for item in self.stats]) > 0:
            print('\n\n')
            for item in self.__dict__:
                if self.__dict__[item]:
                    print(f'{item}: {self.__dict__[item]}')
            print('\n\n')


if __name__ == '__main__':
    PLAYER = Player()
    PLAYER.setup()
