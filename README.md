# Mini-Pipeline Bio-informatique : Analyse de Séquence ADN & Traduction Protéique

Un outil en ligne de commande (CLI) développé en **Python** permettant d'analyser des séquences nucléotidiques (composition, taux de GC, recherche de motifs) et de simuler la traduction biologique de l'ADN en séquence protéique selon le code génétique standard.

---

## Objectifs et Contexte du Projet

En bio-informatique, le traitement primaire d'une séquence génomique consiste à extraire ses propriétés statistiques fondamentales et à identifier ses cadres ouverts de lecture (*ORF - Open Reading Frames*) pour prédire la protéine synthétisée.

Ce projet implémente un mini-pipeline sans dépendance externe (Python natif) permettant de :
1. **Parser et nettoyer** des séquences brutes ou issues de fichiers standards `.fasta` (suppression des en-têtes `>`, espaces et retours à la ligne, normalisation de la casse).
2. **Analyser la composition nucléotidique** : calcul de la longueur, décompte des bases (A, T, G, C) et calcul du **pourcentage de GC (%GC)**, indicateur clé de la stabilité thermique de la molécule d'ADN.
3. **Rechercher des motifs génétiques** : localisation des index d'apparition d'une sous-séquence spécifique (par défaut le codon d'initiation `ATG`).
4. **Traduire l'ADN en protéine** : découpage en triplets de nucléotides (codons), gestion du cadre de lecture (*reading frame* 0, 1 ou 2) et traduction en acides aminés (code IUPAC à 1 lettre) jusqu'à la rencontre d'un codon STOP (`TAA`, `TAG`, `TGA`).

---

## Fonctionnalités

* **Chargement flexible** : Analyse d'une séquence par défaut ou importation dynamique de fichiers `.fasta` (issus de banques de données comme le NCBI).
* **Menu interactif en console** : Navigation fluide entre l'analyse statistique, la traduction protéique et le changement de fichier.
* **Gestion des cadres de lecture** : Possibilité de décaler la fenêtre de lecture (`frame = 0, 1, 2`) pour observer l'impact d'un décalage de cadre sur la séquence peptidique générée.

---

## Prérequis et Installation

Aucune bibliothèque tierce n'est requise. Il suffit de disposer de **Python 3.x** installé sur votre machine.

1. Cloner ce dépôt (ou télécharger les fichiers) :
   ```bash
   git clone [https://github.com/Emy584/analyseur_adn.git](https://github.com/Emy584/analyseur_adn.git)
   cd bio-analyse-adn
   ```

2. Lancer le programme dans un terminal :
   ```bash
   python bio_analyse.py
   ```
   *(ou `python3 bio_analyse.py` sous macOS / Linux)*

---

## Exemple d'Exécution (Gène humain *ACE2*)

Test réalisé sur un extrait de 161 bases de la région codante du gène humain **ACE2** (*Homo sapiens angiotensin converting enzyme 2*, NCBI).

### 1. Analyse statistique et recherche du codon Start (`ATG`)

```text
*** ANALYSE DE LA SEQUENCE ***
Séquence propre : ATGTCAAGCTCTTCCTGGCTCCTTCTCAGCCTTGTTGCTGTAACTGCTGCTCAGTCCACCATTGAGGAACAGGCCAAGACATTTTTGGACAAGTTTAACCACGAAGCCGAAGACCTGTTCTATCAAAGTTCACTTGCTTCTTGGAATTATAACACCAATAT
Longueur : 161
Nombre de A : 42
Nombre de T : 48
Nombre de G : 29
Nombre de C : 42
Pourcentage de Guanine et de Cytosine : 44.099
Position trouvée : 0
```

### 2. Traduction en protéine (Cadre de lecture 0)

```text
*** TRADUCTION ***
Séquence protéique : MSSSSWLLLSLVAVTAAQSTIEEQAKTFLDKFNHEAEDLFYQSSLASWNYNTN
Longueur de la protéine : 53 acides aminés
```
*(Note : La séquence obtenue `MSSSSWLLLSLVAVTAA...` correspond exactement au peptide signal et au domaine N-terminal de la protéine ACE2 humaine référencée sur UniProt).*

---

## Structure du Code

| Fonction | Rôle |
| :--- | :--- |
| `lecture_fichier(nom_fichier)` | Ouvre un fichier `.fasta`, ignore la ligne d'en-tête (`>`) et concatène la séquence. |
| `nettoyer_sequence(sequence)` | Normalise la chaîne en majuscules et supprime les espaces et sauts de ligne (`\n`). |
| `analyser_sequence(sequence, motif)` | Calcule la longueur, les fréquences A/T/G/C, le `%GC` et relève les positions du `motif`. |
| `traduire_sequence(sequence, frame)` | Parcourt la séquence par pas de 3 à partir de `frame` et traduit chaque codon via le dictionnaire génétique jusqu'à un codon STOP (`*`). |

---

## Pistes d'Amélioration

* **Détection automatique des ORF** : Démarrer automatiquement la traduction au premier codon `ATG` détecté dans la séquence.
* **Brin complémentaire inverse** : Générer le brin anti-sens (`A↔T`, `C↔G` inversé) pour analyser les 6 cadres de lecture possibles (3 sens + 3 anti-sens).
* **Transcription ARNm** : Ajouter une étape intermédiaire convertissant la Thymine (`T`) en Uracile (`U`).