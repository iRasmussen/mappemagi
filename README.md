# mappemagi

Et lille Python-projekt, der viser, hvordan datoer og mapper kan bruges i et
terminalprogram.

**Version: 1008a** (se også `VERSION` og `CHANGELOG.md`).

## Formål og læringsmål

Med `datemagic.py` kan du øve dig i at:

- hente brugerinput fra terminalen og validere det,
- arbejde med datoer og kalendermåneder i Pythons standardbibliotek,
- bygge filstier og oprette mapper,
- gennemgå et programs flow fra forhåndsvisning til bekræftelse og resultat.

Programmet opretter én mappe for hver dag i den aktuelle lokale måned. Mappenavne
følger ISO 8601-formatet `YYYY-MM-DD`, for eksempel `2026-10-01`. Programmet
bruger kun Pythons standardbibliotek; ekstra pakker skal ikke installeres.

## Krav

- Python 3.10 eller nyere.
- En terminal (for eksempel Terminal på macOS/Linux eller PowerShell på Windows).

Tjek din Python-version med:

```console
python3 --version
```

## Sådan kører du programmet

1. Åbn en terminal, og gå til projektmappen, hvor `datemagic.py` ligger.
2. Start programmet:

   ```console
   python3 datemagic.py
   ```

3. Angiv en eksisterende målmappe, eller tryk Enter for at bruge den aktuelle
   mappe. En sti, der begynder med `~`, udvides til din hjemmemappe.
4. Vælg datoformat `1` (`YYYY-MM-DD`). Det er det eneste understøttede format.
5. Gennemgå måneden, målstedet og listen over planlagte mapper.
6. Svar `ja` for at oprette mapperne eller tryk Enter/svar `nej` for at afslutte
   uden ændringer.

## Eksempel

Eksemplet viser en kørsel i oktober 2026. Den viste målmappe er et eksempel; den
faktiske sti afhænger af din computer. Listen forkortes her for læsbarhed.

```text
Målmappe [/projektmappe]: /home/studerende/Dokumenter/Projekt

Datoformat:
1) YYYY-MM-DD (ISO 8601)
Vælg format [1]: 1

Aktuel måned: oktober 2026
Målmappe: /home/studerende/Dokumenter/Projekt
Planlagte mapper:
  2026-10-01
  2026-10-02
  ...
  2026-10-31

Opret disse mapper? [j/nej]: ja

Oprettet: 31
Sprunget over: 0
```

Når kørslen er færdig, vises hvor mange mapper der blev oprettet, og hvor mange
der allerede fandtes og derfor blev sprunget over. Programmet afslutter derefter,
og terminalens kommandoprompt vises igen. Det er sikkert at køre programmet
flere gange: eksisterende mapper overskrives ikke. Hvis du afviser bekræftelsen,
oprettes der ingen mapper.

Antallet afhænger af måneden. Programmet håndterer også skudår korrekt, så
februar kan have 29 mapper.
