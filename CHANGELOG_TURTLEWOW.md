# Atlas-TW - Turtle WoW Compatibility Fixes Changelog

## Version 9.3.2 [God-Tier] - Localization Sync Update (April 5, 2026)

### 1. Localization Parity
- **Full Sync**: Synchronized all `esES` locale modules (`Bosses`, `Factions`, `ItemSets`, `MapData`, `Spells`, `Zones`) with `enUS` counterparts to reach **0 missing keys**.
- **esMX Support**: Implemented a global alias in the framework to redirect Latin American Spanish clients to the updated `esES` resources.
- **Turtle WoW 1.17/1.18 Ready**: Added 84 missing boss profiles and new world content profiles from the latest private server patches.

### 2. Language & Code Integrity
- **Fragment Cleanup**: Purged non-Spanish fragments (Portuguese/German) from the quest database.
- **Maintenance Tools**: Added Python-based synchronization and auditing scripts to the repository root for future localized content updates.

---

## Version 9.3.1 [God-Tier] - El Séquito del Terror Edition (April 1, 2026)

### Author Information
- **Lead Developer**: DarckRovert / Elnazzareno
- **Technical Assistant**: Antigravity (Advanced AI)
- **Guild**: El Séquito del Terror (@TurtleWoW)

### 1. Visual & Branding Overhaul
- **Clan Identity**: Integrated the official "El Séquito del Terror" skull logo in the main Atlas header.
- **Header Refinement**: Repositioned all functional buttons (Options, Quests, Loot Panel, Filter) to eliminate overlaps with the version string and localization text.
- **Display Name**: Addon now identifies as "Atlas-TW - El Séquito del Terror Edition" in the UI.

### 2. Loot Panel Reconstruction
- **Dimensions**: Widened the bottom Loot Panel to **800px** and increased height to **125px** for a superior browsing experience.
- **Button Normalization**: Standardized all category button widths and Y-offsets to ensure a clean, professional aesthetic in the Spanish localization.

### 3. Technical & Conflict Resolution
- **AtlasLoot Deactivation**: Formally resolved the "Double Atlas" conflict by deactivating legacy AtlasLoot functionality in favor of the modernized Atlas-TW core.
- **Legacy Migration**: Implemented a robust data migration system that automatically absorbs **Wishlists** and **QuickLooks** from `AtlasLootCharDB` into `AtlasTWCharDB` on first load.
- **Version Logic**: Fixed a critical Lua error in the version check module to support the custom "[God-Tier]" string format.

### 4. Localization & Repository
- **Spanish Support**: Updated `esES` locales with the new clan repository link and specific UI fixes.
- **Official Repo**: `https://github.com/DarckRovert/AtlasTW-TurtleWoW-El-Sequito-del-Terror-Edition`

---

## Version 1.51 - Turtle WoW Edition (April 2026)

### Author Information
- **Real Name**: DarckRovert
- **In-Game Character**: Elnazzareno
- **Guild**: El Sequito del Terror
- **Integration Assistant**: Antigravity
- **Date**: April 1, 2026

---

## Major Changes in 1.51-TW

### 1. Synchronization with Upstream 1.51
- Full codebase synchronization with the official 1.51 release.
- Updated all instance and loot data to the latest Turtle WoW standards.
- Integrated the official **Timbermaw Hold** instance map and loot tables.
- Synchronized **PvP Rewards** restructure for patch 1.18.2 compatibility.

### 2. Feature Enhancements
- **ShaguTweaks Integration**: Enhanced equipment comparison support for players using ShaguTweaks.
- **New Tables**: Added dedicated data for *Cloth* and *Disenchanting* categories.
- **Improved Map Data**: Accurate entrance and sub-zone labeling for 1.18.x content.

### 3. Localization & Polish
- Synchronized all localization modules with new 1.51 strings.
- Maintained the custom "El Séquito del Terror" branding and Spanish (esES) quality of life fixes.
- Updated versioning to `9.3.1 [God-Tier]`.

---


## Version 1.50 - Turtle WoW Edition (March 2026)

### Author Information
- **Real Name**: DarckRovert
- **In-Game Character**: Elnazzareno
- **Guild**: El Sequito del Terror
- **Date**: March 23, 2026

