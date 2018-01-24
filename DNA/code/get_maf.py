import sys, re
infile = sys.argv[1] # XJX2_vs_XJX.mutect2.vcf
sample = infile.split(".")[0]
a = 0
with open(infile, 'r') as f:
	for line in f:
      		lines = line.rstrip()
        	cols = lines.split("\t")
		if line.startswith("#"):
			pass
        	else:
			Hugo_Symbol = cols[0]
			Chromosome = cols[4]
			Start_position = cols[5]
			End_position = cols[6]
			Variant_Classification = cols[8]
			Variant_Type = cols[9]
			Reference_Allele = cols[10]
			Tumor_Seq_Allele1 = cols[11]
			Tumor_Seq_Allele2 = cols[12]
			Tumor_Sample_Barcode = sample
			if a == 0:
				Tumor_Sample_Barcode = 'Tumor_Sample_Barcode'
				a = 1
			Tumor_Seq_Allele1 = Tumor_Seq_Allele2
			ss = [Hugo_Symbol,Chromosome,Start_position,End_position,Variant_Classification,Variant_Type,Reference_Allele,Tumor_Seq_Allele1,Tumor_Seq_Allele2,Tumor_Sample_Barcode]
			print "\t".join(ss)
