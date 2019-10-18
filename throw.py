'''from bs4 import BeautifulSoup

bs = BeautifulSoup(None, features='html.parser')

results = {}
weap_type = ''
weap_obs = ''
for tr in bs.findAll('tr'):
    td = tr.findAll('td')
    cur_title = tr.findAll('th')
    if cur_title:
        if len(cur_title) == 1:
            weap_type = cur_title[0].string
        else:
            weap_obs = cur_title[0].string
    if td and td[0].string:
        key_vals = ['Cost', 'Dmg (S)', 'Dmg (M)', 'Critical', 'Range Increment', 'Weight', 'Damage Type', 'Weapon Type', 'Rarity']
        vals = [i.string for i in td[1:]] + [weap_type] + [weap_obs]
        out = zip(key_vals, vals)
        results[td[0].string] = {key: value for (key, value) in out}

print('},\n\t'.join(str(results).split('}, ')))
'''


