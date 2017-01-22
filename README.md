
#Usage
How to use this generator:
  run main.py with Data.py in the same folder
  the generator should prompt you for a race, you may enter a race, a race and a class, or nothing for a completely random character
  the resulting character will be printed to the commandline.

##Features
This generator will create every aspect of a character as defined in the D&D 3.5 Player's Handbook. That includes:

Name, Age, Class, Race, Alignment, Languages, Feats, (Schools, forbidden schools, domains, and familiars applicable), weapons, armor, shields, armor class, arcane spell failure chance, health points, stats, size type, height, weight, physical descriptions, religion, load, skills, gold, and items.

the generator also accounts for exceptions to rules, such as Paladin's always being Lawful good, Clerics only moving one alignment away from their god's alignment, stat buffs for races, etc.

included inside of the generator is a die roller, which accepts standard 3d6 die formatting. it also supports dropping low rolls, such as 4d6D1.

##About
This was a personal project for me, made in python version 3.4 and 3.5. Due to how little I knew at the beginning of this project, the code is inefficent and can be repetetive.

##Known Bugs
* Only male charaxters are generated
* I made the weapon data a while ago, knowing what I know now, this could be rewritten so there would be no need for mutliple ditionaries.
* if you input something that isn't an actual Race/Class, the generator will break. this is intentional, work on your spelling.
* To my knowlegde, everything is in accordance with standard D&D 3.5, but it is well within reason that there are some exceptions I did not account for.
* while not technically a bug, age is not generated correctly. it should be based upon both race and class, but it is not. this could be fixed with a function which grabs age data for races/classes, but i've yet to think of a concise way to handle this.
* some data is still stores within DanDY.py, rather than data.py
* dicts within dicts could be used to cut down immensely on the redundancy of physical descriptions
