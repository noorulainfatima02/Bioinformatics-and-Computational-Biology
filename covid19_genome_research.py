# ====================================================================
# Noor Ul Ain Fatima - Advanced Bioinformatics Research Project
# SARS-CoV-2 (COVID-19) Genomic Data Analysis & Structure Mapping
# ====================================================================

# Asli COVID-19 Virus ka Structural Spike Protein RNA Sequence (Sample Fragment)
# Source Reference: Standard National Center for Biotechnology Information (NCBI) GenBank
covid19_rna_sequence = "AUGUACUCAUUCGUUUCGGAAGAGACAGGUACGUUAAUAGUUAAUAGCGUACUUCUUUUUCUUGCUUUCGUGGUAUUCUUGCUAGUUACACUAGCCAUCCUUACUGCGCUUCGAUUGUGUGCGUACUGCUGCAAUAUUGUUAACGUGAGUCUUGUAAAACCUUCUUUUUACGUUUACUCUCGUGUUAAAAAAUCUGAUU"

print("=========================================================")
print("🔬 COMPUTATIONAL BIOLOGY LAB - VIRAL GENOME DASHBOARD 🔬")
print("=========================================================\n")
print(f"Target Organism: SARS-CoV-2 (COVID-19 Pandemic Strain)")
print(f"Analyzed Genome Segment: {covid19_rna_sequence[:50]}...\n")

# 1. Total Length of the Analyzed Corona Virus Fragment
total_nucleotides = len(covid19_rna_sequence)
print(f"[STATUS] Total Nucleotide Chain Length: {total_nucleotides} Ribonucleic Bases")

# 2. Individual Base Frequency Analysis (How the virus is structured)
adenine_count = covid19_rna_sequence.count('A')
uracil_count = covid19_rna_sequence.count('U')
guanine_count = covid19_rna_sequence.count('G')
cytosine_count = covid19_rna_sequence.count('C')

print(f"\n🧬 Nucleotide Composition Summary:")
print(f"   - Adenine (A): {adenine_count} bases")
print(f"   - Uracil (U) : {uracil_count} bases (Replaces Thymine in Viral RNA)")
print(f"   - Guanine (G): {guanine_count} bases")
print(f"   - Cytosine (C): {cytosine_count} bases")

# 3. Viral Genome Stability Index (AU/GC Ratio)
gc_total = guanine_count + cytosine_count
gc_percentage = (gc_total / total_nucleotides) * 100
print(f"\n⚡ Genomic Stability Index:")
print(f"   - Total GC Content: {gc_percentage:.2f}%")
print(f"   - Total AU Content: {(100 - gc_percentage):.2f}%")

# 4. Scanning for Potential Clinical Start Codons (AUG - Where virus translation begins)
start_codons_found = covid19_rna_sequence.count("AUG")
print(f"\n🔍 Clinical Mutation Screening:")
print(f"   - Active Start Codons (AUG) Detected: {start_codons_found}")
if start_codons_found > 0:
    print("   - [ALERT] Potential active translation sites identified for protein manufacturing.")

print("\n=========================================================")
print("Analysis Complete. Dataset prepared for Russian Scholarship Review Portfolio.")
print("=========================================================")
