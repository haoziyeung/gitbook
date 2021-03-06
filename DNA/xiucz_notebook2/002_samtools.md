

### sam文件格式sam格式的定义：
https://samtools.github.io/hts-specs/SAMv1.pdf
http://broadinstitute.github.io/picard/explain-flags.html
 1. 第3和第7列，可以用来判断某条reads是否比对成功到了基因组的染色体，左右两条reads是否比对到同一条染色体。
 而第1，10，11列可以提取出来还原成我们的测序数据fastq格式的。  
 2. 第2列是二进制转换成十进制后的和。   
 3. 第5列，比对结果的质量值，也是因工具而异。  
 4. 第6列CIGAR是比较重要的，解释如下，其中M并不是说match，所以我们的PE 150的reads，大部分都会是150M，但是并不代表着跟参考序列一模一样。其中S/H是比较特殊的，很难讲清楚，但是大部分情况下用不到。
 （soft-clipping碱基是指一条reads未匹配上当前基因组位置的部分，如果有多个reads在这种情况并且这些reads的soft-clipping碱基都能够比对在基因组另一位置，那么就可能存在SV）   
 5. RG代表着你的sam文件比对来自于哪个样本的fastq程序结果。NM这个tag是编辑距离，大概就是你的reads如果想转变成参考基因组，需要改变多少个碱基，如果编辑距离是0才说明你的这个150bp长度的序列跟参考基因组一模一样。
 6. 从整体来看，一个bam文件的行数是约等于reads数的，但考虑到少数reads可能比对多基因组上多个位置，所以行数一般是略大于reads数。
 

## samtools
#### 对fasta文件建立索引
```
samtools faidx ref_genome.fasta

提取子序列
samtools faidx ref_genome.fasta scffold_10 > scaffold_10.fasta
```
#### sam文件<=>bam文件
```bash
samtools view -h sample.bam > sample.sam samtools view -bS sample.sam > sample.bam
```
#### view
```
0x1 PAIRED paired-end (or multiple-segment) sequencing technology 
0x2 PROPER_PAIR each segment properly aligned according to the aligner 
0x4 UNMAP segment unmapped 0x8 MUNMAP next segment in the template unmapped 
0x10 REVERSE SEQ is reverse complemented 
0x20 MREVERSE SEQ of the next segment in the template is reverse complemented 
0x40 READ1 the first segment in the template 
0x80 READ2 the last segment in the template 
0x100 SECONDARY secondary alignment 
0x200 QCFAIL not passing quality controls 
0x400 DUP PCR or optical duplicate 
0x800 SUPPLEMENTARY supplementary alignment
```

```bash
1)提取没有比对到参考序列上的比对结果
samtools view -bf 4 abc.bam > abc.f.bam

2)提取比对到参考序列上的比对结果
samtools view -bF 4 abc.bam > abc.F.bam 

3)提取paired reads中两条reads都比对到参考序列上的比对结果，只需要把两个4+8的值12作为过滤参数即可
samtools view -bF 12 abc.bam > abc.F12.bam

4)提取bam文件中比对到caffold1上的比对结果，并保存到sam文件格式
samtools view abc.bam scaffold1 > scaffold1.sam

5)提取scaffold1上能比对到30k到100k区域的比对结果
samtools view abc.bam scaffold1:30000-100000 $gt; scaffold1_30k-100k.sam

6)根据fasta文件，将 header 加入到 sam 或 bam 文件中
samtools view -T genome.fasta -h scaffold1.sam > scaffold1.h.sam

7)查看bwa比对结果中比对上基因组的unique mapped reads
samtools view xx.bam |grep "XT：A：U" | wc -l

8)samtools idxstats选项输出记录由tab分隔，其中第1列为参考序列ID(染色体号)，第二列为参考序列长度，第三列为mapped reads数，第四列为unmapped reads数

9)快速计算一个bam文件的reads数
samtools idxstats in.bam|awk "{s+=$3+$4}’END{print s}"

10)Subsample BAM file
samtools view -s 0.5 test.bam > test_hafl_random.bam

11)bam2fastq
bam2fastq工具链接：http://www.hudsonalpha.org/gsl/software/bam2fastq.php
```

