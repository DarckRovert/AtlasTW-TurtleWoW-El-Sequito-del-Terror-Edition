# ðŸ“ Wiki: Arquitectura 'Diamond Tier' â€” Atlas-TW [v1.8.3]

Estructura tÃ©cnica de la cartografÃ­a de mazmorras mantenida por **DarckRovert**.

## ðŸ—ï¸ JerarquÃ­a del Sistema Atlas (Navigator Hierarchy)

Atlas-TW separa la lÃ³gica de visualizaciÃ³n de la gestiÃ³n de bases de datos masivas:

1.  **Hueso del Navigator (`TWAtlas/`)**: Gestiona la selecciÃ³n de mapas, coordenadas de bosses y el renderizado de la ventana principal.
2.  **Motor de BotÃ­n (`TWLoot/`)**: Es el mÃ³dulo de datos mÃ¡s denso. Contiene las tablas con IDs de objetos y porcentajes de drop de Turtle WoW.
3.  **Puente de Misiones (`TWQuest/`)**: Interfaz asÃ­ncrona que se comunica con **pfQuest** para mostrar misiones activas en la mazmorra seleccionada.
4.  **Capa de Persistencia (`AtlasTWOptions.lua`)**: Almacena las preferencias de usuario y el estado del buscador.

---

## ðŸ§­ Diagrama de Flujo: Carga de Datos v9.4

```mermaid
graph TD
    A[Evento: Apertura de Atlas] --> B[Carga de TWAtlas_Init]
    B --> C[SelecciÃ³n de Mazmorra]
    C --> D{Â¿Zona Custom?}
    D -- SÃ­ --> E[InyecciÃ³n de Mapas SÃ©quito]
    D -- No --> F[Carga de Mapa Blizzard/Atlas]
    E --> G[Consulta de TWLoot Database]
    F --> G
    G --> H[PeticiÃ³n a pfQuest Linker]
    H --> I[Vincular Misiones de Instancia]
    I --> J[Render Final Diamond Tier HUD]
```

## âš¡ Estrategias de IngenierÃ­a Diamond Tier

- **Selective Database Loading**: Solo se cargan en memoria los datos de la mazmorra actualmente seleccionada, liberando recursos del cliente 1.12.1.
- **Apex Skin Hook**: El AddOn detecta si pfUI estÃ¡ presente para aplicar capas de diseÃ±o coherentes con el resto del ecosistema del SÃ©quito.
- **Turtle WoW ID Sync**: Las tablas de botÃ­n se sincronizan periÃ³dicamente con los parches del servidor para garantizar precisiÃ³n absoluta.

---
Â© 2026 **DarckRovert** â€” El SÃ©quito del Terror.
*CartografÃ­a de Ã©lite para la conquista de Azeroth.*

