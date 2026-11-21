[English](README.en.md) · [简体中文](README.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · Deutsch · [Español](README.es.md)

<p align="center">
  <img src="assets/pika-ui-logo.png" width="300" alt="Farbiges Pickup-Logo von Pika UI">
</p>

<h1 align="center">Pika UI</h1>

<p align="center"><strong>Mit der echten Aufgabe beginnen, die Oberfläche klar gestalten und passend zum Projekt umsetzen.</strong></p>

Pika UI ist ein plattformübergreifender Skill für Interface-Design und Implementierung mit KI-Coding-Agenten. Er begleitet den gesamten Weg von neuen Oberflächen und Redesigns bis zur Screenshot-Reproduktion und UI-Prüfung – für Web, Desktop, Mobilgeräte und weitere Softwareoberflächen.

React Bits ist eine optionale Quelle für visuelle und interaktive Ideen, keine Vorgabe für den Tech-Stack. React-Projekte können passende Komponenten prüfen; andere Stacks setzen den Effekt für ihre Zielplattform um.

## Schnellstart

Klone das Repository in dein Codex-Skills-Verzeichnis:

```bash
git clone https://github.com/lbxx-13/pika-ui.git ~/.codex/skills/pika-ui
```

Bei einem eigenen `CODEX_HOME` gehört das Repository nach `$CODEX_HOME/skills/pika-ui`. Für ein privates Repository muss GitHub auf deinem Rechner erreichbar sein. Verwende nach der Installation in einem neuen Codex-Turn `$pika-ui` oder beschreibe die Aufgabe direkt.

Eine vorhandene Installation aktualisieren:

```bash
git -C ~/.codex/skills/pika-ui pull --ff-only
```

## Was du damit tun kannst

- **Neue Oberflächen gestalten:** Richtung festlegen und Produktseiten, Workspaces, mobile Ansichten oder Komponenten umsetzen.
- **Bestehende UI verbessern:** Seiten, Design-Tokens, gemeinsame Komponenten und Verhalten des Projekts verstehen, bevor Änderungen beginnen.
- **Referenzen nachbauen:** Layout, Proportionen, Schrift, Farbe und Hierarchie umsetzen und im Ziel-Viewport prüfen.
- **Designrichtungen vergleichen:** Auf Wunsch bis zu drei tatsächlich unterschiedliche Entwürfe erstellen und lokal nebeneinander ansehen.
- **Erlebnisse prüfen:** Hierarchie, responsive Layouts, Zustände, Tastaturzugang und Verhalten bei reduzierter Bewegung kontrollieren.
- **Bewegung und Medien erkunden:** React Bits optional als Komponentenreferenz verwenden oder geeignete Bilder, Icons und Animationen auswählen.

## Beispielprompts

```text
$pika-ui Erstelle eine Landingpage für dieses Kursbuchungsprodukt, die ich in einer Vorschau ansehen kann. Leite die Richtung aus Zielgruppe und Kursinhalten ab und setze Desktop- und Mobil-Layouts um.
```

```text
Rekonstruiere diesen Screenshot mit Pika UI. Prüfe zuerst Framework und Styling-Konventionen des Projekts und kontrolliere nach der Umsetzung auch ein schmales Layout.
```

```text
Prüfe diese Seite mit Pika UI. Melde nur Probleme, die durch Screenshot oder Code belegt sind, nenne konkrete Korrekturen und ändere keine Dateien.
```

## Arbeitsablauf

1. **Kontext verstehen:** Zielgruppe, Hauptaufgabe, Gerät, vorhandene Oberfläche und Tech-Stack bestimmen.
2. **Designentscheidungen treffen:** Fokus, primäre Aktion, visuelle Richtung, Typografie und Farbe, Bildwelt und wichtige Zustände festlegen.
3. **Im Projekt umsetzen:** Vorhandene Komponenten, Design-Tokens, Abhängigkeiten und Plattformkonventionen weiterverwenden.
4. **Die echte Oberfläche prüfen:** Ziel-Viewport, wichtige Zustände und primäre Aktionen kontrollieren; anschließend verfeinern und Überflüssiges entfernen.

Lies Referenzen nur dann, wenn die Aufgabe sie braucht. Kleine, klar umrissene Änderungen müssen nicht den gesamten Prozess zur Richtungsfindung durchlaufen.

## Leitfadenübersicht

| Aufgabe | Leitfaden |
| --- | --- |
| Neue UI, Redesign und Umsetzung | [`references/design-workflow.md`](references/design-workflow.md) |
| Visuelle Richtung und Konzeptfindung | [`references/design-direction.md`](references/design-direction.md), [`references/task-explore.md`](references/task-explore.md) |
| Marketing-, Marken- und Launch-Seiten | [`references/direction-persuasion.md`](references/direction-persuasion.md) |
| Screenshot-Reproduktion, Layout und Viewport | [`references/layout-and-viewport.md`](references/layout-and-viewport.md) |
| Typografie, Farbe, Oberflächen und Hierarchie | [`references/visual-language.md`](references/visual-language.md) |
| Design-Tokens und Systempflege | [`references/design-system.md`](references/design-system.md) |
| Formulare, Dialoge und komplexe Zustände | [`references/interaction-states.md`](references/interaction-states.md) |
| Bewegung und reduzierte Bewegung | [`references/motion.md`](references/motion.md) |
| Bilder, Icons und Medienquellen | [`references/media.md`](references/media.md) |
| UX-Abläufe durchgehen | [`references/ux-review.md`](references/ux-review.md) |
| UI-Review ohne Änderungen | [`references/task-review.md`](references/task-review.md), [`references/review-checklist.md`](references/review-checklist.md) |
| Entwürfe vergleichen | [`references/style-explorer.md`](references/style-explorer.md) |
| Browser und Entwicklungstools | [`references/tools.md`](references/tools.md) |

### Die Rolle von React Bits

[React Bits](https://reactbits.dev/) bietet Textanimationen, Hintergründe, Komponenten und Micro-Interactions. Pika UI behandelt die Seite als optionale Inspirationsquelle für Visuals und Interaktionen. Lies vor der Nutzung oder Anpassung [`references/react-bits.md`](references/react-bits.md). React-Komponenten aus dem Quellcode werden nur direkt integriert, wenn das Zielprojekt React nutzt und die Integration passt. Andere Plattformen setzen Absicht und Effekt mit ihren eigenen Mitteln um.

## Repository-Struktur

```text
SKILL.md                          Skill-Einstieg und Aufgaben-Routing
references/                       Leitfäden für Design, Umsetzung und Review
assets/style-explorer.html        Lokale Seite zum Vergleichen von Entwürfen
assets/pika-ui-logo.png           Pika-UI-Pickup-Logo
scripts/create_style_explorer.py  Skript zum Erzeugen von Vergleichslinks
```

Die Vergleichsseite zeigt bereits vorhandene Entwürfe nebeneinander. Sie ersetzt keine Richtungsfindung und erzeugt selbst keine Konzepte.

## Gestaltungsgrundsätze

- Folge Marke, Tech-Stack, Komponenten und Plattformkonventionen des Projekts, statt einen festen Stil aufzuzwingen.
- Nutze Produktfakten aus dem Projekt oder verifizierte Angaben; erfinde keine Kennzahlen, Kundenstimmen oder Funktionsversprechen.
- React Bits ist weder eine plattformübergreifende Komponentenbibliothek noch die einzige Komponentenquelle. Passe Ideen an den Ziel-Stack an.
- Prüfe Visuals, Interaktionen und Funktion getrennt. Kennzeichne nicht geprüfte Bereiche, wenn die Oberfläche nicht ausgeführt wurde.

