import yaml
from pathlib import Path

p = Path("./tournaments/DivisionC")

t = [x for x in p.iterdir()]

x = t[0]

with x.open() as fin:
    content = yaml.safe_load(fin)

tournament_details = content["Tournament"]
events = content["Events"]
teams = content["Teams"]
placings = content["Placings"]

# print(tournament_details['date'])

for team in teams:
    print(team['school'])

print(teams)



def _details():
    def dfs(tag, subd, indentation):
        print(" " * indentation * 4 + tag)
        if isinstance(subd[tag], dict):
            for subtag in subd[tag]:
                dfs(subtag, subd[tag], indentation + 1)
        elif isinstance(subd[tag], list):
            for subdict in subd[tag]:
                print(" " * indentation * 8 + str(subdict))
        else:
            print(" " * indentation * 8 + str(subd[tag]))

    for tag in content:
        dfs(tag, content, 1)

