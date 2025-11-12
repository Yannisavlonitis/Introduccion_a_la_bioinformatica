def amino_lab (dna, inv):
    directo = {}
    inicio = [] #codones de inicio
    completo = {} #directo
    bases = {0:'A', 1:'U', 2:'G', 3:'C'}
    trad = []
    
    for i in range(4):
        for j in range(4):
            for k in range(4):
                completo[bases[i]+bases[j]+bases[k]] = ''
    
    for i in range(len(dna)):
        dna[i]= ''.join(dna[i].upper().replace('T','U').split())
        # esto está guardado en la lista dna
    for aa in inv:
        for codon in inv.get(aa):
            if aa != 'Z': # también puedo meterlo y sacarlo con pop a un dicc de codones de inicio
                if codon not in directo:
                    directo[codon] = aa
                else:
                    return False  #print false?
            else: # Creo que no hace falta elif, solo con else. 
                inicio.append(codon) # creo que inicio tiene q ser una lista en vez de un diccionario
    
    for codon in completo:
       if codon not in directo:
           directo[codon] = '_'   
    
    import re
    c = 0           # buscamos el inicio de traducción
    for cadena in dna:
        prot = ''
        for i in inicio:
            iniciotrad = re.search(i, cadena)
            if iniciotrad != None:
                dna[c] = cadena[iniciotrad.start():]
                
                for i in range(0,len(dna[c])-2,3):
                    triplete = dna[c][i:i+3]
                    
                    aa = directo.get(triplete)
                    if aa == 'X':
                        break
                    prot = prot + aa
                trad.append(prot)
                c += 1
                break
            else:
                dna[c] = 'No traducible'
                trad.append(dna[c])
                c += 1
                break
         
    
    return (trad)        
            
                
inp = input("Inserta una secuencia de DNA de <700 bases: ")
secuencia = [inp]
codgen = {
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'N': ['AAU', 'AAC'],
    'D': ['GAU', 'GAC'],
    'C': ['UGU', 'UGC'],
    'Q': ['CAA', 'CAG'],
    'E': ['GAA', 'GAG'],
    'G': ['GGU', 'GGC', 'GGA', 'GGG'],
    'H': ['CAU', 'CAC'],
    'I': ['AUU', 'AUC', 'AUA'],
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],
    'K': ['AAA', 'AAG'],
    'M': ['AUG'],
    'F': ['UUU', 'UUC'],
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],
    'W': ['UGG'],
    'Y': ['UAU', 'UAC'],
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],
    'X': ['UAA', 'UAG', 'UGA'],  # codones de parada
    'Z': ['AUG', 'CUG', 'UUG']   # posibles codones de inicio
}



print(amino_lab(secuencia, codgen))
