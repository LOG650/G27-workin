#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Bygg LaTeX-versjon av prosjektrapporten fra Markdown-kilden.

Markdown-fila er strukturert for GitHub (tittel som overskrift, manuell
innholdsfortegnelse med lenker). Dette skriptet forbehandler en MIDLERTIDIG
kopi slik at LaTeX-versjonen får:
  - en ordentlig sentrert tittelside (\\begin{titlepage}) i stedet for en
    venstrestilt overskrift, og
  - LaTeX sin ekte \\tableofcontents (med sidetall) i stedet for lenkelista.

Selve kilde-Markdown endres ALDRI, så GitHub-visningen er uberørt.
Kjør:  python lag_latex.py
Krever: pandoc i PATH og preamble.tex i samme mappe.
"""
import subprocess
import sys
from pathlib import Path

HER = Path(__file__).resolve().parent
KILDE = HER / 'Prosjektrapport_LOG650_G27.md'
TMP = HER / '_build_tmp.md'
UT = HER / 'Prosjektrapport_LOG650_G27.tex'
PREAMBLE = HER / 'preamble.tex'

# Raw LaTeX-tittelside som erstatter de seks første linjene i kilden.
TITTELSIDE = r"""\begin{titlepage}
\centering
\vspace*{3cm}
{\LARGE\bfseries Prosjektrapport: Prognosepresisjon ved REMA 1000 Distribusjon Trondheim (LOG650)\par}
\vspace{2.5cm}
{\large Line Lyngsnes Johansen \\ Amanda Arnesen Almaas\par}
\vspace{1cm}
{\large Logistikk (Nettbasert), Høgskolen i Molde\par}
\vspace{0.5cm}
{\large Trondheim, 31. mai 2026\par}
\vfill
\end{titlepage}"""


def forbehandle(linjer):
    """Bytt ut tittelblokk og manuell innholdsfortegnelse med raw LaTeX."""
    # 1) Tittelblokk: fra første linje til og med første \newpage.
    if not linjer[0].startswith('# Prosjektrapport'):
        sys.exit('FEIL: forventet tittel-overskrift på linje 1.')
    try:
        np_idx = next(i for i, l in enumerate(linjer) if l.strip() == r'\newpage')
    except StopIteration:
        sys.exit('FEIL: fant ikke \\newpage etter tittelblokken.')
    linjer = [TITTELSIDE, ''] + linjer[np_idx + 1:]

    # 2) Innholdsfortegnelse: fra «# Innhold» til og med skillelinjen «---».
    try:
        toc_start = next(i for i, l in enumerate(linjer) if l.strip() == '# Innhold')
        toc_end = next(i for i, l in enumerate(linjer)
                       if i > toc_start and l.strip() == '---')
    except StopIteration:
        sys.exit('FEIL: fant ikke «# Innhold ... ---»-blokken.')
    linjer = (linjer[:toc_start]
              + [r'\newpage', r'\tableofcontents', r'\newpage']
              + linjer[toc_end + 1:])
    return linjer


def main():
    tekst = KILDE.read_text(encoding='utf-8')
    linjer = forbehandle(tekst.split('\n'))
    TMP.write_text('\n'.join(linjer), encoding='utf-8', newline='\n')

    kommando = [
        'pandoc', str(TMP), '-o', str(UT),
        '--standalone',
        # -implicit_figures: bilder blir innlinje (ingen flytende figur og
        # ingen dobbel auto-bildetekst); midtstilling gjøres av lua-filteret.
        '--from=markdown+task_lists+tex_math_dollars+pipe_tables+raw_tex-implicit_figures',
        '--to=latex',
        '--lua-filter=' + str(HER / 'senter_tekster.lua'),
        '-V', 'documentclass=article', '-V', 'fontsize=11pt', '-V', 'papersize=a4',
        '-V', 'geometry:margin=2.5cm', '-V', 'lang=nb',
        '-V', 'colorlinks=true', '-V', 'linkcolor=black',
        '-V', 'urlcolor=blue', '-V', 'citecolor=black',
        '-H', str(PREAMBLE),
    ]
    res = subprocess.run(kommando)
    TMP.unlink(missing_ok=True)
    if res.returncode == 0:
        print(f'OK: skrev {UT.name}')
    else:
        sys.exit(f'pandoc feilet (kode {res.returncode})')


if __name__ == '__main__':
    main()
