# Contributor Guide

## Code Style
- Extensive use of comments are encouraged to make the code human readable
- Preferred style of comment is a hash indented to the same level as the code line with a short horizontal line, the comment and a longer horizontal line after. Here follows some examples at different levels of indentation:

           # ───── main entry point ─────────────────────────────────────────────────
            # ── 0. Quick reachability check ───────────────────────────────────
                # ── 1. fetch model + firmware (no login needed) ────────────────────────────────────────────────

- Tkinter "clam" theme is preferred wherever it could be applied
## Rules
- There may sometimes be supplemental notes and instructions embedded in the Python code that will aid in understanding and provide guidance on the task. Such notes will always start with "#Note to developer":
- Always update the Last Update date at the top of the Python files to show the current Date and time of the change in GMT+2 in the format YYYY-MM-DD HH:MM.
- Always update the version in gVER of all Python files with the same release number that goes into the RELEASE_NOTES.md and keep all files in sync.
- Always add time and date stamped release notes to the top of RELEASE_NOTES.md file that shortly explains what was done, gives the reason for the change as well as shortly explains how the change was accomplished.
- Set the variable `DISPLAY_RELEASE_NOTES` in `BraaSMAN.conf` to `TRUE` whenever a new entry is added to `RELEASE_NOTES.md` so the release notes show on next start.

## Testing
- Testing is regarded as completed if the code compiles without errors
