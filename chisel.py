import csv

data = []

def cell_value_to_chisel(value):
    value = value.strip()
    if value == "*": return "X"
    else: return value.upper()

def check_only_one_en_flag(arr):
    count = 0
    for val in arr:
        if "_1" in val:
            count += 1
            if count > 1:
                return False
    return True

# Open the .csv file for reading
with open('yourinst.csv', 'r') as csvfile:
    # Create a reader object
    reader = csv.reader(csvfile)

    # Skip first row (headers)
    next(reader)
    
    # Loop over each row in the .csv file
    row_idx = 0
    for row in reader:
        pseudocode = row[1]
        CSR = cell_value_to_chisel(row[18]) if row[18] else "CSR.N"
        LdIR = "LDIR_" + cell_value_to_chisel(row[2])
        RegSel = "RS_" + cell_value_to_chisel(row[3])
        RegWr = "RWR_" + cell_value_to_chisel(row[4])
        EnReg = "REN_" + cell_value_to_chisel(row[5])
        LdA = "LDA_" + cell_value_to_chisel(row[6])
        LdB = "LDB_" + cell_value_to_chisel(row[7])
        ALUOP = "ALU_" + cell_value_to_chisel(row[8])
        EnALU = "AEN_" + cell_value_to_chisel(row[9])
        LdMA = "LDMA_" + cell_value_to_chisel(row[10])
        MemWr = "MWR_" + cell_value_to_chisel(row[11])
        EnMem = "MEN_" + cell_value_to_chisel(row[12])
        MT = cell_value_to_chisel(row[17]) if row[17] else "MT_X"
        ImmSel = "IS_" + cell_value_to_chisel(row[13])
        EnImm = "IEN_" + cell_value_to_chisel(row[14])
        uBr = "UBR_" + cell_value_to_chisel(row[15])

        en_flags = [EnReg, EnALU, EnMem, EnImm]
        if not check_only_one_en_flag(en_flags):
            err_msg = "More than 1 bus flag was enabled for row {}.\nFlags: {}\nPseudocode:\n{}".format(row_idx + 1, en_flags, pseudocode)
            assert False, err_msg

        next_state = row[16].upper().strip()
        if next_state == "FETCH0": next_state = "FETCH"
        next_state = "\"{}\"".format(next_state) if next_state else "\"X\""
        label = row[0].replace(":", "")
        chisel_label = ""
        if label:
            if label == "FETCH0":
              chisel_label += ",Label(\"FETCH\")\n"
            else:
              chisel_label += ",Label(\"{}\")\n".format(label)

        control_flags = ", ".join([CSR, LdIR, RegSel, RegWr, EnReg, LdA, LdB, ALUOP,
                                  EnALU, LdMA, MemWr, EnMem, MT, ImmSel, EnImm, uBr])

        # Add the row to the data list, with a newline character after each row
        data.append("{},Signals(Cat({}), {})".format(chisel_label, control_flags, next_state) + '\n')

        row_idx += 1
        
# Open the text file for writing
with open('output.txt', 'w') as textfile:
    # Write all of the data to the text file in one go
    textfile.writelines(data)
