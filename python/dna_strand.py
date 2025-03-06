def dna_strand(dna):
    new_dna = ""
    
    for elem in dna:
        match elem:
            case "A":
                new_dna += "T"
            case "T":
                new_dna += "A"                
            case "C":
                new_dna += "G"               
            case "G":
                new_dna += "C"
    return new_dna

print(dna_strand("ATCG"))