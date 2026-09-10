# ==========================================
# Noor Ul Ain Fatima - Bioinformatics Project
# DNA Sequence Analyzer & Computational Biology Tool
# ==========================================

# 1. Input: Sample DNA sequence (Adenine, Thymine, Guanine, Cytosine)
dna_sequence = "ATGCGATCGATCGATCGATCGATCGATCGCGCGTATATCGAT"

print("--- Bioinformatics Analysis Dashboard ---")
print(f"Original DNA Sequence: {dna_sequence}\n")

# 2. Calculating the Total Length of the DNA string
sequence_length = len(dna_sequence)
print(f"1. Total Nucleotide Count (Length): {sequence_length} bases")

# 3. Computing GC-Content (Critical for Genomic Stability Research)
g_count = dna_sequence.count('G')
c_count = dna_sequence.count('C')
gc_content = ((g_count + c_count) / sequence_length) * 100

print(f"2. Guanine (G) Count: {g_count}")
print(f"3. Cytosine (C) Count: {c_count}")
print(f"4. Total GC-Content Percentage: {gc_content:.2f}%")

# 4. Simulating DNA-to-RNA Transcription
rna_sequence = dna_sequence.replace('T', 'U')
print(f"5. Transcribed RNA Sequence: {rna_sequence}")
print("-----------------------------------------")
