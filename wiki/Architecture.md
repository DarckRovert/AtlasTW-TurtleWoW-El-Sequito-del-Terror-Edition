# Arquitectura — Atlas-TW Sequito 🏗️

mermaid
graph TD
    CORE[Atlas Core]
    MAP_DB[Atlas-TW Maps]
    LOOT_DB[TWLoot Database]
    QUEST[TWQuest Integration]
    UI[Map Browser]

    MAP_DB --> CORE
    LOOT_DB --> CORE
    QUEST --> CORE
    CORE --> UI


## Componentes
- **TWAtlas/**: Contiene los archivos de datos de los mapas de Turtle WoW.
- **TWLoot/**: Módulo de base de datos de objetos y sus tablas de botín.
- **TWQuest/**: Integración de misiones y localizaciones de NPCs.
