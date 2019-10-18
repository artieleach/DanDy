import random
import data as d
import time


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
        self.armor = None
        self.shield = None
        self.weapon = None
        self.religion = None
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
            user_input = str.title(input(f'Select a Race\n{d.race_list}\nand class\n{d.class_list}\n[Enter] for random\n'))
            if 'Half ' in user_input:
                user_input = user_input.replace('Half ', 'Half-')
            self.user_race = [item for item in user_input.split(' ') if item in d.race_list] or [random.choice(d.race_list)]
            self.user_class = [item for item in user_input.split(' ') if item in d.class_list] or [random.choice(d.class_list)]
        self.user_class = self.user_class[0]
        self.user_race = self.user_race[0]
        self.generate_character()

    @staticmethod
    def roll_dice(roll):
        values = [int(s) for s in roll.split('d') if s.isdigit()]
        top_rolls = sorted(list(random.randint(1, values[1]) for _ in range(values[0])))
        return sum(top_rolls[len(values) == 3*values[-1]:])

    @staticmethod
    def stat_mod(skill):
        return (skill - 10) // 2

    def generic_input(self, choices, num_of_choices=1):
        res = []
        for answer in range(num_of_choices):
            cur_ans = input(f'{choices}\n')
            if [item for item in cur_ans.split(' ') if item in choices]:
                res += cur_ans
            else:
                pass
        if len(res) == 1:
            return res[0]
        else:
            return res

    def generate_character(self):
        self.languages = ['Common']
        for item in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            self.stats[item] = self.roll_dice('4d6d1')
        self.alignment = random.choice(d.align_chart)
        self.skin_tone = random.choice(d.human_skin_tones)
        self.hair_color = random.choice(d.human_hair_colors)
        self.hair_type = random.choice(d.human_hair_types)
        self.eye_color = random.choice(d.human_eye_colors)

        if self.user_race == 'Dwarf':
            self.name = f'{random.choice(d.dwarf_first_names)} {random.choice(d.dwarf_last_names)}, of the clan {random.choice(d.dwarf_clans)}'
            self.age = 40 + self.roll_dice('5d6')
            self.height = self.roll_dice('2d4') + 45
            self.weight = 130 + (self.roll_dice('2d6') * (self.height-45))
            self.stats['con'] += 2
            self.stats['cha'] -= 2
            self.size = 1
            self.languages += ['Dwarven']
            if self.roll_dice('1d10') > 7:
                self.religion = 'Moradin'
        
        if self.user_race == 'Elf':
            self.name = f'{random.choice(d.elf_first_names)} {random.choice(d.elf_last_names)}'
            self.age = 110 + self.roll_dice('6d6')
            self.height = 58 + self.roll_dice('2d6')
            self.weight = 85 + (self.roll_dice('1d6') * self.height - 58)
            self.stats['dex'] += 2
            self.stats['con'] -= 2
            self.languages += ['Elven']
            self.size = 1
            if self.roll_dice('1d10') > 7:
                self.religion = 'Corellon Larethian'

        if self.user_race == 'Halfling':
            self.name = f'{random.choice(d.halfling_first_names)} {random.choice(d.halfling_last_names)}'
            self.age = 20 + self.roll_dice('3d6')
            self.height = self.roll_dice('2d4') + 32
            self.weight = 30 + (self.roll_dice('1d1') * (self.height - 32))  # i decided to use 1d1 instead of removing the * to keep this consistent with the rest of the races
            self.stats['dex'] += 2
            self.stats['str'] -= 2
            self.languages += ['Halfling']
            self.size = 2

        if self.user_race == 'Gnome':
            self.name = f'{random.choice(d.gnome_first_names)} "{random.choice(d.gnome_nick_names)}" {random.choice(d.gnome_last_names)}, of the clan {random.choice(d.gnome_clans)}'
            self.age = 40 + self.roll_dice('6d6')
            self.height = self.roll_dice('2d4') + 36
            self.weight = 40 + (self.roll_dice('1d6') * (self.height - 36))
            self.stats['con'] += 2
            self.stats['str'] -= 2
            self.languages += ['Gnome']
            self.size = 2

        if self.user_race == 'Half-Elf':
            tribe = random.choice(list(d.human_last_names.keys()))
            self.name = f'{random.choice(list(d.human_first_names[tribe]) + list(d.elf_first_names))} {random.choice(list(d.human_first_names[tribe]) + list(d.elf_last_names))}'
            if self.roll_dice('1d2') == 2:
                self.name += ' of the clan ' + tribe
            self.age = 20 + self.roll_dice('2d6')
            self.height = self.roll_dice('2d8') + 55
            self.weight = 100 + (self.roll_dice('2d4') * (self.height - 55))
            self.languages += ['Elven']
            self.size = 1

        if self.user_race == 'Half-Orc':
            tribe = random.choice(list(d.human_last_names.keys()))
            if self.roll_dice('1d2') == 2:
                self.name = random.choice(d.orc_first_names)
            else:
                self.name = f'{random.choice(list(d.human_first_names[tribe]) + list(d.orc_first_names))} {random.choice(list(d.human_first_names[tribe]))}'
                if self.roll_dice('1d10') > 7:
                    self.name += f',of the tribe {tribe}'
            self.age = 14 + self.roll_dice('1d6')
            self.height = self.roll_dice('2d12') + 58
            self.weight = 150 + (self.roll_dice('2d6') * (self.height-58))
            self.stats['int'] -= 2
            self.stats['cha'] -= 2
            self.stats['str'] += 2
            self.languages += ['Orc']
            self.size = 1

        if self.user_race == 'Human':
            tribe = random.choice(list(d.human_last_names.keys()))
            self.age = 15 + self.roll_dice('1d6')
            self.height = self.roll_dice('2d4') + 58
            self.weight = 120 + self.roll_dice('2d6') * (self.height-58)
            self.name = f'{random.choice(list(d.human_first_names[tribe]))} {random.choice(list(d.human_last_names[tribe]))}, of the clan {tribe}'
            self.size = 1
            self.languages += [random.choice([item for item in d.language_list if item not in self.languages])]

        for item in ['str', 'dex', 'con', 'int', 'wis', 'cha']:
            self.stat_mods[item] = (self.stats[item] - 10) // 2

        skill_points = d.class_xp[self.user_class] + self.stat_mods['int']
        self.health = d.class_health[self.user_class] + self.stat_mods['con']

        if self.user_class == 'Barbarian':
            self.weapon = random.choice([i for i in d.weapon_data.keys() if d.weapon_data[i]['Rarity'] in ['Simple Weapons', 'Martial Weapons']])
            self.shield = random.choice(d.shields)
            self.armor = random.choice(d.barbarian_armor)
            self.alignment = random.choice([item for item in d.align_chart if item[0] not in 'Lawful '])
            self.religion = random.choice(d.religions)
            self.gold = self.roll_dice('4d4') * 10

        if self.user_class == 'Bard':
            self.weapon = random.choice(d.bard_weapons)
            self.shield = random.choice([i for i in d.shield_data.keys() if d.shield_data[i]['Class'] == 'Light'])
            self.armor = random.choice(list(d.armor_data.keys()))
            self.alignment = random.choice([item for item in d.align_chart if item[0] not in 'Lawful '])
            if 'Chaotic' in self.alignment[0]:
                self.religion = 'Olidammara'
            elif self.roll_dice('1d2') == 2:
                self.religion = random.choice(['Pelor', 'Corellon Larethian'])
            self.gold = self.roll_dice('4d4') * 10

        if self.user_class == 'Cleric':
            self.religion = random.choice(d.religions)
            self.alignment = random.choice(d.cleric_alignment[d.religion_alignments[self.religion]-1])
            self.weapon = d.religion_weapons[self.religion]
            self.armor = random.choice(d.cleric_armor)
            self.shield = random.choice(d.shields)
            self.domains = random.sample(d.religion_domains[self.religion], 2)
            self.languages += [random.choice(['Celestial', 'Abyssal', 'Infernal'])]
            if 'War' in self.domains:
                self.feats += ['Weapon Focus']
            if ['Animal', 'Plant'] in self.domains:
                self.skills += 'Knowledge, Nature'
            self.gold = self.roll_dice('5d4') * 10

        if self.user_class == 'Druid':
            if self.roll_dice('1d2') == 2:
                self.shield = 'Light Wooden'
                self.weapon = 'Unarmed'
            else:
                self.shield = 'Heavy Wooden'
                self.weapon = random.choice(d.druid_weapons)
            self.armor = random.choice(['Padded', 'Leather', 'Hide'])
            self.religion = random.choice(d.religions)
            self.alignment = d.align_chart[int(random.choice('24568'))]
            self.languages += ['Druidic', 'Sylvan']
            self.familiar = random.choice(d.druid_companions)
            self.gold = self.roll_dice('2d4') * 10

        if self.user_class == 'Fighter':
            self.weapon = random.choice([i for i in d.weapon_data.keys() if d.weapon_data[i]['Rarity'] in ['Simple Weapons', 'Martial Weapons']])
            self.shield = random.choice(d.shields)
            self.armor = random.choice(d.armor)
            self.religion = random.choice(d.fighter_religions)
            self.feats += [random.choice(d.feat_list)]

        if self.user_class == 'Monk':
            self.alignment = random.choice([item for item in d.align_chart if item[0] in 'Lawful '])
            self.weapon = random.choice(d.monk_weapons)
            if self.roll_dice('1d10') == 10:
                self.armor = random.choice([i for i in d.armor_data.keys() if d.armor_data[i]['Class'] == 'Light'])
                self.shield = random.choice([i for i in d.shield_data.keys() if d.shield_data[i]['Class'] == 'Light'])
            else:
                self.shield = 'None'
                self.weapon = 'Unarmed'
            self.religion = random.choice(['Heironeous', 'St. Cuthbert', 'Hextor'] + d.religions)
            if not self.armor:
                self.armor_class = 10 + d.armor_data['None']['Armor Bonus'] + d.shield_data[self.shield]['Armor Bonus'] + self.stat_mods['wis']
            self.feats += ['Improved Unarmed Strike', random.choice(['Improved Grapple', 'Stunning Fist'])]
            self.gold = self.roll_dice('5d4') * 10

        if self.user_class == 'Paladin':
            self.armor = random.choice(d.armor)
            self.shield = random.choice(d.shields)
            self.weapon = random.choice(list(d.weapon_data.keys()))
            self.alignment = ('Lawful ', 'Good')
            self.religion = random.choice(d.religions)
            self.gold = self.roll_dice('6d4') * 10

        if self.user_class == 'Ranger':
            self.armor = random.choice([i for i in d.armor_data.keys() if d.armor_data[i]['Class'] == 'Light'])
            self.shield = random.choice([i for i in d.shield_data.keys() if d.shield_data[i]['Class'] == 'Light'])
            self.weapon = random.choice(d.ranged_weapons)
            self.favored_enemy = random.choice(d.ranger_favored_enemies)
            self.feats += ['Track']
            self.religion = random.choice(d.religions)
            self.gold = self.roll_dice('6d4') * 10

        if self.user_class == 'Rogue':
            self.armor = random.choice([i for i in d.armor_data.keys() if d.armor_data[i]['Class'] == 'Light'])
            self.weapon = random.choice(d.rogue_weapons)
            self.religion = random.choice(d.religions)
            self.gold = self.roll_dice('5d4') * 10

        if self.user_class == 'Sorcerer':
            self.weapon = random.choice(d.ranged_weapons + d.melee_weapons)
            if self.roll_dice('1d2') == 2:
                self.religion = random.choice(d.religions)
            self.familiar = random.choice(d.familiars)
            if self.familiar == 'Toad':
                self.health = 7 + self.stat_mods['con']
            self.gold = self.roll_dice('3d4')

        if self.user_class == 'Wizard':
            self.weapon = random.choice(d.wizard_weapons)
            self.feats += ['Scribe Scroll']
            if self.roll_dice('1d10') > 7:
                self.feats += ['Spell Mastery']
            self.religion = random.choice(d.religions)
            self.familiar = random.choice(d.familiars)
            if self.familiar == 'Toad':
                self.health = 7 + self.stat_mods['con']
            if self.roll_dice('1d10') > 7 and len(self.languages) > 1:
                self.languages.pop()
                self.languages += ['Draconic']
            self.school = random.choice(list(d.wizard_schools.keys()))
            self.forbidden_schools = random.sample([item for item in list(d.wizard_schools.keys()) if item[0] not in self.school], 2 - int(self.school == 'Divination'))

        if self.stat_mods['int'] > 1:
            self.languages += [random.choice([item for item in d.language_list if item[0] not in self.languages])]

        if skill_points < 1:
            skill_points = 1
        if self.user_race == 'Human':
            skill_points += 1
        if skill_points > len(d.skill_list[self.user_class]):
            skill_points = len(d.skill_list[self.user_class]) - 1
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

        if self.weapon and d.weapon_data[self.weapon]['Damage Type'] in ['Two-Handed Melee Weapons', 'Ranged Weapons']:
            self.shield = None

        if not self.armor_class:
            self.armor_class = 10
            if self.armor:
                self.armor_class += d.armor_data[self.armor]['Armor Bonus']
            if self.shield:
                self.armor_class += d.shield_data[self.shield]['Armor Bonus']

        self.skills += random.sample([item for item in d.skill_list[self.user_class] if item[0] not in self.skills], skill_points)

        if self.alignment == ('Neutral ', 'Neutral'):
            self.alignment = ('True ', 'Neutral')

        if self.armor:
            self.arcane_failure = d.armor_data[self.armor]['Arcane Spell Failure']


if __name__ == '__main__':
    m_counter = 0
    while True:
        for u_class in d.class_list:
            for u_race in d.race_list:
                start_time = time.time()
                a = Player(user_class=[u_class], user_race=[u_race])
                a.setup()
                m_counter += 1
                tot = round((time.time() - start_time) * 1000)
                if 10 <= tot:
                    print(f'{m_counter}: {tot}, {a.user_class} {a.user_race}')
    a = Player()
    a.setup()
