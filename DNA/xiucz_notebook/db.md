 refGene,
 ensGene,
 avsnp142,
 avsnp144,
 snp138NonFlagged,
 kaviar_20150923,
 popfreq_all_20150413,
 nci60,
 ljb26_all,
 cosmic70,
 clinvar_20160302,
 gwascatalog,
 phastConsElements46way,
 genomicSuperDups,
 tfbs,
 wgRna,
 targetScanS

Kaviar 
http://db.systemsbiology.net/kaviar/

ExAC(Exome Aggregation Consortium)
http://exac.broadinstitute.org/
NHLBI-ESP
https://esp.gs.washington.edu/drupal/

**annovar docment**
http://annovar.openbioinformatics.org/en/latest/
```
Chrom  Pos Ref Alts    Alt GT_51L  GT_51N  DP_51L  Nref_51L    Nalt_51L    GQ_51L  DP_51N  Nref_51N    Nalt_51N    GQ_51N  Filter  Qual    AF  Func.refGene    Gene.refGene    GeneDetail.refGene  ExonicFunc.refGene  AAChange.refGene    Gene.ensGene    GeneDetail.ensGene  AAChange.ensGene    Kaviar_AF   PopFreqMax  1000G_ALL   1000G_EAS   1000G_SAS   ExAC_ALL    ExAC_EAS    ExAC_SAS    ESP6500siv2_ALL ESP6500siv2_AA  ESP6500siv2_EA  CG46    nci60   avsnp142    snp138NonFlagged    cosmic70    CLINSIG CLNDBN  CLNACC  CLNDSDB CLNDSDBID   omim_id omim_des    gwascatalog SIFT_score  SIFT_pred   Polyphen2_HDIV_score    Polyphen2_HDIV_pred Polyphen2_HVAR_score    Polyphen2_HVAR_pred LRT_score   LRT_pred    MutationTaster_score    MutationTaster_pred MutationAssessor_score  MutationAssessor_pred   FATHMM_score    FATHMM_pred CADD_raw    CADD_phred  GERP++_RS   phyloP46way_placental   phyloP100way_vertebrate SiPhy_29way_logOdds phastConsElements46way  genomicSuperDups    tfbs    wgRna   targetScanS
```

# OMIM
https://www.omim.org/help/api


# Clinvar
```bash
wget -c ftp://ftp.ncbi.nlm.nih.gov/pub/clinvar/vcf_GRCh37/clinvar_20171029.vcf.gz
```
# GENCODE
http://www.gencodegenes.org/stats.html
I recommend to download gh38 fasta and gff3 files from GENCODE. These 2 files would be the main fasta and gff3 files for most users.
```
http://www.gencodegenes.org/releases/
==>
wget ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_23/GRCh38.primary_assembly.genome.fa.gz

wget ftp://ftp.sanger.ac.uk/pub/gencode/Gencode_human/release_23/gencode.v23.basic.annotation.gff3.gz
```

# Ensembl(recommend)
I recommend to download gh38 sequence functional annotations from Ensembl: 
```
www.ensembl.org/info/data/ftp/index.html
==>
ftp://ftp.ensembl.org/pub/
==>
ftp://ftp.ensembl.org/pub/release-90/genbank/homo_sapiens/
```

# GATK
```
https://software.broadinstitute.org/gatk/download/bundle
==>
ftp://gsapubftp-anonymous@ftp.broadinstitute.org/bundle/
==>
ftp://ftp.broadinstitute.org/bundle/hg19/
```