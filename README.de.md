[English](README.md) · [简体中文](README.zh-CN.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · Deutsch · [Español](README.es.md)

<p align="center">
  <img src="assets/pika-ui-logo.png" width="300" alt="Farbiges Pickup-Logo von Pika UI">
</p>

<h1 align="center">Pika UI</h1>

<p align="center"><strong>Mit der echten Aufgabe beginnen, die Oberfläche klar gestalten und passend zum Projekt umsetzen.</strong></p>

Pika UI ist ein plattformübergreifender Skill für Interface-Design und Implementierung mit KI-Coding-Agenten. Er begleitet den gesamten Weg von neuen Oberflächen und Redesigns bis zur Screenshot-Reproduktion und UI-Prüfung – für Web, Desktop, Mobilgeräte und weitere Softwareoberflächen.

React Bits ist eine optionale Quelle für visuelle und interaktive Ideen, keine Vorgabe für den Tech-Stack. React-Projekte können passende Komponenten prüfen; andere Stacks setzen den Effekt für ihre Zielplattform um.

## Installation

### Im Terminal installieren

Führe den folgenden Befehl in einem beliebigen Verzeichnis aus. Er installiert nur den Skill `pika-ui` für Codex und stellt ihn für alle Projekte bereit:

```bash
npx skills add lbxx-13/pika-ui --skill pika-ui -g -a codex
```

Dieses GitHub-Repository ist derzeit privat. Der Rechner, auf dem der Befehl läuft, benötigt Zugriff über Git-Zugangsdaten, eine Anmeldung mit GitHub CLI oder SSH. Falls eine Auswahl erscheint, wähle Codex und die globale Installation.

### Einen Agenten um die Installation bitten

Sende diese Nachricht an einen Agenten, der Terminalbefehle ausführen kann:

```text
Bitte installiere den Pika UI Skill für Codex. Führe dazu Folgendes aus: npx skills add lbxx-13/pika-ui --skill pika-ui -g -a codex
```

Auch der Rechner des Agenten benötigt Zugriff auf dieses private GitHub-Repository. Schlägt die Authentifizierung fehl, richte zuerst den GitHub-Zugriff ein und führe den Befehl erneut aus.

### Später aktualisieren

```bash
npx skills update pika-ui -g
```

Wenn du das Repository stattdessen manuell geklont hast, aktualisiere es so:

```bash
git -C ~/.codex/skills/pika-ui pull --ff-only
```

Bei einem eigenen `CODEX_HOME` ersetzt du `~/.codex` durch dein Codex-Hauptverzeichnis.

## Pika UI verwenden

Starte nach der Installation einen neuen Codex-Turn. Rufe den Skill mit `$pika-ui` ausdrücklich auf oder beschreibe die Aufgabe und bitte Codex, Pika UI zu verwenden. Teile relevante Projekte, Screenshots, Markenmaterialien und Vorgaben mit. Pika UI prüft den vorhandenen Tech-Stack und lädt nur die passenden Leitfäden.

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

