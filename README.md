[DIMEV]: https://www.dimev.net/
[Zotero library]: https://www.zotero.org/irc7/tags/Walton_consolation/library

This repository supplies basic tools for study of John Walton's versified English translation of Boethius's *Consolatio philosophiae*, dated 1410.
For a bibliography of writings about this poem, see my [Zotero library].

# Line number concordance
`line-number-concordance.csv` concords the line and stanza numerations employed in the modern editions and studies of Walton's poem.
For each stanza, I supply the following:

1. The continuous line number of the stanza-opening line
1. Continuous stanza number in the EETS edition by Mark Science
1. Science's alternative numbering, by book, section, and stanza
1. The numbering, by book and line, employed by Nicholas Myklebust
1. The continuous stanza number in the partial edition by Karl Schümmer

Bibliographical details for these sources may be found in my Zotero library, linked above.

The Python script `converter.py` runs simple interactive queries on the `csv` file.
Usage:

```
$ python3 converter.py
```

Then follow the prompts.
Requires Python 3.6 or above.

# Shelfmarks and sigla
`shelfmarks-and-sigla.csv` records shelfmarks of the known manuscript copies of Walton's poem and the sigla assigned to each in editions.
The 1525 print is treated as a manuscript and identified by Short Title Catalogue number.
The file also records the following:

- The witness number assigned to each manuscript in the *New Index of Middle English Verse*, under item 1597 (= *[DIMEV]* 2677).
- My preferred sigla for the manuscripts and print. These retain past sigla where possible.
- Links to on-line images of the manuscripts, where available.

Extracts are not recorded.
For those, see the *New Index of Middle English Verse* (items 1597 and 2080) or the *[DIMEV]* \(items 2078 and 4490).