---

## Major Changes in 1.50-TW

### 1. Synchronization with Upstream 1.50
- Merged all core improvements from the official `DarckRovert/AtlasTW-TurtleWoW-El-Sequito-del-Terror-Edition` repository.
- Full codebase synchronization keeping the modular localization framework.

### 2. Turtle WoW 1.18.1 Patch Support
- **New Zones**: Integrated data for *Moonwhisper Coast* and *Thorn Gorge*.
- **Faction Rewards**: Added comprehensive loot tables for the *Draenei Exiles* faction.
- **Instance Updates**: Synchronized the latest loot data for *Naxxramas*, *Onyxia's Lair*, and *Blackwing Lair*.
- **Crafting Overhaul**:
    - Profession menus are now organized by skill tier (Apprentice to Artisan).
    - Added new recipes for *Survival*, *Jewelcrafting*, and other professions.

### 3. Maintenance & Polish
- Updated map markers and interface assets.
- Improved pfQuest lookup integration for new 1.18.1 items.
- Full audit for Lua 5.0 compatibility.

---

## Version 1.45 - Turtle WoW Edition (January 2026)

### Author Information
- **Real Name**: DarckRovert
- **In-Game Character**: Elnazzareno
- **Guild**: El Sequito del Terror
- **Date**: January 8, 2026

---

## Overview

This version of Atlas-TW has been specifically adapted for Turtle WoW, replacing the external Babble library dependencies with a modular localization system and fixing all compatibility issues with Turtle WoW's custom content.

---

## Major Changes

### 1. Localization System Overhaul

**Problem**: The original Atlas addon relied on external Babble libraries (Babble-Zone, Babble-Boss, Babble-Spell, etc.) which caused errors and compatibility issues in Turtle WoW.

**Solution**: Completely replaced the Babble library system with a custom modular localization framework.

#### Implementation Details:

**Created `Locales/LocalizationFramework.lua`**:
- Core localization system with namespace support
- Automatic fallback to English for missing translations
- Efficient lookup system for zones, bosses, spells, items, etc.

**Modular Structure**:
```
Locales/
├── LocalizationFramework.lua (Core system)
├── locales.xml (Load order)
└── [locale]/
    ├── Core.lua (UI strings)
    ├── Zones.lua (Zone names)
    ├── Bosses.lua (Boss names)
    ├── Classes.lua (Class names)
    ├── Factions.lua (Faction names)
    ├── Spells.lua (Spell names)
    ├── ItemSets.lua (Item set names)
    ├── MapData.lua (Map-specific data)
    └── QuestData.lua (Quest information)
```

**Supported Languages**:
- English (enUS) - Complete
- Spanish (esES) - Complete
- German (deDE) - Complete
- Portuguese (ptBR) - Complete
- Chinese (zhCN) - Complete

### 2. Spanish (esES) Localization Fixes

**Files Fixed**:
- `Locales/esES/Core.lua` - All UI strings translated
- `Locales/esES/Zones.lua` - All zone names translated
- `Locales/esES/Bosses.lua` - All boss names translated
- `Locales/esES/Classes.lua` - All class names translated
- `Locales/esES/Factions.lua` - All faction names translated
- `Locales/esES/Spells.lua` - All spell names translated
- `Locales/esES/ItemSets.lua` - All item set names translated
- `Locales/esES/MapData.lua` - Map-specific translations
- `Locales/esES/QuestData.lua` - Quest translations

**Result**: No more localization errors when using Spanish language in Turtle WoW.

### 3. Turtle WoW Custom Content Support

**Custom Zones Supported**:
- The Black Morass (Morass Oscuro)
- Emerald Sanctum (Santuario Esmeralda)
- Tower of Karazhan (Torre de Karazhan)
- All other Turtle WoW custom instances

**Custom Bosses Supported**:
- All custom raid bosses from Turtle WoW content
- Proper localization for custom encounters

### 4. pfQuest Integration Enhancements

**Improved Features**:
- Right-click on items in loot panel to search in pfQuest database
- Right-click on quests to show starter location on map
- Right-click on quest rewards to search in pfQuest database
- Seamless integration with pfQuest addon

