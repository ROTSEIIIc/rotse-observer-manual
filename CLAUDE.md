# rotse-observer-manual: notes for Claude

The observer manual for **ROTSE-IIIc**, the robotic telescope at the H.E.S.S. site, Namibia.
Static website built with Material for MkDocs. Readers are **observers at night**, often new
to the telescope. The site always has internet. Editors are the ROTSE team; most know
Markdown, not MkDocs.

`README.md` is the human guide to editing. Keep it true when you change how things work.

## Commands

```bash
uv sync                          # install (first time)
uv run mkdocs serve              # live preview on http://127.0.0.1:8000
uv run mkdocs build --strict     # MUST pass before you say a change is done
grep -rn TODO docs/              # what is still unwritten
uv run python scripts/make_pdf.py  # PDF of the whole manual -> dist/ (needs Chrome)
```

The build prints a Material end-of-life notice and an "MkDocs 2.0" warning. Both are expected,
not errors. (`NO_MKDOCS_2_WARNING=1` silences the second.)

## Layout

| Path | What |
|---|---|
| `mkdocs.yml` | Settings, theme, extensions, and `nav:` (the menu) |
| `docs/*.md` | Observer pages, one file per page |
| `docs/editors/features.md` | Feature showcase: every enabled feature, rendered + its Markdown. Copy syntax from here. |
| `docs/about.md` | Maintainers, how to report mistakes, version history |
| `docs/assets/` | Images. `rotse.png` = logo, white on transparent |
| `docs/stylesheets/extra.css` | All colours (`--rotse-navy`, `--rotse-accent` amber) |
| `includes/abbreviations.md` | Glossary, auto-appended to every page → hover tooltips |
| `includes/*.md` | Shared text, pulled in with `--8<-- "file.md"` |
| `templates/page.md`, `templates/snippets.md` | Starting points for new pages; not built |
| `pdf/cover_page.tpl`, `hooks/build_info.py` | PDF cover; version/date from git |
| `docs/javascripts/print.js` + print part of `extra.css` | Print/PDF: light colours, open boxes, all tabs, page numbers |

## Rules for content (most important first)

1. **Never invent a procedure, limit, value, name, phone number or GUI label.** This manual
   tells people when to open a roof over a telescope. If a fact isn't given to you by the
   editor or found in a source they point you to, write a `!!! todo "TODO"` box that says
   what is missing. A wrong instruction is worse than a missing one. When you replace a TODO
   with something you were told, say in your reply where it came from.
2. **Safety:** anything that can damage the telescope or hurt someone goes in a
   `!!! danger` box, at the top of the step where it matters. The emergency contact box on
   `index.md` must stay at the top of the home page.
3. **No secrets:** no passwords, keys, private phone numbers or internal hostnames beyond
   what is already there. Write where to get them instead.
4. **Procedures:** numbered steps, one action each, imperative ("Click **Park**"). After a
   step whose outcome matters, add *You should see:* … GUI labels in **bold** exactly as the
   GUI shows them.
5. Short sentences, plain English (many readers aren't native speakers). Number and unit with a
   space (`85 %`, `30 s`), except degrees (`20°`). Dates as YYYY-MM-DD. Mark temporary situations with
   `!!! warning "Temporary (since YYYY-MM-DD)"`.

## Mechanics

- **New page:** copy `templates/page.md` into `docs/`, lowercase-hyphen filename, **add it to
  `nav:` in `mkdocs.yml`** (a page missing from `nav:` only gets an INFO line, the strict
  build won't catch it).
- **Links are relative to the file:** `[Shutdown](shutdown.md)` from `docs/`,
  `../shutdown.md` from `docs/editors/`. Section links use the heading slug:
  `weather-and-safety.md#weather-limits`. Renaming a heading breaks its anchor links.
- **New abbreviation:** one line `*[ABBR]: Explanation` in `includes/abbreviations.md`, not
  per page.
- **Text used on several pages:** put it in `includes/` and include it; don't copy-paste.
- **Images:** `docs/assets/`, descriptive name, cropped, under ~500 KB, always alt text.
- **Colours** only in `extra.css`. Check any visual change in **both** dark (default) and
  light mode: the logo is white, the header stays navy in both.
- The **"last updated" date** on each page comes from git (`git-revision-date-localized`),
  so it only changes after a commit. CI checkouts need full history (`fetch-depth: 0`).
- **PDF / print:** `print-site` must stay the **last plugin**. It puts every `nav:` page except
  `editors/*` on `/print_page/`. After layout changes, run `scripts/make_pdf.py` and look at
  the PDF: tabs must print all their content, collapsible boxes must print open.
- Front matter keys in use: `title`, `description`, `icon`, `tags`, `hide`. Examples at the
  end of the feature showcase.

## Git

- **Never commit, push, tag or open a PR unless the editor asks.** Leave changes uncommitted
  and say so.
- Commits the editor asks for end with the Claude co-author line, as in the first commit.
- Short branch per topic (`docs/startup-procedure`), PR so someone else reads it.
- Don't commit `site/` or `.venv/` (gitignored).

## Status and open items

- Structure is done; nearly all observer content is TODO (procedures, weather limits,
  contacts, camera details, maintainers in `about.md` and the footer `copyright:` in
  `mkdocs.yml`).
- Not pushed yet: `repo_url`/`edit_uri` and `extra.social` in `mkdocs.yml` are commented out
  until there is a remote.
- Hosting not decided: nginx on `ocs-server` or GitHub Pages.
- Material for MkDocs reaches end of life on 2027-05-05. Successor: Zensical (same authors,
  reads `mkdocs.yml`). Migrate before then; content in `docs/` should not need changes.

## Related (only on the original developer's machine)

The telescope software lives in sibling repos under `~/rotse-dev/` (`pyobs-schier`,
`pyobs-rotse-roof`, `rotse-boltwood`, `rotse-sandbox`, `rotse-namibia-ocs`), with its own
`CLAUDE.md` one level up. Use them to check software facts, but procedures for observers
must still be confirmed by a person who has run them on the real telescope.
