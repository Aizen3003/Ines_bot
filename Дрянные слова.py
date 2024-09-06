import json
# pamit = {7059447212: {'Apfel': 'яблоко'}}
# xxx = open("wospominania", "w", encoding="UTF-8")
# json.dump(pamit, xxx, ensure_ascii=False, indent=4)
xxx = open("wospominania", "r", encoding="UTF-8")
posnania = json.load(xxx)
print(posnania)