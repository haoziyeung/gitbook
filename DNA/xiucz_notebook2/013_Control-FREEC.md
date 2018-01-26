http://www.novogene.com/tech/suppor/news/563.html

driver mutation

## 1. Introduction
 [http://boevalab.com/FREEC/tutorial.html#CONFIG](http://boevalab.com/FREEC/tutorial.html#CONFIG)

[http://boevalab.com/FREEC/](http://boevalab.com/FREEC/)
## 2. Download & Install
ftp://hgdownload.cse.ucsc.edu/goldenPath/hg19/chromosomes/

```
cat config_sample.txt
```

```
###For more options see: http://boevalab.com/FREEC/tutorial.html#CONFIG ###

[general]
chrLenFile = ~/FREEC-11.0/hg19.len
window = 0
ploidy = 2
outputDir = ./sample/

bedtools = ~/bedtools2-2.18.0/bin/bedtools
samtools = ~/samtools

#sex=XY
breakPointType=4
chrFiles = ~/FREEC-11.0/hg19/

maxThreads=6

breakPointThreshold=1.2
noisyData=TRUE
printNA=FALSE

readCountThreshold=50

[sample]

mateFile = sample_tumor.bam
inputFormat = bam
mateOrientation = FR

[control]

mateFile = sample_normal.bam
inputFormat = bam
mateOrientation = FR

[BAF]
makePileup = hg19_snp142.SingleDiNucl.1based.bed
fastaFile = hg19.fasta

SNPfile = hg19_snp142.SingleDiNucl.1based.txt
minimalCoveragePerPosition = 5

[target]

captureRegions = trim_S07604514_Regions.bed
```
### 2.1. Create Config file
## 3. run
```
~/FREEC-11.0/src//freec -conf config_sample.txt
```
```
cd ./sample/
ls

GC_profile.targetedRegions.cnp
sample_tumor.recalibrated.bam_BAF.txt
sample_tumor.recalibrated.bam_CNVs
sample_tumor.recalibrated.bam_info.txt
sample_tumor.recalibrated.bam_minipileup.pileup
sample_tumor.recalibrated.bam_ratio.txt
sample_tumor.recalibrated.bam_sample.cpn
sample_normal.recalibrated.bam_control.cpn
sample_normal.recalibrated.bam_minipileup.pileup
```

```
cat ~/FREEC-11.0/scripts/makeGraph.R | R --slave --args 2 sample_tumor.recalibrated.bam_ratio.txt sample_tumor.recalibrated.bam_BAF.txt
```

```
cat /data3/dna/dnapipe/script/freec/makeGraph.combine.R | R --slave --args 2 sample_tumor.recalibrated.bam_ratio.txt sample_tumor.recalibrated.bam_BAF.txt
```