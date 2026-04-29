# Marvel Rivals Manual — Enhancement Proposals

## Current State Summary

The manual currently has **231 locations** built around:
- Per-hero: Play as, Win as, Use [Ability], Use [Team-Up Ability] (~3–5 checks per hero)
- Faction group games: 1/2/4 Fantastic 4, 1/3/5/7/10 Mutants, etc.
- Game mode checks: Quick Match play/win, Practice vs AI (Easy/Normal/Hard) play/win

---

## 1. Extended Per-Hero Checks

Each hero currently has 3–5 checks. Adding more per-hero checks is the easiest win and makes every hero feel more fully explored.

### 1a. Win Streak / Mastery Checks

For every hero, add:

| Check | Requires |
|---|---|
| Win 3 games as [Hero] | `\|@Game Mode:1\| AND \|[Hero]\|` |
| Win 5 games as [Hero] | `\|@Game Mode:1\| AND \|[Hero]\|` |

These gates mastery behind repeated play rather than a single lucky win.

### 1b. Performance Milestone Checks

For every hero, add 1–2 stat-based goals appropriate to their role:

**Vanguards** (tanks):
- Absorb 10,000 damage in a single match as [Hero]

**Duelists** (damage):
- Get 10 eliminations across any number of matches as [Hero]

**Strategists** (support):
- Heal 10,000 HP in a single match as [Hero]


### 1c. Ultimate Ability Checks

For every hero, add:
- **Use [Hero]'s Ultimate ability** — tracked separately from regular abilities

This uses the same require pattern as existing ability checks: `|@Game Mode:1| AND |[Hero]|`

## 2. Full-Faction Win Checks (Requires Entire Roster Unlocked)

These are the "win a game with all the Avengers" style checks the user specifically requested. Each requires the player to have **all members of a faction** unlocked.

### 2a. Avengers Full Lineup (8 members)

Current Avengers roster: Bruce Banner, Doctor Strange, Black Panther, Iron Man, Thor, Captain America, Hawkeye, Black Widow

```json
{
  "name": "Win a game with ALL the Avengers",
  "requires": "|@Game Mode:1| AND |Bruce Banner| AND |Doctor Strange| AND |Black Panther| AND |Iron Man| AND |Thor| AND |Captain America| AND |Hawkeye| AND |Black Widow|"
}
```

Or equivalently using the category count (requires all 8 Avengers):
```json
{
  "name": "Win a game with ALL the Avengers",
  "requires": "|@Game Mode:1| AND |@Avenger:8|"
}
```

### 2b. Fantastic Four Complete Team (4 members)

All four must be unlocked: The Thing, Human Torch, Mister Fantastic, Invisible Woman

```json
{
  "name": "Win a game with the Complete Fantastic Four",
  "requires": "|@Game Mode:1| AND |@Fantastic 4:4|"
}
```

*(This one already exists as "Complete a Game with 4 Members of the Fantastic 4" — it can be kept or rephrased to distinguish "any 4 from pool" vs "you own all 4".)*

### 2c. All Guardians of the Galaxy (5 members)

Mantis, Rocket Raccoon, Groot, Star-Lord, Adam Warlock

```json
{
  "name": "Win a game with ALL the Guardians of the Galaxy",
  "requires": "|@Game Mode:1| AND |@Guardians of the Galaxy:5|"
}
```

### 2d. All Agents of Atlas (3 members)

Luna Snow, Iron Fist, White Fox

```json
{
  "name": "Win a game with ALL the Agents of Atlas",
  "requires": "|@Game Mode:1| AND |@Agents of Atlas:3|"
}
```

### 2e. All-Villain Team (requires owning 6 villains)

The Punisher, Loki, Ultron, Hela, Venom, Winter Soldier — pure villain team-up

```json
{
  "name": "Win a game where your entire team is Villains (6 Villains)",
  "requires": "|@Game Mode:1| AND |@Villain:6|"
}
```

### 2f. Mutant Brotherhood (requires 6 mutants)

