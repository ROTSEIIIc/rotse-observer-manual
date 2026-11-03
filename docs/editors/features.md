---
title: Feature showcase
description: Everything this site can render, with the Markdown that produces it.
icon: material/palette
tags:
  - editors
  - reference
---

# Feature showcase

Everything this manual can do. Each example has a **Result** tab (what observers see) and a
**Markdown** tab (what you type). Copy from the Markdown tab.

!!! info "For editors"
    This page is for people writing the manual, not observers. Full documentation:
    [Material for MkDocs reference](https://squidfunk.github.io/mkdocs-material/reference/).
    The examples about the telescope are made up to show the syntax. They are **not** real
    procedures.

---

## Text formatting

=== "Result"

    **Bold**, *italic*, ***both***, ==highlighted==, ^^inserted^^, ~~struck out~~,
    `inline code`.

    Sub- and superscript: H~2~O, 10^-3^, m^2^.

    Keys: ++ctrl+c++, ++cmd+shift+p++, ++enter++, ++esc++.

    Smart symbols: (c) (r) (tm) --> <-- +/- != 1/2 1st 2nd.

=== "Markdown"

    ```markdown
    **Bold**, *italic*, ***both***, ==highlighted==, ^^inserted^^, ~~struck out~~,
    `inline code`.

    Sub- and superscript: H~2~O, 10^-3^, m^2^.

    Keys: ++ctrl+c++, ++cmd+shift+p++, ++enter++, ++esc++.

    Smart symbols: (c) (r) (tm) --> <-- +/- != 1/2 1st 2nd.
    ```

### Suggested changes (Critic markup)

Useful when proposing a change to someone else's text in a pull request.

=== "Result"

    Close the roof when humidity exceeds {--80--}{++85++} %.
    {~~Open~>Check the weather, then open~~} the roof.
    {==Is this limit still right?==}{>>Ask the site manager.<<}

=== "Markdown"

    ```markdown
    Close the roof when humidity exceeds {--80--}{++85++} %.
    {~~Open~>Check the weather, then open~~} the roof.
    {==Is this limit still right?==}{>>Ask the site manager.<<}
    ```

---

## Headings and contents

Every `##` and `###` heading appears in the **table of contents** on the right and gets a
permalink (hover the heading, click the ¶). Link to a heading with `page.md#heading-text`
in lowercase with hyphens.

```markdown
# Page title (only one per page)
## Section
### Subsection
#### Sub-subsection (not shown in the contents)
```

---

## Lists

=== "Result"

    1. Numbered step
    2. Next step
        - a detail (indent 4 spaces)
        - another detail
    3. Last step

    - [x] Checklist item, done
    - [ ] Checklist item, open

    Definition list
    :   A term with its explanation. Good for glossaries.

    Park position
    :   Where the mount goes at the end of the night.

=== "Markdown"

    ```markdown
    1. Numbered step
    2. Next step
        - a detail (indent 4 spaces)
        - another detail
    3. Last step

    - [x] Checklist item, done
    - [ ] Checklist item, open

    Definition list
    :   A term with its explanation. Good for glossaries.

    Park position
    :   Where the mount goes at the end of the night.
    ```

!!! tip
    Write `1.` on every line of a numbered list if you like; it numbers itself. Leave a
    blank line before a list.

---

## Links, footnotes, abbreviations

=== "Result"

    Link to a page: [Shutdown](../shutdown.md).
    Link to a section: [weather limits](../weather-and-safety.md#weather-limits).
    External: [pyobs](https://www.pyobs.org "pyobs website").
    Footnote[^1].

    Abbreviations get a tooltip automatically: the pyobs modules talk via XMPP, images
    are saved as FITS. Hover over them.

    [^1]: Footnotes collect at the bottom of the page.

=== "Markdown"

    ```markdown
    Link to a page: [Shutdown](../shutdown.md).
    Link to a section: [weather limits](../weather-and-safety.md#weather-limits).
    External: [pyobs](https://www.pyobs.org "pyobs website").
    Footnote[^1].

    Abbreviations get a tooltip automatically: the pyobs modules talk via XMPP, images
    are saved as FITS. Hover over them.

    [^1]: Footnotes collect at the bottom of the page.
    ```

Links are relative to the current file: pages in `docs/` link with `shutdown.md`; this page
is in `docs/editors/`, so it needs `../shutdown.md`.

Abbreviations are defined once in `includes/abbreviations.md` and work on every page. Add new
ones there.

---

## Admonitions (coloured boxes)

All types, each with its own colour and icon:

!!! note
    `note`: background information.

!!! abstract
    `abstract` (also `summary`): a short summary.

!!! info
    `info` (also `todo`): extra information.

!!! tip
    `tip` (also `hint`): shortcuts and good habits.

!!! success
    `success` (also `check`): things that worked.

!!! question
    `question` (also `help`, `faq`): troubleshooting entries.

!!! warning
    `warning` (also `caution`, `attention`): easy mistakes.

!!! failure
    `failure` (also `fail`, `missing`): known not to work.

!!! danger
    `danger` (also `error`): damage or injury.

!!! bug
    `bug`: known software bugs.

!!! example
    `example`: worked examples.

!!! quote
    `quote` (also `cite`): quotations.

### Box variants

=== "Result"

    !!! warning "Custom title"
        Any title in quotes.

    !!! note ""
        No title at all.

    ??? question "Collapsible, closed (click me)"
        Hidden until clicked.

    ???+ tip "Collapsible, open"
        Shown, can be collapsed.

    !!! danger "Boxes can be nested"
        Outer box.

        !!! tip
            Inner box.

=== "Markdown"

    ```markdown
    !!! warning "Custom title"
        Any title in quotes.

    !!! note ""
        No title at all.

    ??? question "Collapsible, closed (click me)"
        Hidden until clicked.

    ???+ tip "Collapsible, open"
        Shown, can be collapsed.

    !!! danger "Boxes can be nested"
        Outer box.

        !!! tip
            Inner box.
    ```

### Box beside the text

=== "Result"

    !!! info inline end "Side note"
        Floats to the right of the text that follows.

    This paragraph wraps around the box on the right. Good for short side remarks next
    to a procedure, without breaking up the steps. On a phone it stacks above the text
    instead. Use `inline` (left) or `inline end` (right).

=== "Markdown"

    ```markdown
    !!! info inline end "Side note"
        Floats to the right of the text that follows.

    This paragraph wraps around the box on the right. ...
    ```

---

## Content tabs

Good for "on site vs. remote" or "macOS vs. Linux". Tabs with the same labels switch
together across the whole page: click **Remote** here and the second group follows.

=== "Result"

    === "On site"

        Walk to the control room and log in to the console.

    === "Remote"

        Connect to the VPN first, then start the GUI.

    === "On site"

        Check the roof visually.

    === "Remote"

        Check the roof on the webcam.

=== "Markdown"

    ```markdown
    === "On site"

        Walk to the control room and log in to the console.

    === "Remote"

        Connect to the VPN first, then start the GUI.
    ```

---

## Code blocks

Every code block gets a **copy button** (top right, on hover).

=== "Result"

    ```bash title="Start the sandbox"
    cd ~/rotse-dev/rotse-sandbox
    ./sandbox up
    ./sandbox gui
    ```

    With line numbers, lines 2–3 highlighted:

    ```yaml linenums="1" hl_lines="2 3"
    class: pyobs_schier.DummySchierTelescope
    name: Telescope
    min_altitude: 20
    ```

    Inline code with highlighting: `#!python print("hello")`.

=== "Markdown"

    ````markdown
    ```bash title="Start the sandbox"
    cd ~/rotse-dev/rotse-sandbox
    ./sandbox up
    ./sandbox gui
    ```

    With line numbers, lines 2–3 highlighted:

    ```yaml linenums="1" hl_lines="2 3"
    class: pyobs_schier.DummySchierTelescope
    name: Telescope
    min_altitude: 20
    ```

    Inline code with highlighting: `#!python print("hello")`.
    ````

### Code annotations

Click the (+) markers.

=== "Result"

    ```yaml
    class: pyobs_schier.DummySchierTelescope  # (1)!
    min_altitude: 20  # (2)!
    ```

    1.  The Python class pyobs loads for this module.
    2.  Example value only. Annotations can hold **any Markdown**, even lists and links.

=== "Markdown"

    ````markdown
    ```yaml
    class: pyobs_schier.DummySchierTelescope  # (1)!
    min_altitude: 20  # (2)!
    ```

    1.  The Python class pyobs loads for this module.
    2.  Example value only. Annotations can hold **any Markdown**, even lists and links.
    ````

The `!` in `(1)!` removes the comment marker itself, leaving only the (+).

---

## Tables

=== "Result"

    | Left aligned | Centred | Right aligned |
    |:---|:---:|---:|
    | Cloud | TODO | 1 |
    | Rain | TODO | 10 |
    | Wind | TODO | 100 |

=== "Markdown"

    ```markdown
    | Left aligned | Centred | Right aligned |
    |:---|:---:|---:|
    | Cloud | TODO | 1 |
    | Rain | TODO | 10 |
    | Wind | TODO | 100 |
    ```

The `:` in the second line sets the alignment. Tables don't need to line up in the source.

---

## Images

=== "Result"

    Plain, with a set width:

    ![ROTSE logo](../assets/rotse.png){ width="120" }

    With a caption:

    <figure markdown="span">
      ![ROTSE logo](../assets/rotse.png){ width="120" }
      <figcaption>The ROTSE Namibia logo</figcaption>
    </figure>

    ![ROTSE logo](../assets/rotse.png){ align=right width="80" }
    Aligned right with `align=right`: the text flows around the image on the left.
    Use `align=left` for the other side. Good for small photos of a switch or a
    connector next to the instruction about it.

=== "Markdown"

    ```markdown
    ![ROTSE logo](../assets/rotse.png){ width="120" }

    <figure markdown="span">
      ![ROTSE logo](../assets/rotse.png){ width="120" }
      <figcaption>The ROTSE Namibia logo</figcaption>
    </figure>

    ![ROTSE logo](../assets/rotse.png){ align=right width="80" }
    Aligned right with `align=right`: ...
    ```

Other image options:

| Option | Markdown | Use |
|---|---|---|
| Lazy loading | `![x](a.png){ loading=lazy }` | Long pages with many screenshots |
| Dark mode only | `![x](a-dark.png#only-dark)` | Screenshots taken in the dark GUI theme |
| Light mode only | `![x](a-light.png#only-light)` | The same screenshot in light theme |

---

## Buttons

=== "Result"

    [Start the night](../startup.md){ .md-button .md-button--primary }
    [Troubleshooting](../troubleshooting.md){ .md-button }

=== "Markdown"

    ```markdown
    [Start the night](../startup.md){ .md-button .md-button--primary }
    [Troubleshooting](../troubleshooting.md){ .md-button }
    ```

---

## Icons and emojis

Over 10 000 icons. Search them on the
[icon search page](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search).

=== "Result"

    :material-telescope: Telescope ·
    :material-home-roof: Roof ·
    :material-weather-pouring: Rain ·
    :material-weather-night: Night ·
    :material-camera: Camera ·
    :material-shield-alert: Safety ·
    :material-phone: Phone ·
    :fontawesome-solid-satellite: Satellite ·
    :fontawesome-solid-moon: Moon

    Emojis: :star: :warning: :white_check_mark: :x: :telescope:

=== "Markdown"

    ```markdown
    :material-telescope: Telescope ·
    :material-home-roof: Roof ·
    :material-weather-pouring: Rain ·
    :material-weather-night: Night ·
    :material-camera: Camera ·
    :material-shield-alert: Safety ·
    :material-phone: Phone ·
    :fontawesome-solid-satellite: Satellite ·
    :fontawesome-solid-moon: Moon

    Emojis: :star: :warning: :white_check_mark: :x: :telescope:
    ```

---

## Grids and cards

Good for overview pages, like the home page.

=== "Result"

    <div class="grid cards" markdown>

    -   :material-power: __Startup__

        ---

        Bring the system up and open the roof.

        [:octicons-arrow-right-24: Startup](../startup.md)

    -   :material-telescope: __Observing__

        ---

        Point, track and take images.

        [:octicons-arrow-right-24: Observing](../observing.md)

    -   :material-weather-pouring: __Weather & safety__

        ---

        Limits for opening and closing.

        [:octicons-arrow-right-24: Weather & safety](../weather-and-safety.md)

    -   :material-power-sleep: __Shutdown__

        ---

        Park, close, check.

        [:octicons-arrow-right-24: Shutdown](../shutdown.md)

    </div>

=== "Markdown"

    ```markdown
    <div class="grid cards" markdown>

    -   :material-power: __Startup__

        ---

        Bring the system up and open the roof.

        [:octicons-arrow-right-24: Startup](../startup.md)

    -   :material-telescope: __Observing__

        ---

        Point, track and take images.

        [:octicons-arrow-right-24: Observing](../observing.md)

    </div>
    ```

---

## Diagrams (Mermaid)

Drawn from text, so they're easy to change. Syntax:
[mermaid.js.org](https://mermaid.js.org/intro/).

### Flowchart

=== "Result"

    ```mermaid
    flowchart LR
      A[Check weather] --> B{Safe?}
      B -- yes --> C[Open roof]
      B -- no --> D[Stay closed]
      C --> E[Observe]
      E --> F[Park and close]
    ```

=== "Markdown"

    ````markdown
    ```mermaid
    flowchart LR
      A[Check weather] --> B{Safe?}
      B -- yes --> C[Open roof]
      B -- no --> D[Stay closed]
      C --> E[Observe]
      E --> F[Park and close]
    ```
    ````

### Sequence diagram

=== "Result"

    ```mermaid
    sequenceDiagram
      participant O as Observer (GUI)
      participant T as Telescope module
      O->>T: move to RA/Dec
      T-->>O: SLEWING
      T-->>O: TRACKING
    ```

=== "Markdown"

    ````markdown
    ```mermaid
    sequenceDiagram
      participant O as Observer (GUI)
      participant T as Telescope module
      O->>T: move to RA/Dec
      T-->>O: SLEWING
      T-->>O: TRACKING
    ```
    ````

### State diagram

=== "Result"

    ```mermaid
    stateDiagram-v2
      [*] --> Closed
      Closed --> Opening
      Opening --> Open
      Open --> Closing
      Closing --> Closed
    ```

=== "Markdown"

    ````markdown
    ```mermaid
    stateDiagram-v2
      [*] --> Closed
      Closed --> Opening
      Opening --> Open
      Open --> Closing
      Closing --> Closed
    ```
    ````

Mermaid also does pie charts, Gantt charts (e.g. a night plan), timelines and more.

---

## Math

=== "Result"

    Inline: the airmass is roughly \(X \approx \sec z\).

    Block:

    $$
    m = -2.5 \log_{10}\left(\frac{F}{F_0}\right)
    $$

=== "Markdown"

    ```markdown
    Inline: the airmass is roughly \(X \approx \sec z\).

    Block:

    $$
    m = -2.5 \log_{10}\left(\frac{F}{F_0}\right)
    $$
    ```

---

## Reusing text (includes)

Write a warning once and use it on several pages. Shared pieces live in `includes/` (outside
`docs/`, so they aren't pages themselves).

=== "Result"

    --8<-- "roof-warning.md"

=== "Markdown"

    ```markdown
    ;--8<-- "roof-warning.md"
    ```


---

## Page settings (front matter)

An optional block at the very top of a `.md` file, between `---` lines:

```yaml
---
title: Feature showcase        # title in the browser tab and menu, if different from the # heading
description: One sentence      # for search engines and link previews
icon: material/palette         # icon next to the page in the menu
tags:                          # listed on the Tags page
  - editors
hide:                          # hide parts of the layout on this page
  - navigation                 # left menu
  - toc                        # right contents
  - footer                     # previous/next links
---
```

This page uses `title`, `description`, `icon` and `tags`. See it on the
[Tags](tags.md) page.

---

## Site-wide options (in `mkdocs.yml`)

Switched on or off in `mkdocs.yml`, not per page. The disabled ones are already in the file as
comments: remove the `#` to try them.

| Feature | Setting | Effect | Here |
|---|---|---|---|
| Dark / light toggle | `theme.palette` | Sun/moon button in the header | on |
| Search | `plugins: search` | Search box | on |
| Tags | `plugins: tags` | Tag pages by topic | on |
| Copy button | `content.code.copy` | On every code block | on |
| Back to top | `navigation.top` | Button when scrolling up | on |
| Prev / next | `navigation.footer` | Links at the bottom of each page | on |
| Section index pages | `navigation.indexes` | A menu group can have its own page | on |
| Top tabs | `navigation.tabs` | Top-level menu as tabs under the header | off |
| Instant loading | `navigation.instant` | Faster page changes, no full reload | off |
| Expanded menu | `navigation.expand` | All menu groups open | off |
| Contents in menu | `toc.integrate` | Right-hand contents moves into the left menu | off |
| Auto-hide header | `header.autohide` | More room on small screens | off |
| Edit button | `content.action.edit` | "Edit this page" link to GitHub (needs `repo_url`) | off |
| Offline plugin | `plugins: offline` | Site works opened from a folder or USB stick, no server | off |
| Privacy plugin | `plugins: privacy` | Downloads external scripts (Mermaid, MathJax) into the site, so they work without internet | off |
| Blog plugin | `plugins: blog` | Blog section, e.g. a night log or news for observers | off |
| Social cards | `plugins: social` | Preview images for links (needs extra system libraries) | off |
| Language | `theme.language: de` | Interface in another language | `en` |
