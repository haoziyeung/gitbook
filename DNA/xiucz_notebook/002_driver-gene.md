## 2. MutSigCV

| header | tails | tails2 |
| :--- | :--- | :--- |
| slient mutation | 沉默突变 | 突变不改变表型，发生在外显子或内含子区域 |
| nonslient mutation | 非沉默突变 | 改变蛋白质序列或剪切位点，并影响表型改 |
| synonymous mutation | 同义突变 | 突变不改变氨基酸序列，只发生在外显子区域 |
| missense mutation | 错义突变 | 改变密码子并导致氨基酸改变 |
| nonsense mutation | 无义突变 | 将密码子突变成终止密码子，导致多肽序列提前终止 |

**CGA:**  
[http://archive.broadinstitute.org/cancer/cga/mutsig](http://archive.broadinstitute.org/cancer/cga/mutsig)  
**MutSig:**  
[https://hpc.nih.gov/apps/MutSig.html](https://hpc.nih.gov/apps/MutSig.html)  
**MutSigCV:**  
[http://software.broadinstitute.org/cancer/software/genepattern/modules/docs/mutsigcv](http://software.broadinstitute.org/cancer/software/genepattern/modules/docs/mutsigcv)

![](/assets/mutsig_fig1.PNG)  
左边是一组基因组（或外显子组），每一组来自对不同癌症患者的肿瘤细胞进行测序。基因表示为彩色条带，体细胞突变表示为红色三角形。首先，将肿瘤聚集在一起并记录突变，然后计算每个基因的得分和p值。选择显着性阈值来控制假发现率（FDR），超过这个阈值的基因被报告显着变异。

**NOTES:**

##### note1:

MutSig was originally developed for analyzing somatic mutations, but it has also been useful in analyzing germline mutations. MutSig最初是为分析体细胞突变而开发的，但它也可用于分析种系突变。

##### note2:

版本更新：  
MutSig1.0 --&gt; MutSig1.5 --&gt; MutSig2.0;  
MutSigS2N --&gt; MutSigCV

### 2.1. 下载 & 安装

[http://archive.broadinstitute.org/cancer/cga/mutsig\_download](http://archive.broadinstitute.org/cancer/cga/mutsig_download)

#### Ref\_Info

MCR安装: [http://youzicha1231.lofter.com/post/1e273e34\_cfd7bb2](http://youzicha1231.lofter.com/post/1e273e34_cfd7bb2)
http://www.cnblogs.com/qiniqnyang/p/5561104.html
http://www.cnblogs.com/qiniqnyang/p/5560913.html

### 2.1.1. 输入文件

**Note: **gene and sample names must agree across these three files. Similarly, the categ numbers must agree between the mutation and coverage files.

* MAF mutation file
* Coverage file
* Covariates file
* Mutation type dictionary
* Genome build

### 2.1.2. MAF file

The MAF file to be used in MutSigCV must have 2 additional, nonstandard columns: effect and categ.  MutSigCV requires only 4 columns of the MAF file \(see this page for the full MAF specification\) and can process a simple tab-delimited file with only these columns if a full MAF is not available.  
要在MutSigCV中使用的MAF文件必须有2个额外的非标准列：效果和类别。MutSigCV仅需要MAF文件的4列，并且如果完整的MAF不可用，则可以仅使用这些列来处理简单的制表符分隔的文件。

| header | tails |
| :--- | :--- |
| gene | 突变基因名称\(Hugo Symbol\) |
| patient | 突变样本名称\(Tumor Sample Barcode\) |
| effect | 突变对基因产生的影响， 这个信息可以从标准的Variant\_Classification MAF列导出。”nonsilent”（改变蛋白质序列或剪切位点）；”silent”（沉默突变，发生在外显子或内含子区域，在外显子区域时一般为同义突变，不改变mRNA翻译结果）；”noncoding”（突变发生在内含子或非编码区）；”flank”（无） |
| categ | 突变类别，该列可以从标准MAF文件Variant\_Classification，Reference\_Allele和Tumor\_Seq\_Allele1中的三个列以及其他基因组信息以及用于识别CpG上下文和无效突变的基因组信息中导出。每个突变只属于一个类别。 |

**effect:**

**categ:**  
1. CpG transitions  
2. CpG transversions  
3. C:G transitions  
4. C:G transversions  
5. A:T transitions  
6. A:T transversions  
7. null+indel mutations, 包括无义突变（Nonsense\_Mutation、Nonstop\_Mutation）、剪切位点（splicing\_Site）、插入缺失（Frame\_Shift\_Del、Frame\_Shift\_Ins、In\_Frame\_Del、In\_Frame\_Ins）、翻译起始位置（Translation\_Start\_Site）。

### 2.1.3. Coverage file

该文件包含有关每个基因和患者/肿瘤的测序覆盖率信息。

| header | tails |
| :--- | :--- |
| gene | 对应于MAF文件的Hugo\_Symbol |
| effect\(zone\) |  |
| categ | 必须与突变表中的类别匹配 |
| &lt;patient\_name\_1&gt; | 受该基因突变影响的患者1在该位点发生突变的base数，等同于alt的深度。 |
| ... |  |

Note, covered bases will typically contribute fractionally to more than one effect depending on the consequences of mutating to each of three different possible alternate bases.被覆盖的碱基通常会贡献一个以上的效果，具体取决于三种不同的可能替代碱基的变异后果。

### 2.1.4. Covariate file

| header | tail |
| :--- | :--- |
| gene |  |
| expr |  |
| reptime | 该基因的DNA复制时间（在HeLa细胞中测量），范围从100（非常早）到1000（非常晚） |
| hic | HiC统计量，是开放与封闭染色质状态的量度。该基因的染色质状态（从K562细胞中的HiC实验测量）范围约为-50（非常封闭）至+50（非常开放）。 |

### 2.2. run

[http://archive.broadinstitute.org/cancer/cga/mutsig\_run](http://archive.broadinstitute.org/cancer/cga/mutsig_run)

```
## exmaple data
http://www.broadinstitute.org/cancer/cga/sites/default/files/data/tools/mutsig/LUSC.MutSigCV.input.data.v1.0.zip

## run1
bash run_MutSigCV.sh <LUSC.maf> <LUSC.coverage.txt> <gene.covariates.txt> <LUSC.output.txt>

## run2
run_MutSigCV.sh <path_to_MCR> <my_mutations.maf> <exome_full192.coverage.txt gene.covariates.txt> <my_results> <mutation_type_dictionary_file.txt> <chr_files_hg19>
```

### 2.3. 输出文件
```
LUSC.output.txt.categs.txt    
LUSC.output.txt.mutations.txt
LUSC.output.txt.coverage.txt 
LUSC.output.txt.sig_genes.txt
```

LUSC.output.txt.sig_genes.txt输出分析中的“nnei”，“x”和“X”值可以深入了解给定基因如何计算背景突变率。  
nnei给出相邻基因的数量，这些基因汇集在一起​​计算该基因的背景突变率; 这些基因不一定在基因组上相邻，而是它们具有相近的协变量值；  
x给出这些相邻基因中的突变碱基的数目，这些基因是沉默的或非编码的；  
而X给出与这些相邻基因相关的碱基的总数。

### 2.4. Q&A
#### 2.4.1 制作MAF文件
利用python模块vcf2maf；
利用oncotator将mutect2生成的vcf文件转成maf.txt文件再进一步处理；
```
python3 get_vcf_to_tsv.py mutect2.vcf > mutect2.tsv
## 利用官网转化
python3 get_maf.py mutect2.txt > mutect2.maf
```
