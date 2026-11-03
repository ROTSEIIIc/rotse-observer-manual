# ROTSE-IIIc Observer Manual

The website observers use to run ROTSE-IIIc at the H.E.S.S. site, Namibia. It is built with
[Material for MkDocs](https://squidfunk.github.io/mkdocs-material/): you write Markdown files,
it turns them into a searchable static website (dark mode by default).

The manual is a **template that we fill in as we go**. Everything not yet written is in a blue
`TODO` box. Replace them one at a time as procedures get tested on the real telescope.

---

## 1. One-time setup

You need [uv](https://docs.astral.sh/uv/) (it installs Python and everything else).

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

git clone <repo-url> rotse-observer-manual   # TODO: fill in once pushed
cd rotse-observer-manual
uv sync                                      # installs MkDocs + theme into .venv
```

## 2. Preview while you edit

```bash
uv run mkdocs serve
```

Open <http://127.0.0.1:8000>. Leave it running: every time you save a file the browser
reloads. Stop it with Ctrl+C.

## 3. Where things are

```
rotse-observer-manual/
├── mkdocs.yml               ← site settings + the menu (nav:)
├── docs/                    ← THE CONTENT: one .md file = one page
│   ├── index.md             ← home page
│   ├── before-you-observe.md
│   ├── startup.md
│   ├── observing.md
│   ├── weather-and-safety.md
│   ├── shutdown.md
│   ├── troubleshooting.md
│   ├── contacts.md
│   ├── editors/features.md  ← FEATURE SHOWCASE: everything the site can do
│   ├── editors/tags.md      ← pages grouped by tag
│   ├── assets/              ← images (logo, screenshots)
│   ├── javascripts/         ← MathJax setup (math formulas)
│   └── stylesheets/extra.css← colours
├── includes/                ← reusable text, pulled into pages (not pages themselves)
│   ├── abbreviations.md     ← glossary: tooltips on every page
│   └── roof-warning.md      ← example of a shared warning box
├── templates/               ← copy-paste starting points (not part of the site)
│   ├── page.md
│   └── snippets.md
└── site/                    ← built website (generated, never edit, not in git)
```

## 4. Everyday tasks

### Fill in a TODO

Find what is left:

```bash
grep -rn TODO docs/
```

Open the file, replace the `!!! todo` box (and its indented lines) with the real text. Save,
check the preview.

### Edit an existing page

Open the `.md` file in `docs/` in any editor (VS Code is fine), change it, save.

### Add a new page

1. Copy the template: `cp templates/page.md docs/focusing.md`
   (lowercase, hyphens, no spaces).
2. Add it to the menu in `mkdocs.yml` under `nav:`, where it should appear:
   ```yaml
   nav:
     - Observing: observing.md
     - Focusing: focusing.md        # new
   ```
3. Link to it from other pages: `[Focusing](focusing.md)`.

Pages can be grouped into menu sections:

```yaml
nav:
  - Observing:
      - Basics: observing.md
      - Focusing: focusing.md
```

### Add a screenshot or photo

1. Save the image in `docs/assets/` with a clear name, e.g. `gui-telescope-tab.png`.
   Keep files small (crop; under ~500 KB).
2. Put it in the page:
   ```markdown
   ![Telescope tab of the pyobs GUI](assets/gui-telescope-tab.png)
   ```

### Rename or remove a page

Rename/delete the file **and** update `nav:` in `mkdocs.yml` **and** any links to it.
The strict build (below) tells you about broken links.

### Change colours or the logo

Colours: `docs/stylesheets/extra.css` (top of the file). Logo: replace
`docs/assets/rotse.png` (white on transparent works best on the dark header).

## 5. Writing cheat sheet

**See everything in action:** run `uv run mkdocs serve` and open *For editors → Feature
showcase*. Every feature (boxes, tabs, code annotations, cards, icons, diagrams, math,
includes, front matter, site-wide options) is shown as a result, with the Markdown to copy
next to it. Source: `docs/editors/features.md`.

The basics are below; more copy-paste examples are in `templates/snippets.md`, and the full
list is in the [Material reference](https://squidfunk.github.io/mkdocs-material/reference/).

| You want | Write |
|---|---|
| Heading | `## Section`, `### Subsection` (one `#` title per page) |
| Bold / italic | `**bold**`, `*italic*` |
| Link to a page | `[Shutdown](shutdown.md)` or a section: `[limits](weather-and-safety.md#weather-limits)` |
| Numbered steps | `1. Do this` (next lines `1.` too, it numbers itself) |
| Checklist | `- [ ] item` |
| Keyboard key | `++ctrl+c++` |
| Highlight | `==important==` |
| Command / code | wrap in triple backticks (gets a copy button) |
| Table | see `templates/snippets.md` |

Coloured boxes (the indented text, 4 spaces, belongs to the box):

```markdown
!!! danger "Title"
    For anything that can damage the telescope or hurt someone.

!!! warning
    Easy mistakes.

!!! tip
    Shortcuts and good habits.

!!! note
    Background information.

!!! todo "TODO"
    Not written yet.

??? question "Collapsible box (closed until clicked)"
    Good for troubleshooting entries.
```

### Glossary and shared text

- **Abbreviations:** add a line `*[OCS]: Observatory control system` to
  `includes/abbreviations.md`. Every "OCS" on every page then gets a tooltip.
- **Shared boxes or paragraphs:** put them in a file in `includes/` and pull them into any
  page with a line `--8<-- "filename.md"`. Edit once, it changes everywhere.

### Diagrams and math need internet

Mermaid diagrams and math formulas load a library from the internet when the page opens.
On site without internet they show as plain text. The `privacy` plugin can download them
into the site (see the end of the feature showcase).

## 6. House rules for content

- **Never guess a procedure or a limit.** If it isn't confirmed, leave a `TODO` box saying
  what is missing. A wrong instruction is worse than a missing one.
- **Steps are numbered and one action each**: "Click *Park*", not a paragraph.
- **Say what the observer should see** after a step ("the roof status shows *closed*").
- **Safety goes in `danger` boxes**, at the top of the step where it matters.
- **No passwords, keys or private phone numbers in this repo.** Say where to get them instead.
- Screenshots from the real system, cropped to the part that matters.
- Put the date in a note when something is temporary ("Since 2026-11: dome camera offline").

## 7. Check before you commit

```bash
uv run mkdocs build --strict
```

Fails on broken links and missing images (a page missing from `nav:` is only reported as INFO, so check the menu yourself). Fix what it says, then:

```bash
git switch -c docs/startup-procedure     # short branch per topic
git add -A
git commit -m "Write startup procedure"
git push -u origin docs/startup-procedure # then open a PR, someone else reads it
```

## 8. Publish

`uv run mkdocs build` writes the finished website into `site/`: plain HTML files, no server
software needed.

- **On site (`ocs-server`)**: copy `site/` to a folder served by nginx. Works without
  internet. TODO: decide path/URL and write the deploy command here.
- **GitHub Pages**: `uv run mkdocs gh-deploy` (once the repo is on GitHub).

TODO: pick one and record it here.

## 9. Tooling note

Material for MkDocs reaches **end of life on 5 May 2027** (security fixes until then; the
build prints a notice about it). Its successor [Zensical](https://zensical.org) (same authors)
reads this same `mkdocs.yml` and Markdown: see the
[migration guide](https://zensical.org/docs/compatibility/mkdocs/migration/). Plan to switch
before that date; the content in `docs/` doesn't change.

The "MkDocs 2.0" warning at build time can be silenced with `NO_MKDOCS_2_WARNING=1`.