Storm, Magik, Magneto, Emma Frost, Psylocke, Wolverine

```json
{
  "name": "Win a game with 6 Mutants on your team",
  "requires": "|@Game Mode:1| AND |@Mutant:6|"
}
```

## 4. Map-Specific Checks

Marvel Rivals maps organized by zone. Checks only require **visiting/playing** a map — not winning — to keep them accessible and low-friction.

### Map Roster (20 maps)

| Map | Zone | Mode |
|---|---|---|
| Yggsgard: Royal Palace | Yggsgard | Domination |
| Yggsgard: Yggdrasil Path | Yggsgard | Convoy |
| Tokyo 2099: Shin-Shibuya | Tokyo 2099 | Convergence |
| Tokyo 2099: Spider-Islands | Tokyo 2099 | Convoy |
| Tokyo 2099: Ninomaru | Tokyo 2099 | Conquest |
| Intergalactic Empire of Wakanda: Hall of Djalia | Intergalactic Empire of Wakanda | Convergence |
| Intergalactic Empire of Wakanda: Birnin T'Challa | Intergalactic Empire of Wakanda | Domination |
| Hydra Charteris Base: Hell's Heaven | Hydra Charteris Base | Domination |
| Empire of Eternal Night: Midtown | Empire of Eternal Night | Convoy |
| Empire of Eternal Night: Central Park | Empire of Eternal Night | Convergence |
| Empire of Eternal Night: Sanctum Sanctorum | Empire of Eternal Night | Doom Match |
| Hellfire Gala: Krakoa | Hellfire Gala | Domination |
| Hellfire Gala: Arakko | Hellfire Gala | Convoy |
| Klyntar: Symbiotic Surface | Klyntar | Convergence |
| Klyntar: Celestial Husk | Klyntar | Domination |
| Klyntar: Throne of Knull | Klyntar | Resource Rumble |
| K'un-Lun: Heart of Heaven | K'un-Lun | Convergence |
| Lower Manhattan | New York City | Convergence |
| Museum of Contemplation | Standalone | Convoy |
| Grand Garden | Arena | Annihilation (18v18) |

### 4a. Play on Each Map (Visit Checks)

One check per map — just play a match on it, no win required:

```json
{ "name": "Play a match on Yggsgard: Royal Palace", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Yggsgard: Yggdrasil Path", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Tokyo 2099: Shin-Shibuya", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Tokyo 2099: Spider-Islands", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Tokyo 2099: Ninomaru", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Intergalactic Empire of Wakanda: Hall of Djalia", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Intergalactic Empire of Wakanda: Birnin T'Challa", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Hydra Charteris Base: Hell's Heaven", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Empire of Eternal Night: Midtown", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Empire of Eternal Night: Central Park", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Empire of Eternal Night: Sanctum Sanctorum", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Hellfire Gala: Krakoa", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Hellfire Gala: Arakko", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Klyntar: Symbiotic Surface", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Klyntar: Celestial Husk", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Klyntar: Throne of Knull", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on K'un-Lun: Heart of Heaven", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Lower Manhattan", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Museum of Contemplation", "requires": "|@Game Mode:1|" },
{ "name": "Play a match on Grand Garden", "requires": "|@Game Mode:1|" }
```

### 4b. Play on Every Map (Map Grand Tour)

```json
{
  "name": "Play a match on every map (Map Grand Tour)",
  "requires": "|@Game Mode:1|"
}
```

### 4c. Hero + Map Thematic Combination Checks

Play a specific hero on a thematically linked map — no win required, just set foot there together.

