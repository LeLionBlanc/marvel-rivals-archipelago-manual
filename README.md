# Marvel Rivals — Manual Archipelago Randomizer


## What is this?

This is a **Manual** Archipelago randomizer for **Marvel Rivals**. Because Marvel Rivals has no mod support, all check completion is done **manually** — you play the game normally, and when you complete a check (e.g. "Complete a game with a Mutant"), you click the ✅ **Check** button yourself in the Archipelago client.

## Requirements

- [Archipelago](https://archipelago.gg/downloads) (latest version)
- The `Manual_MarvelRivals_DrakeLeLionBlanc.apworld` file placed in your Archipelago `worlds/` folder
- Marvel Rivals (PC)

---

## Installation

1. Download `Manual_MarvelRivals_DrakeLeLionBlanc.apworld`.
2. Place it in your Archipelago installation's `worlds/` folder (e.g. `C:\ProgramData\Archipelago\worlds\`).
3. Launch the Archipelago Launcher and generate a game as usual, selecting **MarvelRivals** as your game.

---

## How to Play

### Starting the Client

1. Open the **Archipelago Launcher**.
2. Click **Manual Client** 
3. Connect to your Archipelago server with your slot name and server address.

### Your Starting State

- You begin with **Quick Match** unlocked — you can play Quick Match games from the start.
- You also start with **two random Character** unlocked.
- Additional characters are **items** received from the multiworld. You can only play as characters you have received.

### Completing Checks

This is the core loop of the randomizer:

1. **Look at your available locations** in the client — these are the checks you can currently attempt based on the items (characters, game modes) you have received.
2. **Play Marvel Rivals** and complete the real in-game action described by the check name (e.g. *"Complete a Game with a Fantastic 4 Member"*).
3. **Come back to the Manual Client** and click the ✅ **Check** button next to that location to send the check to the server.

> ⚠️ **You are on the honour system.** The client cannot verify what you do in-game. Only check off locations you have genuinely completed.

### Check Requirements

Checks are only available when you meet their requirements:

| Requirement shown | Meaning |
|---|---|
| `@Game Mode:1` | You must have received at least 1 Game Mode item (Quick Match counts) |
| `@Fantastic 4:2` | You must have received at least 2 Fantastic 4 characters |
| `@Mutant:5` | You must have received at least 5 Mutant characters |
| `@Character` | You must have received any character |

The client will automatically grey out checks you cannot yet attempt.

---

## Check Categories

| Category | Description |
|---|---|
| **Factions** | Play games using characters from a specific faction (Avengers, Mutants, Villains, Fantastic 4, Guardians of the Galaxy, etc.) |
| **Maps** | Play or win matches on specific maps |
| **Game Modes** | Win matches in Domination, Convoy, Convergence, or Clash |
| **Achievements** | Long-term goals like winning 50 total matches or winning as every character |
| **Characters** | Per-character challenges: win X games, get X eliminations, use their Ultimate, etc. |
| **Blood Hunt** | Complete PvE co-op Blood Hunt missions at various difficulties |

---

## Options

These options are configured when generating your game:

| Option | Default | Description |
|---|---|---|
| **Include Faction Challenges** | On | Adds checks like "Complete a game with 5 Mutants" |
| **Include Map Challenges** | On | Adds checks for playing on specific maps |
| **Include Gamemode Challenges** | On | Adds checks for winning Domination, Convoy, Convergence, Clash matches |
| **Include Achievement Challenges** | On | Adds long-term checks like "Win 50 total matches" |
| **Include Extended Character Challenges** | On | Adds per-character checks (win 3/5 games, 10 elims, 10k dmg/healing, use Ultimate) |
| **Include Blood Hunt Mode** | On | Adds Blood Hunt PvE co-op checks |
| **Blood Hunt Max Difficulty** | Hard | Highest Blood Hunt difficulty included (Normal / Hard / Extreme / Nightmare) |
| **Death Link** | Off | Standard Archipelago Death Link option |

---

## Filler 

- **Filler item:** Chrono Tokens (cosmetic currency, flavour filler)

---

## Tips

- Start by checking which characters you have received — plan your early checks around them.
- Faction checks often require multiple characters from the same faction; prioritise unlocking those.
- "Play X games featuring at least one Y" checks stack — each game counts as long as you have the required character in your team.
- Blood Hunt checks require the **Blood Hunt** game mode item to be received before they become available.
