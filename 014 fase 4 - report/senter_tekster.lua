-- Pandoc Lua-filter for LaTeX-eksport av prosjektrapporten.
-- 1) Midtstiller frittstående bilder.
-- 2) Midtstiller og forminsker kursive figur-/tabelltekster
--    (avsnitt som i sin helhet er kursive og starter med
--     "Figur", "Tabell" eller "Vedlegg").
-- Brukes sammen med pandoc-utvidelsen -implicit_figures, slik at bilder
-- blir innlinje (ingen flytende figur, ingen dobbel auto-bildetekst).

function Para(el)
  -- Frittstående bilde: pakk inn i center-miljø.
  if #el.content == 1 and el.content[1].t == 'Image' then
    return {
      pandoc.RawBlock('latex', '\\begin{center}'),
      el,
      pandoc.RawBlock('latex', '\\end{center}'),
    }
  end

  -- Kursiv figur-/tabelltekst: midtstill og sett mindre skrift.
  if #el.content == 1 and el.content[1].t == 'Emph' then
    local txt = pandoc.utils.stringify(el)
    if txt:match('^Figur') or txt:match('^Tabell') or txt:match('^Vedlegg') then
      return {
        pandoc.RawBlock('latex', '{\\centering\\small'),
        el,
        pandoc.RawBlock('latex', '\\par}'),
      }
    end
  end
end
