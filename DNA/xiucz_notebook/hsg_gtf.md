```
wget -c ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_27/gencode.v27.annotation.gtf.gz
```
```bash
 zcat gencode.v27.annotation.gtf.gz | grep --color=auto -v "^#" | cut -f3 | sort | uniq -c | sort -k1rn
1200453 exon
 713073 CDS
 285630 UTR
 200401 transcript
  83727 start_codon
  75506 stop_codon
  58288 gene
    119 Selenocysteine
```
### exon
```bash
zcat gencode.v27.annotation.gtf.gz |
awk 'BEGIN{OFS="\t";} $3=="exon" {print $1,$4-1,$5}' |
sortBed | mergeBed -i -| gzip > gencode_v27_exon_merged.bed.gz
```
### subtract the exonic region from the genic region
how to avoid issues when merging the exons due to overlapping genes on each strand???
```bash
zcat gencode.v27.annotation.gtf.gz | 
awk 'BEGIN{OFS="\t";} $3=="gene" {print $1,$4-1,$5}' | 
sortBed | subtractBed -a stdin -b gencode_v27_exon_merged.bed.gz | gzip > gencode_v27_intron.bed.gz
```
### intergenic

### UTR
```
chr11   HAVANA  transcript      5225464 5227071 .       -       .       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  exon    5226930 5227071 .       -       .       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  CDS     5226930 5227021 .       -       0       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  start_codon     5227019 5227021 .       -       0       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  exon    5226577 5226799 .       -       .       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  CDS     5226577 5226799 .       -       1       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  exon    5225464 5225726 .       -       .       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  CDS     5225601 5225726 .       -       0       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  stop_codon      5225598 5225600 .       -       0       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  UTR     5227022 5227071 .       -       .       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4";
chr11   HAVANA  UTR     5225464 5225600 .       -       .       gene_id "ENSG00000244734.3"; transcript_id "ENST00000335295.4"; 
```
![](../pictures/bedtools.png)
## Reference_Info
https://davetang.org/muse/2013/01/18/defining-genomic-regions/