import sys, re
infile = sys.argv[1] # XJX2_vs_XJX.mutect2.vcf
sample = sys.argv[2]

with open(infile, 'r') as f:
	for line in f:
      		lines = line.rstrip()
        	cols = lines.split("\t")
		if line.startswith("#"):
			pass
        	else:
			chr = cols[0]
			start = cols[1]
			ref = cols[3]
			alt = cols[4]
			filter = cols[6]
			if filter == 'PASS':
				if len(ref) == len(alt):
					end = start
				if len(ref) > len(alt):
					start = str(int(start)+1)
					ref = ref[1:]
					alt = '-'
					end = str(int(start)+len(ref)-1)
				if len(ref) < len(alt):
					start = str(int(start)+1)
					ref = '-'
					alt = alt[1:]
					end = str(int(start)+len(alt)-1)
				ss = [chr,start,end,ref,alt,sample]
				print "\t".join(ss)
