import json


with open('winners.json','r+') as fp:
    winners = json.load(fp)


def get_data():
    return winners

def add_data(winner):
    """
    :winner -> name of the new dohek
    adds a new dohek to list if name doesn't exists in list
    """
    arr = filter(lambda x: x['name']==winner, winners)
    if len(arr) == 0:
        winners.append({"name": winner, "id": winners[-1]['id'] + 1})
    else:
        print("Already Added")