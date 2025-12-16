# AI Coding Agent Instructions for BattleTEst

## Overview
BattleTEst is a whimsical console-based RPG game where players recruit heroes to defend artifacts in a pastel suburb. The game features turn-based combat, random enemy encounters, and exploration of themed locations (casino, blacksmith, store, restaurant).

## Architecture
- **Core Loop**: `main.py` initializes a Player and runs an infinite battle loop (normal enemies every fight, bosses every 5th). Post-combat handles item/gold drops and stat recovery.
- **Modular Places**: Each location (e.g., `places/casino/`) is a self-contained module with its own menu and logic, called from gameplay.
- **Class Hierarchy**: Player types (warrior, basement dweller, boat man, ninja) inherit base stats with unique specials. Enemies/Bosses have randomized drops.
- **Online/Offline Modes**: Internet connectivity determines store access (online uses APIs for pricing, offline uses cached data).

## Key Components
- `gameplay/gameplay.py`: Battle logic, character creation intro, post-combat rewards.
- `classes/player/createPlayer.py`: Player class with type-based stats, inventory, party system.
- `classes/enemy.py`: Enemy/Boss classes with drops (gold or StoreItems).
- `places/`: Submodules for locations; e.g., casino includes blackjack, case opening, horse racing.
- `audioMixer.py`: Pygame-based sound management.
- `images/openPicture.py`: PIL-based image display for locations.

## Workflows
- **Run Game**: `python main.py` (requires pygame, PIL, etc. from requirements.txt).
- **Install Deps**: `pip install -r requirements.txt`.
- **Online Features**: Store uses `csgo_market_api` for real-time pricing; leaderboard posting via JS (currently placeholder).
- **Debugging**: Print statements for battle logs; no formal logging or tests.

## Conventions
- **Player Types**: Stats and specials defined in Player.__init__; color modifies base stats (e.g., blue +10 health).
- **Combat**: Turn-based with success rolls (random.randint); specials consume mana.
- **Drops**: Random from enemy.drop tuple; items auto-equip if armor/weapon, else prompt storage.
- **Error Handling**: "Bad boy" flag for invalid inputs, skipping rewards.
- **Imports**: Conditional for online/offline (e.g., store modules).
- **Audio/Images**: Always initialize SoundManager; use relative paths for assets.

## Examples
- Add new enemy: Extend `Enemy.__init__` with kind, stats, drop tuple (e.g., `StoreItems(name, amount, ...)`).
- New special: Create `Special(name, type, attack/heal, mana_cost)` in Player.attacks.
- Location integration: Add menu option in gameplay, call `openLocation(player)` function.