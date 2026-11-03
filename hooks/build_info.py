"""MkDocs hook: put the manual's version and date into config.extra.

Used by the PDF cover page (pdf/cover_page.tpl) as {{ config.extra.manual_version }}
and {{ config.extra.manual_date }}.
"""

import datetime
import subprocess


def _git(*args: str) -> str | None:
    try:
        out = subprocess.run(
            ["git", *args], capture_output=True, text=True, check=True, timeout=10
        )
        return out.stdout.strip() or None
    except (OSError, subprocess.SubprocessError):
        return None


def on_config(config, **kwargs):
    # v1.2.0 when on a tag, v1.2.0-3-gabc1234 after it, abc1234 without tags;
    # "-dirty" means uncommitted changes went into this build.
    version = _git("describe", "--tags", "--always", "--dirty") or "unknown"
    dirty = version.endswith("-dirty")
    date = datetime.date.today().isoformat() if dirty else _git("log", "-1", "--format=%cs")
    config.extra["manual_version"] = version
    config.extra["manual_date"] = date or datetime.date.today().isoformat()
    return config
