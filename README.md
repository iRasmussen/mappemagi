# mappemagi

Et lille Python-eksempel, der demonstrerer mappestruktur, datoer og scripting
via terminalen.

## `datemagic.py`

`datemagic.py` opretter en mappe for hver dag i den aktuelle lokale måned.
Mappenavnene bruger det godkendte ISO-format `YYYY-MM-DD`, for eksempel
`2026-09-01` og `2026-09-30`. Scriptet bruger kun Pythons standardbibliotek.

Kør scriptet fra projektmappen:

```console
python3 datemagic.py
```

Scriptet:

1. spørger efter en eksisterende målmappe (den aktuelle mappe er standardvalget),
2. lader dig vælge `YYYY-MM-DD`,
3. viser måneden og alle planlagte mapper,
4. beder om bekræftelse, før der oprettes noget.

Der oprettes det korrekte antal dage for måneden, også 29 dage i februar i
skudår. Eksisterende mapper springes over uden fejl, og til sidst vises antal
oprettede og sprangne mapper. Svar nej ved bekræftelsen for at afslutte uden
ændringer.

Eksempel:

```text
Target directory [.]: ~/Dokumenter/Projekt
Choose a format [1]: 1
...
Create these folders? [y/N]: y

Created: 30
Skipped: 0
```
