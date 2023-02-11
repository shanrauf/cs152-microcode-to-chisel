# COMSCPI 152 (CS152) Microcode Table To Chisel Converter

A program that converts a microcode table (.csv) to the Scala Chisel format.

# Usage

1. Fill out `yourinst.csv`, which is currently populated with a replica of the MOVN instruction.
1. `python chisel.py`

# Example Output (MOVN):

```
,Label("MOVN")

,Signals(Cat(CSR.N, LDIR_0, RS_RS1, RWR_0, REN_1, LDA_1, LDB_X, ALU_X, AEN_0, LDMA_X, MWR_0, MEN_0, MT_X, IS_X, IEN_0, UBR_N), "X")

,Signals(Cat(CSR.N, LDIR_0, RS_RS2, RWR_0, REN_1, LDA_0, LDB_1, ALU_X, AEN_0, LDMA_X, MWR_0, MEN_0, MT_X, IS_X, IEN_0, UBR_N), "X")

,Signals(Cat(CSR.N, LDIR_0, RS_X, RWR_0, REN_0, LDA_0, LDB_0, ALU_COPY_B, AEN_0, LDMA_X, MWR_0, MEN_0, MT_X, IS_X, IEN_0, UBR_EZ), "FETCH")

,Signals(Cat(CSR.N, LDIR_0, RS_RD, RWR_1, REN_0, LDA_0, LDB_0, ALU_COPY_A, AEN_1, LDMA_X, MWR_0, MEN_0, MT_X, IS_X, IEN_0, UBR_J), "FETCH")
```

# Notes
- If migrating from the table format on the homeworks/discussions to the .csv, it is trivial to copy/paste all of the columns except the pseudocode column, which you have to copy and then double click into a cell before pasting it (so that formatting is good)
