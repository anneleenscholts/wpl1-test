# Mini-website voorbeeldproject (PXL)

Dit is een lesvoorbeeld van een kleine, semantisch correct opgebouwde
website, inclusief een GitHub Actions pipeline die automatisch controleert
op een aantal basisvereisten en de site publiceert naar GitHub Pages.

## Gebruikte technologieën

- **HTML5** — semantische structuur (`header`, `nav`, `main`, `section`, `article`, `aside`, `figure`, `footer`).
- **CSS3** — eigen stylesheet (`public/css/style.css`) met custom properties voor kleuren en lettertypes, Flexbox en CSS Grid voor de lay-out (hero, kaartengrid, zigzag beeld/tekstblokken).
- **Vanilla JavaScript** (`public/js/script.js`) — kopieert een hexcode naar het klembord via de Clipboard API, geladen met `defer` in de `<head>`.
- **Google Fonts** — in de `<head>` van beide pagina's toegevoegd via `<link>`: Archivo Black (hero-titel), Lora (koppen) en IBM Plex Mono (labels/eyebrows).

## Credits

- Placeholderfoto's via [placehold.co](https://placehold.co).
- Lettertypes via [Google Fonts](https://fonts.google.com) (Archivo Black, Lora, IBM Plex Mono).

### AI-gebruik

Voor dit project heb ik Claude Code (AI-assistent) gebruikt bij het **herstijlen** van de site:
de hero-sectie, de kaartenlay-out, de zigzag beeld/tekstblokken en het kleur- en
typografiesysteem van de werkbezoekpagina zijn met AI opgezet op basis van een aangeleverd
ontwerpvoorbeeld, en diezelfde stijl is doorgetrokken naar de portfoliopagina. De tekts heb ik allemaal laten proeflezen door AI om te zorgen dat ik een professionele en consistente toon uitstraal.

Zelf heb ik de inhoud van het werkbezoekverslag geschreven, de projecten en het kleurenpalet in
de portfolio samengesteld, en telkens gecontroleerd of het resultaat klopte en aangepast waar nodig.

## Privacy

Dit is een fictief lesvoorbeeld: de vermelde namen, e-mailadressen en bedrijfsgegevens bestaan
niet echt. De pagina's laden geen trackers of analytics; de enige interactie (kleur kopiëren op
de portfoliopagina) gebeurt volledig lokaal in de browser via de Clipboard API, zonder dat er
gegevens worden verzonden of opgeslagen.