```bash
想知道有多少paired end reads有mate并且都有map时，可以使用-f 1 -F 12来过滤
samtools view -c -f 1 -F 12 test.bam
其中-f 1指定只包含那些paired end reads，-F 12是不包含那些unmapped(flag 0×0004)以及mate是unmapped(flag 0×0008)。0×0004 + 0×0008 = 12.
```
测序数据的双端的，那么sam文件的第3列是reads1的比对情况，第6列是reads2的比对情况。所以未比对成功的测序数据可以分成3类，仅reads1，仅reads2，和两端reads都没有比对成功。
也可以用下面的代码分步提取这3类未比对成功的reads:
```
samtools view -u  -f 4 -F264 alignments.bam  > tmps1.bam
samtools view -u -f 8 -F 260 alignments.bam  > tmps2.bam
samtools view -u -f 12 -F 256 alignments.bam > tmps3.bam
samtools merge -u - tmps[123].bam | samtools sort -n - unmapped
bamToFastq -bam unmapped.bam -fq1 unmapped_reads1.fastq -fq2 unmapped_reads2.fastq
```
```bash
samtools view sample_sorted.bam chr1:1234-123456
samtools flagstat sample_sorted.bam
```

#### sort
```bash
samtools sort sample.bam sort_default
samtools sort -n sample.bam sort_left
```
Sort alignments by leftmost coordinates, or by read name when -n is used.  默认按照染色体位置进行排序，而-n参数则是根据read名进行排序。

#### flagstat
```
#Version: 1.3
samtools flagstat example.bam
14367369 + 0 in total (QC-passed reads + QC-failed reads)  #总共的reads数
26939 + 0 secondary
0 + 0 supplementary
0 + 0 duplicates
13229644 + 0 mapped (92.08% : N/A)  #总体上reads的匹配率
14340430 + 0 paired in sequencing  #有多少reads是属于paired reads
7170215 + 0 read1
7170215 + 0 read2
13005936 + 0 properly paired (90.69% : N/A) #完美匹配的reads数：比对到同一条参考序列，并且两条reads之间的距离符合设置的阈值
13109520 + 0 with itself and mate mapped  #paired reads中两条都比对到参考序列上的reads数
93185 + 0 singletons (0.65% : N/A)  #单独一条匹配到参考序列上的reads数，和上一个相加，则是总的匹配上的reads数。
0 + 0 with mate mapped to a different chr # #paired reads中两条分别比对到两条不同的参考序列的reads数
0 + 0 with mate mapped to a different chr (mapQ>=5)

```

```
#cat junti.bowtie.err
5421701 reads; of these:
  5421701 (100.00%) were paired; of these:
    705166 (13.01%) aligned concordantly 0 times
    4524924 (83.46%) aligned concordantly exactly 1 time
    191611 (3.53%) aligned concordantly >1 times
    ----
    705166 pairs aligned concordantly 0 times; of these:
      226261 (32.09%) aligned discordantly 1 time
    ----
    478905 pairs aligned 0 times concordantly or discordantly; of these:
      957810 mates make up the pairs; of these:
        644240 (67.26%) aligned 0 times
        8949 (0.93%) aligned exactly 1 time
        304621 (31.80%) aligned >1 times
94.06% overall alignment rate


A pair that aligns with the expected relative mate orientation and with the
expected range of distances between mates is said to align "concordantly". If
both mates have unique alignments, but the alignments do not match paired-end
expectations (i.e. the mates aren't in the expcted relative orientation, or
aren't within the expected disatance range, or both), the pair is said to align
"discordantly".

total reads: 5421701*2
mapping ratio: 1 - 644240*1/5421701*2 
```