### 5. Code Optimization

**Performance Improvements**:
- Removed dependency on external Babble libraries (reduced memory footprint)
- Optimized localization lookup system
- Faster addon loading time
- Reduced CPU usage during runtime

---

## Technical Details

### Localization Framework API

The new localization system provides the following functions:

```lua
-- Get localized string
AtlasTW_GetLocale(namespace, key)

-- Register translations for a namespace
AtlasTW_RegisterLocale(namespace, locale, translations)

-- Check if translation exists
AtlasTW_HasTranslation(namespace, key)
```

### Namespace Structure

- `"Core"` - UI strings and interface text
- `"Zones"` - Zone and instance names
- `"Bosses"` - Boss and NPC names
- `"Classes"` - Player class names
- `"Factions"` - Faction names
- `"Spells"` - Spell and ability names
- `"ItemSets"` - Item set names
- `"MapData"` - Map-specific localized data
- `"QuestData"` - Quest names and descriptions

### Fallback System

If a translation is not found in the current locale, the system automatically falls back to English (enUS). This ensures that the addon always displays readable text, even if some translations are missing.

---

## Testing Procedure

### Test Environment
- **Server**: Turtle WoW
- **Client**: WoW 1.12.1
- **Language**: Spanish (esES)
- **Character**: Elnazzareno (El Sequito del Terror)

### Tests Performed
1. ✓ Loaded addon without errors
2. ✓ Verified all UI elements display correctly in Spanish
3. ✓ Tested all instance maps (Vanilla + Turtle WoW custom)
4. ✓ Verified loot panel functionality
5. ✓ Tested quest panel with Alliance and Horde quests
6. ✓ Verified pfQuest integration
7. ✓ Tested all dropdown menus and options
8. ✓ Verified tooltip integration
9. ✓ Tested minimap button functionality
10. ✓ Verified saved variables persistence

### Results
- **No errors** during addon loading
- **No errors** during runtime
- **All features** working as expected
- **All localizations** displaying correctly

---

## Files Modified/Created

### New Files Created (Localization System)
- `Locales/LocalizationFramework.lua`
- `Locales/locales.xml`
- `Locales/enUS/*.lua` (9 files)
- `Locales/esES/*.lua` (9 files)
- `Locales/deDE/*.lua` (9 files)
- `Locales/ptBR/*.lua` (9 files)
- `Locales/zhCN/*.lua` (9 files)

### Modified Files
- All core addon files to use new localization system
- `Atlas-TW.toc` - Updated with credits
- `README.md` - Added Turtle WoW compatibility section

### Documentation Files
- `CHANGELOG_TURTLEWOW.md` (this file)
- `CREDITOS_ES.md` - Spanish version of this changelog
- `LEEME.md` - Spanish README

---

## Future Maintenance

### Adding New Translations

To add or update translations:

1. Navigate to `Locales/[locale]/`
2. Edit the appropriate module file (e.g., `Zones.lua` for zone names)
3. Add your translation following the existing format
4. Reload the addon with `/reload`

### Adding New Custom Content

When Turtle WoW adds new custom content:

1. Add zone names to `Locales/*/Zones.lua`
2. Add boss names to `Locales/*/Bosses.lua`
3. Add map data to `Locales/*/MapData.lua`
4. Add quest data to `Locales/*/QuestData.lua`
5. Test with `/reload`

---

## Known Issues

None at this time. All known issues have been resolved.

---

## Credits

### Original Atlas Development Team
- CFM
- Otari98
- Dan Gilbert
- Daviesh
- pepopo
- And many other contributors

### Turtle WoW Compatibility Fixes
- **DarckRovert** (Elnazzareno - El Sequito del Terror)
  - Localization system overhaul
  - Spanish translation fixes
  - Turtle WoW custom content support
  - pfQuest integration enhancements
  - Documentation

---

## Special Thanks

- The Turtle WoW development team for creating amazing custom content
- The Atlas development team for the original addon
- El Sequito del Terror guild for support and testing
- The Turtle WoW community for feedback

---

## License

This addon maintains the original Atlas license. The Turtle WoW compatibility fixes are open source and can be used freely.

---

**Enjoy your dungeon runs without errors!** 🐢✨
