# COMSCPI 152 (CS152) Microcode Table To Chisel Converter

A program that converts a microcode table (.csv) to the Scala Chisel format.

# Usage

1. Fill out `yourinst.csv`, which is currently populated with a replica of the MOVN instruction.
1. `python chisel.py`

# Notes
- If migrating from the table format on the homeworks/discussions to the .csv, it is trivial to copy/paste all of the columns except the pseudocode column, which you have to copy and then double click into a cell before pasting it (so that formatting is good)
