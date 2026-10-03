# dictionnaire
table_codons = {
    "ATA":"I", "ATC":"I", "ATT":"I", "ATG":"M",
    "ACA":"T", "ACC":"T", "ACG":"T", "ACT":"T",
    "AAC":"N", "AAT":"N", "AAA":"K", "AAG":"K",
    "AGC":"S", "AGT":"S", "AGA":"R", "AGG":"R",
    "CTA":"L", "CTC":"L", "CTG":"L", "CTT":"L",
    "CCA":"P", "CCC":"P", "CCG":"P", "CCT":"P",
    "CAC":"H", "CAT":"H", "CAA":"Q", "CAG":"Q",
    "CGA":"R", "CGC":"R", "CGG":"R", "CGT":"R",
    "GTA":"V", "GTC":"V", "GTG":"V", "GTT":"V",
    "GCA":"A", "GCC":"A", "GCG":"A", "GCT":"A",
    "GAC":"D", "GAT":"D", "GAA":"E", "GAG":"E",
    "GGA":"G", "GGC":"G", "GGG":"G", "GGT":"G",
    "TCA":"S", "TCC":"S", "TCG":"S", "TCT":"S",
    "TTC":"F", "TTT":"F", "TTA":"L", "TTG":"L",
    "TAC":"Y", "TAT":"Y", "TAA":"*", "TAG":"*",
    "TGC":"C", "TGT":"C", "TGA":"*", "TGG":"W"
}

# fonction de lecture 
def lecture_fichier(nom_fichier):
    sequence = ""
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            if not ligne.startswith(">"):
                sequence += ligne
    return nettoyer_sequence(sequence)


# fonction de nettoyage
def nettoyer_sequence(sequence): 
    return sequence.upper().replace(" ", "").replace("\n", "")

# fonction d'analyse
def analyser_sequence(sequence, motif  = "ATG"):
    longueur = len(sequence)
    positions = []

    nb_a = sequence.count("A")
    nb_t = sequence.count("T")
    nb_g = sequence.count("G")
    nb_c = sequence.count("C")

    # calcul
    pourcentage_gc = ((nb_g + nb_c) / longueur) * 100
    pourcentage_gc = round(pourcentage_gc, 3)

    # position
    for i in range(longueur):
        if sequence[i : i + 3] == motif:
            positions.append(i) 

    print("*** ANALYSE DE  LA SEQUENCE ***")
    print(f"Séquence propre : {sequence}")
    print(f"Longueur : {longueur}")
    print(f"Nombre de A : {nb_a}")
    print(f"Nombre de T : {nb_t}")
    print(f"Nombre de G : {nb_g}")
    print(f"Nombre de C : {nb_c}")
    print(f"Pourcentage de Guanine et de Cytosine : {pourcentage_gc}")

    for pos in positions:
        print(f"Position trouvée : {pos}")
   

# fonction de traduction
def traduire_sequence(sequence, frame=0):
    proteine = ""
     
    for i in range(frame, len(sequence) - 2, 3):
        codon = sequence[i : i + 3]
        acide_amine = table_codons.get(codon, "?")

        if acide_amine == "*":
            break
    
        proteine += acide_amine

    print("*** TRADUCTION ***")
    print(f"Séquence protéique : {proteine}")
    print(f"Longueur de la protéine : {len(proteine)} acides aminés")


# variable
adn_brut = "atg cgt acc\ntga taa"
adn_propre = nettoyer_sequence(adn_brut)

# main
# sequence par defaut
adn_brut = "atg cgt acc\ntga taa"
adn_propre = nettoyer_sequence(adn_brut)

# main
while True:
    print("\n*** MENU ***")
    print("1 : Analyser la séquence")
    print("2 : Traduire la séquence")
    print("3 : Charger un fichier .fasta")
    print("4 : Quitter")

    choix = input("Ton choix : ")

    if choix == "1":
        motif_choisi = input("Motif à chercher (Entrée pour 'ATG' par défaut) : ")
        if motif_choisi == "":
            analyser_sequence(adn_propre)
        else:
            analyser_sequence(adn_propre, motif_choisi.upper())

    elif choix == "2":
        cadre = int(input("Cadre de lecture (0, 1 ou 2) : "))
        traduire_sequence(adn_propre, frame=cadre)

    elif choix == "3":
        nom = input("Nom du fichier (ex: ace2.fasta) : ")
        adn_propre = lecture_fichier(nom)
        print("Nouvelle séquence chargée avec succès")

    elif choix == "4":
        break

    else:
        print("Choix invalide, veuillez taper 1, 2, 3 ou 4.")





        
