# Grindstone

A grinding game that runs in your terminal.

Chop trees, burn logs, watch numbers go up. It's inspired by old school RuneScape, but it lives entirely in a text interface, so there is no clicking around a game world and no combat that depends on your reaction time. What's left is the part I actually like about those games: skills, XP, gear tiers, and the slow climb.

## Status

Early. Very early. Right now there is a woodcutting skill, a firemaking skill, a shop that sells one axe, and a save file. Everything else is planned.

I'm building this to learn, so the code grows as I do. Expect it to be rough in places.

## What it does so far

* Gather coins (a temporary way to get some starting coins)
* Chop trees to get logs and woodcutting XP
* Buy an axe from a shop with coins

## Planned

* Save file
* Offline grind
* Better item functions
* More trees and more axes, each with level requirements
* More skills (firemaking, fishing and cooking are next, they pair the same way woodcutting and firemaking do)
* A proper interface built with Textual instead of plain text menus
* A bank, so your inventory stops being the bottleneck
* Combat, eventually, once the skilling side feels good
* Portuguese translation

## Running it

You need Python 3.11 or newer.

```
git clone https://github.com/FernandesTiago/grindstone
cd grindstone
python game.py
```

No dependencies yet. That will change once the Textual interface lands.

Windows works, but use Windows Terminal rather than the old cmd window, otherwise the box characters render as garbage.

## Save files

Saves live in your home folder under `.grindstone`. They're plain JSON, so if something breaks you can open the file and see exactly what went wrong. Or edit it and cheat. It's a single player game, I'm not going to stop you.

## Why terminal

Two reasons. The honest one is that I don't know how to build a web frontend or work with a game engine yet. The better one is that a grinding game doesn't really need either. The genre is about progression systems and the loop, not graphics, and text is a fine way to show a number getting bigger.

## About the project

I'm learning Python and this is my practice ground. If you read the code and something looks wrong, it probably is, and I'd like to hear about it.
