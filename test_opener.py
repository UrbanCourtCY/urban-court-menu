import re
html = open('index.html', encoding='utf-8').read()
# Match only card CONTAINERS: class="card" or class="card deactivated"
# NOT class="card-inner" etc. (those have a dash after "card")
opener = re.compile(r'<div class="card(?:\s[^"]*)?">')
matches = list(opener.finditer(html))
print('Total matches:', len(matches))
# Filter to only card containers (class after "card" starts with space or ends)
card_containers = [m for m in matches if re.match(r'<div class="card(?:\s[^"]*)?">$', m.group())]
print('Card containers:', len(card_containers))
# Separate: class="card" or class="card " not "card-"
good = [m for m in matches if not re.search(r'card-', m.group())]
print('Cards without dash:', len(good))
for m in good[:5]:
    print(' ', repr(m.group()))
