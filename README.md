# Dungeon_Crawler
 Experimental space for a Dungeon Crawling RPG.

# Ideas
Here are some ideas I'm considering for game mechanics.

## Heros
The player will control a party of four heroes as they traverse the dungeon.

### Classes
Each hero has a primary class and a subclass within that. Classes determine (among other things) the combat actions available to the hero, which in turn determine which ability scores should be prioritized. Each class corresponds to an archetype that uses a specific ability score (Toughness, Agility, Personality, or Mind), and most subclasses add a flavor of another class to the primary class.
- **WARRIOR** (Might): Frontline tank.
    - **Soldier** (_Base_)
    - **Bruiser** (_Rogue_)
    - **Knight** (_Support_)
    - **Duelist** (_Caster_)
- **ROGUE** (Agility): Damage-dealer, skill-monkey. 
    - **Thief** (_Base_) 
    - **Monk** (_Warrior_)
    - **Brigand** (_Support_)
    - **Scout** (_Caster_)
- **SUPPORT** (Charisma): Buffs allies.
    - **Noble** (_Base_)
    - **Warlord** (_Warrior_)
    - **Beastmaster** (_Rogue_)
    - **Bard** (_Caster_)
- **CASTER** (Mind): Debuffs enemies, buffs themself.
    - **Sage** (_Base_) 
    - **Bloodmage** (_Warrior_)
    - **Spellblade** (_Rogue_)
    - **Priest** (_Support_)

### Stats
- Ability Scores (intrinsic, contributing to other stats and skill bonuses, as well as being factored into combat actions).
    - **Might**
        - Armor capacity
        - Carrying capacity
        - Physical endurance
    - **Agility**
        - Evasion?
        - Initiative
    - **Charisma**
        - NPC interaction skills
    - **Mind**
        - Perception
        - Knowledge skills

- Class (changeable - see above)
- Meters (change throughout gameplay)
    - HP
    - DEFENSE
    - EXHAUSTION

## Entourage
The party can recruit NPCs an other additions to their entourage, who will travel with the party in the overworld and provide services, bonuses, etc while outside of dungeons.

Each member of the entourage requires resources during overworld travel.

**Entourage inefficiency:** The more elements in the entourage, the less efficiently the party can travel (requiring more time).

For example:

- Traveling Blacksmith (buy/repair weapons and armor)
- Traveling Tinker (buy/craft items)
- Mule (increase entourage inventory)
- Draft Horse (increase entourage inventory & decrease entourage efficiency (but won't reduce inefficiency below 0%))
- Ranger (decrease entourage inefficiency)


## Gameplay Panes
There will be four major panes onscreen for the player to view and interact with:

### Heroes Pane
The hero pane shows the Stats, equipped items, etc for each of the four heroes in the party.

### Inventory Pane
The inventory pane shows the items carried by the heroes, their entourage, and their baggage train, as well as the carrying capacity of each.

### Journal Pane
The journal pane shows the quests, objective, log, prior maps, collected information, etc.

### Exploration Pane
The biggest pane, and the one the player will engage with the most during gameplay. There are several tabs of this pane, which will either be switchable or locked depending on gameplay events. The bottom section of this pane will often show an OPTIONS section, which will display exploration or interaction options the party can take in the current tab that are not otherwise selectable in that tab's GUI.
- **OVERWORLD:** Shows the region's map, including nodes, quest markers, and the player's location. Allows the player to control the party's movement and progression.
- **NODE:** Shows the current location within the current node, which could take several forms depending on the location within the node.
    - **Sandbox:** Shows the various options and details for the current location, including different buildings or locations that can be entered.
    - **Dungeon:** Explorable map grid. Player moves party around the grid, encountering monsters, NPCs, curios, treasure, etc.
- **INTERACT:** Shows the current activity in the node (if any), which could take several forms.
    - **Combat:** Shows the current combat.
    - **Curio:** Shows the current curio being interacted with.
    - **NPC:** Shows the current NPC(s) being interacted with.