| Check | Requires | Thematic Link |
|---|---|---|
| Play on Hellfire Gala: Krakoa as a Mutant | `\|@Game Mode:1\| AND \|@Mutant:1\|` | Krakoa is the Mutant homeland |
| Play on Hellfire Gala: Arakko as a Mutant | `\|@Game Mode:1\| AND \|@Mutant:1\|` | Arakko is the mutant colony world |
| Play on Intergalactic Empire of Wakanda: Hall of Djalia as Black Panther | `\|@Game Mode:1\| AND \|Black Panther\|` | Wakanda map |
| Play on Intergalactic Empire of Wakanda: Birnin T'Challa as Black Panther | `\|@Game Mode:1\| AND \|Black Panther\|` | Wakanda map |
| Play on Yggsgard: Royal Palace as Thor | `\|@Game Mode:1\| AND \|Thor\|` | Asgard is Thor's home |
| Play on Yggsgard: Royal Palace as Loki | `\|@Game Mode:1\| AND \|Loki\|` | Loki's realm |
| Play on Yggsgard: Yggdrasil Path as Thor | `\|@Game Mode:1\| AND \|Thor\|` | Asgard is Thor's home |
| Play on Tokyo 2099: Spider-Islands as Spider-Man | `\|@Game Mode:1\| AND \|Spider-Man\|` | Spider-Man in the Tokyo spider-verse |
| Play on Tokyo 2099: Spider-Islands as Black Cat | `\|@Game Mode:1\| AND \|Black Cat\|` | Spider adjacency |
| Play on Klyntar: Symbiotic Surface as Venom | `\|@Game Mode:1\| AND \|Venom\|` | Klyntar is the symbiote homeworld |
| Play on Klyntar: Celestial Husk as Venom | `\|@Game Mode:1\| AND \|Venom\|` | Symbiote map |
| Play on Hydra Charteris Base: Hell's Heaven as a Villain | `\|@Game Mode:1\| AND \|@Villain:1\|` | Hydra = Villain territory |
| Play on Empire of Eternal Night: Midtown as Iron Man | `\|@Game Mode:1\| AND \|Iron Man\|` | NYC Avenger |
| Play on Empire of Eternal Night: Central Park as Doctor Strange | `\|@Game Mode:1\| AND \|Doctor Strange\|` | NYC Sorcerer Supreme |
| Play on Empire of Eternal Night: Sanctum Sanctorum as Doctor Strange | `\|@Game Mode:1\| AND \|Doctor Strange\|` | Strange's Sanctum |
| Play on Lower Manhattan as Daredevil | `\|@Game Mode:1\| AND \|Daredevil\|` | Hell's Kitchen street hero |
| Play on Lower Manhattan as Spider-Man | `\|@Game Mode:1\| AND \|Spider-Man\|` | Spider-Man's NYC turf |
| Play on K'un-Lun: Heart of Heaven as Iron Fist | `\|@Game Mode:1\| AND \|Iron Fist\|` | K'un-Lun is Iron Fist's home |
| Play on Museum of Contemplation as Adam Warlock | `\|@Game Mode:1\| AND \|Adam Warlock\|` | Cosmic/contemplative theme |
| Play on Hellfire Gala: Krakoa as Wolverine | `\|@Game Mode:1\| AND \|Wolverine\|` | Wolverine is a Krakoa resident |
| Play on Hellfire Gala: Krakoa as Magneto | `\|@Game Mode:1\| AND \|Magneto\|` | Magneto co-founded Krakoa |

---

## 5. Game Mode Specific Checks

### 5a. Win Each Mode

```json
{ "name": "Win a Domination match", "requires": "|Quick Match|" },
{ "name": "Win a Convoy match", "requires": "|Quick Match|" },
{ "name": "Win a Convergence match", "requires": "|Quick Match|" },
{ "name": "Win a Clash match", "requires": "|Quick Match|" }
```

### 5b. Win All Modes

```json
{
  "name": "Win every game mode (Domination, Convoy, Convergence, Clash)",
  "requires": "|Quick Match|"
}
```

### 5c. Comeback Victory Checks

```json
{
  "name": "Win a match after being down 2-0",
  "requires": "|Quick Match|"
},
{
  "name": "Win an overtime match",
  "requires": "|Quick Match|"
}
```

---

## 6. Cross-Faction / Multi-Hero Achievement Checks

These require heroes from multiple factions — interesting for players who have collected broadly.