```
[0] samtools flagstat plus01791.bam

[1] 33037592 + 0 in total (QC-passed reads + QC-failed reads)
[2] 0 + 0 secondary
[3] 0 + 0 supplementary
[4] 0 + 0 duplicates
[5] 31144385 + 0 mapped (94.27% : N/A)
[6] 33037592 + 0 paired in sequencing
[7] 16518796 + 0 read1
[8] 16518796 + 0 read2
[9] 25887744 + 0 properly paired (78.36% : N/A)
[10] 31089116 + 0 with itself and mate mapped
[11] 55269 + 0 singletons (0.17% : N/A)
[12] 0 + 0 with mate mapped to a different chr
[13] 0 + 0 with mate mapped to a different chr (mapQ>=5)
```
```
[14] 16518796 reads; of these:
[15]   16518796 (100.00%) were paired; of these:
[16]     3574924 (21.64%) aligned concordantly 0 times
[17]     11980802 (72.53%) aligned concordantly exactly 1 time
[18]     963070 (5.83%) aligned concordantly >1 times
    ----
[19]     3574924 pairs aligned concordantly 0 times; of these:
[20]       1747451 (48.88%) aligned discordantly 1 time
    ----
[21]     1827473 pairs aligned 0 times concordantly or discordantly; of these:
[22]       3654946 mates make up the pairs; of these:
[23]         1893207 (51.80%) aligned 0 times
[24]         57506 (1.57%) aligned exactly 1 time
[25]         1704233 (46.63%) aligned >1 times
[26] 94.27% overall alignment rate
```
```
[27] 'sample'        'total_reads'   'mapped_reads'  'pair_mapped_reads'     'single_mapped_reads'   'unique_mapped_reads'   'multi_mapped_reads'
[28] plus01791       33037592        31144385        29382646        1761739 27514012        1704233
```
**TIPS:**
[1]: 'total' is the total number of alignments (lines in the sam file), not total reads.'total' is the total number of alignments (lines in the [sam](http://samtools.sourceforge.net/SAM1.pdf) file), not total reads.
[9]:"Properly paired" means both mates of a read pair map to the same chromosome, oriented towards each other, and with a sensible insert size. 

#### Ref_Info
https://www.biostars.org/p/12475/

```
samtools view -@ 8 -bF 1024 过滤PCR扩增的接头序列
samtools view -bF 256    计算mappingratio的时候，因为是因为mem算法比对，需要先过滤打断比对的reads
samtools view -@ 8 -f 1 -F 12 提取paired mapped reads
```

## Concept

**1.** **Chimeric reads** occur when one sequencing read aligns to two distinct portions of the genome with little or no overlap. Chimeric reads are  indicative of structural variation. Chimeric reads are also called **split reads**.
**1.1.** After aligning with [bwa](http://bio-bwa.sourceforge.net/) mem, chimeric reads will have an SA  tag
**1.2.** Also note that chimeric reads are not the same as chimeric genes. In RNA-seq chimeric reads may indicate the presence of chimeric genes but for DNA-seq they often are evidence for structural variation without necessarily being evidence for chimeric gene/transcript events.
**1.3.** In RNA-seq chimeric reads may indicate the presence of circRNAs
```
samtools view my_alignment.bam | grep 'SA:' | less
```

**2.** **soft-clipped reads**
**3.** **hard clipping reads**
**5.** **Multiple mapping**
**6.** **representative**
**7.** **supplementary alignment**
**8.** **secondary alignment**
**9.** **inear alignment**

## Bwa Mem -M Option
```
-M         mark shorter split hits as secondary (for Picard/GATK compatibility)
```
without -M, a split read is flagged as 2048 ( supplementary alignment ) ;
with option -M it is flagged as a duplicate flag=256 ( not primary alignment ): will be ignored by most 'old' tools.

using option -M it says the read to be secondary alignment(not primary alignment) whereas without -M option it gives as supplementary alignment(2048).



#### Ref_Info
https://www.biostars.org/p/97323/
https://www.biostars.org/p/116201/

# QC软件
* Picard https://broadinstitute.github.io/picard/ 
* RSeQC http://rseqc.sourceforge.net/ 
* Qualimap http://qualimap.bioinfo.cipf.es/ 

#### Ref_Info
http://mp.weixin.qq.com/s/WG0KLWPCzTyKheUMRbJlfA

## TOdolist
https://bioinf.comav.upv.es/courses/sequence_analysis/mapping.html