from main import fightNum, mainCharacter
import json
import datetime


print(f"You got to fight number: {fightNum}!!!")
postChoice = input("Would you like to post this to the leader board?")

if postChoice.lower() in ['yes', 'y', 'sure']:
    entry = {
        'date': str(datetime.date.today()),
        'name': mainCharacter.name,
        'type': mainCharacter.type,
        'fight_number': fightNum
    }
    try:
        with open('leaderboard.json', 'r') as f:
            leaderboard = json.load(f)
    except FileNotFoundError:
        leaderboard = []
    leaderboard.append(entry)
    with open('leaderboard.json', 'w') as f:
        json.dump(leaderboard, f, indent=4)
    
    # Display leaderboard
    leaderboard.sort(key=lambda x: x['fight_number'], reverse=True)
    print("\nTop 5 Leaderboard:")
    for i in range(min(5, len(leaderboard))):
        e = leaderboard[i]
        print(f"{i+1}. {e['name']} ({e['type']}) - Fight {e['fight_number']} on {e['date']}")
    
    # Find current player's rank
    for rank, e in enumerate(leaderboard, 1):
        if (e['date'] == entry['date'] and 
            e['name'] == entry['name'] and 
            e['type'] == entry['type'] and 
            e['fight_number'] == entry['fight_number']):
            print(f"\nYour position: {rank}. {e['name']} ({e['type']}) - Fight {e['fight_number']} on {e['date']}")
            break