| Check | Requires |
|---|---|
| Win a game with heroes from 3 different factions | `\|@Game Mode:1\| AND \|@Avenger:1\| AND \|@Mutant:1\| AND \|@Villain:1\|` |
| Win a game with an Avenger and a Villain on the same team | `\|@Game Mode:1\| AND \|@Avenger:1\| AND \|@Villain:1\|` |
| Win with a Fantastic 4 member + a Mutant | `\|@Game Mode:1\| AND \|@Fantastic 4:1\| AND \|@Mutant:1\|` |
| Win a game with heroes from every faction | `\|@Game Mode:1\| AND \|@Avenger:1\| AND \|@Fantastic 4:1\| AND \|@Mutant:1\| AND \|@Villain:1\| AND \|@Guardians of the Galaxy:1\| AND \|@Agents of Atlas:1\|` |

---

## 7. Grand Achievement Checks (Late Game)

These are high-value checks requiring extensive hero collections and serve as alternative victory paths or major milestones.

| Check | Requires | Notes |
|---|---|---|
| Win as every Vanguard | `\|@Game Mode:1\| AND \|@Vanguard:all\|` | Own all Vanguards |
| Win as every Duelist | `\|@Game Mode:1\| AND \|@Duelist:all\|` | Own all Duelists |
| Win as every Strategist | `\|@Game Mode:1\| AND \|@Strategist:all\|` | Own all Strategists |
| Win as every character at least once | `\|@Game Mode:1\| AND \|@Character:all\|` | Own all characters |
| Complete all Avenger individual win checks | Depends on all Avenger win checks | Meta-check |
| Win 50 total matches | `\|@Game Mode:1\|` | Grind milestone |
| Win 100 total matches | `\|@Game Mode:1\|` | Endgame grind |

---

## 8. Implementation Notes

### Adding Items for New Tags

If map-based checks are added, a clean approach is to add **Map items** to `items.json`. This would let the randomizer give players specific maps to "unlock" (restricting which maps they can play), similar to how heroes are locked.

```json
{
  "name": "Hall of Djalia",
  "category": ["Map", "Wakanda Map", "Domination Map"],
  "progression": true
}
```

Then map checks would require: `|@Game Mode:1| AND |Hall of Djalia|`

This adds a whole new layer of randomization — players must unlock maps AND heroes.

### Role Category Items

The items currently have `Vanguard`, `Duelist`, `Strategist` tags on characters. Role-based checks (Section 3) already work using `@Vanguard:3` syntax without any changes.

### Win Streak Tracking

Win streak checks (Win 3 games as [Hero], Win 5 games) need to be tracked manually in the Manual client — the player marks it when achieved. This is consistent with how all other Manual checks work.

### Suggested Priority Order

1. **High Priority** — Per-hero Ultimate ability checks (easy to add, one per hero)
2. **High Priority** — Map win checks (12 checks, adds map variety)
3. **High Priority** — Full faction win checks (the "win with all Avengers" style)
4. **Medium Priority** — Hero + map thematic combinations (flavor and immersion)
5. **Medium Priority** — Role-based composition checks
6. **Medium Priority** — Win streak / mastery checks per hero
7. **Lower Priority** — Map items added to the randomizer pool (biggest structural change)

---

## 9. Estimated New Check Count

| Category | New Checks |
|---|---|
| Per-hero: Win 3 games | ~46 |
| Per-hero: Win 5 games | ~46 |
| Per-hero: Ultimate ability | ~46 |
| Per-hero: Performance milestone | ~92 (2 per hero) |
| Full faction wins | 6 |
| Role composition | 8 |
| Play on each map (visit) | 20 |
| Map Grand Tour | 1 |
| Hero + map thematic combos | 21 |
| Game mode specific | 6 |
| Cross-faction | 4 |
| Grand achievements | 8 |
| **Total new** | **~304** |

Current total: 231 → **New total: ~535 checks**

This roughly doubles the content while keeping all new checks consistent with the existing requirement format.
