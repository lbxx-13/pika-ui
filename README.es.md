[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Deutsch](README.de.md) · Español

<p align="center">
  <img src="assets/pika-ui-logo.png" width="300" alt="Logotipo colorido de la camioneta Pika UI">
</p>

<h1 align="center">Pika UI</h1>

<p align="center"><strong>Empieza por la tarea real, diseña una interfaz clara e impleméntala para el proyecto.</strong></p>

Pika UI es una skill multiplataforma de diseño e implementación de interfaces para agentes de programación con IA. Acompaña todo el proceso, desde crear y rediseñar interfaces hasta recrear capturas y revisar UI, en web, escritorio, móvil y otras superficies de software.

React Bits es una fuente opcional de ideas visuales y de interacción, no un requisito tecnológico. Los proyectos React pueden evaluar sus componentes cuando convenga; los demás pueden adaptar el efecto a su plataforma.

## Instalación

### Instalar desde la terminal

Ejecuta este comando desde cualquier directorio. Instala solo la skill `pika-ui` para Codex y la deja disponible en todos tus proyectos:

```bash
npx skills add lbxx-13/pika-ui --skill pika-ui -g -a codex
```

Este repositorio de GitHub es privado por ahora. El equipo donde ejecutes el comando necesita acceso mediante credenciales de Git, una sesión autenticada de GitHub CLI o SSH. Si aparece una selección, elige Codex e instalación global.

### Pedir a un agente que la instale

Envía este mensaje a un agente que pueda ejecutar comandos de terminal:

```text
Instala la skill Pika UI para Codex. Ejecuta: npx skills add lbxx-13/pika-ui --skill pika-ui -g -a codex
```

El equipo que ejecuta el agente también necesita acceso a este repositorio privado de GitHub. Si falla la autenticación, configura primero el acceso a GitHub y vuelve a ejecutar el comando.

### Actualizar más adelante

```bash
npx skills update pika-ui -g
```

Si la instalaste clonando el repositorio manualmente, actualízala así:

```bash
git -C ~/.codex/skills/pika-ui pull --ff-only
```

Si usas un `CODEX_HOME` personalizado, sustituye `~/.codex` por tu directorio principal de Codex.

## Usar Pika UI

Después de instalarla, inicia un nuevo turno de Codex. Invoca la skill explícitamente con `$pika-ui` o describe la tarea y pide a Codex que use Pika UI. Comparte el proyecto, las capturas, los recursos de marca y las restricciones pertinentes; revisará el stack existente y cargará solo las guías necesarias.

## Qué puedes hacer

- **Diseñar una interfaz nueva:** Define una dirección visual e implementa páginas de producto, espacios de trabajo, vistas móviles o componentes.
- **Mejorar una interfaz existente:** Comprende las páginas, los tokens de diseño, los componentes compartidos y el comportamiento antes de modificar.
- **Recrear una referencia:** Reproduce layout, proporciones, tipografía, color y jerarquía; después revisa la vista objetivo.
- **Comparar direcciones:** Cuando se solicite, crea hasta tres propuestas realmente distintas y compáralas en una página local.
- **Revisar una experiencia:** Comprueba jerarquía, diseño adaptable, estados, acceso por teclado y comportamiento con movimiento reducido.
- **Explorar movimiento y medios:** Usa React Bits como referencia opcional o elige imágenes, iconos y animaciones adecuados.

## Ejemplos de prompts

```text
$pika-ui Diseña una landing page que pueda previsualizar para este producto de reservas de cursos. Define la dirección según el público y el contenido del curso, y crea layouts para escritorio y móvil.
```

```text
Recrea esta captura con Pika UI. Primero revisa el framework y las convenciones de estilos del proyecto; después implementa la página y comprueba un ancho reducido.
```

```text
Revisa esta página con Pika UI. Informa solo de problemas respaldados por capturas o código, propone correcciones concretas y no modifiques archivos.
```

## Flujo de trabajo

1. **Entender el contexto:** Identifica público, tarea principal, dispositivo, interfaz existente y stack del proyecto.
2. **Tomar decisiones de diseño:** Define el foco, la acción principal, la dirección visual, tipografía y color, imágenes clave y estados importantes.
3. **Implementar para el proyecto:** Sigue los componentes, tokens, dependencias y convenciones de plataforma existentes.
4. **Revisar la interfaz real:** Comprueba viewport, estados importantes y acciones principales; refina el resultado y elimina lo innecesario.

Carga referencias solo cuando la tarea las necesite. Los cambios pequeños y concretos pueden hacerse directamente sin recorrer todo el proceso de dirección.

## Mapa de guías

| Tarea | Guía |
| --- | --- |
| Nueva interfaz, rediseño e implementación | [`references/design-workflow.md`](references/design-workflow.md) |
| Dirección visual y exploración de conceptos | [`references/design-direction.md`](references/design-direction.md), [`references/task-explore.md`](references/task-explore.md) |
| Páginas de marketing, marca y lanzamiento | [`references/direction-persuasion.md`](references/direction-persuasion.md) |
| Recreación de capturas, layout y viewport | [`references/layout-and-viewport.md`](references/layout-and-viewport.md) |
| Tipografía, color, superficies y jerarquía | [`references/visual-language.md`](references/visual-language.md) |
| Tokens y mantenimiento del sistema | [`references/design-system.md`](references/design-system.md) |
| Formularios, diálogos y estados complejos | [`references/interaction-states.md`](references/interaction-states.md) |
| Movimiento y preferencias de movimiento reducido | [`references/motion.md`](references/motion.md) |
| Imágenes, iconos y fuentes de medios | [`references/media.md`](references/media.md) |
| Recorrido de flujos UX | [`references/ux-review.md`](references/ux-review.md) |
| Revisión UI de solo lectura | [`references/task-review.md`](references/task-review.md), [`references/review-checklist.md`](references/review-checklist.md) |
| Comparación de propuestas | [`references/style-explorer.md`](references/style-explorer.md) |
| Navegadores y herramientas de desarrollo | [`references/tools.md`](references/tools.md) |

### El papel de React Bits

[React Bits](https://reactbits.dev/) ofrece animaciones de texto, fondos, componentes y microinteracciones. Pika UI lo trata como una fuente opcional de ideas visuales y de interacción. Antes de usar o adaptar un ejemplo, consulta [`references/react-bits.md`](references/react-bits.md). Integra directamente sus componentes React solo si el proyecto usa React y la solución encaja; para otras plataformas, implementa la intención y el efecto con las herramientas del stack correspondiente.

## Estructura del repositorio

```text
SKILL.md                          Entrada de la skill y enrutamiento de tareas
references/                       Guías de diseño, implementación y revisión
assets/style-explorer.html        Página local para comparar propuestas
assets/pika-ui-logo.png           Logotipo de la camioneta Pika UI
scripts/create_style_explorer.py  Script para generar enlaces de comparación
```

La página de comparación sirve para revisar propuestas ya creadas. No reemplaza la exploración de dirección ni genera conceptos por sí sola.

## Límites de diseño

- Sigue la marca, el stack, los componentes y las convenciones de plataforma del proyecto; no impongas un estilo fijo.
- Usa hechos proporcionados por el proyecto o verificados; no inventes métricas, testimonios ni promesas de funciones.
- React Bits no es una biblioteca multiplataforma ni la única fuente de componentes. Adapta las ideas al stack de destino.
- Revisa por separado lo visual, la interacción y la funcionalidad. Indica qué no se ha verificado cuando la interfaz no se ha ejecutado.

