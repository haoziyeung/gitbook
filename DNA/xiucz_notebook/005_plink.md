---
description: This is a short description of my page
---

**ped文件格式:**

PED文件主要是储存每个样本的基因型的，每行代表一个样本，前6列分别为：

| headers | tails |
| :--- | :--- |
| FamilyID | 如果是自然群体，那就把family ID和individual ID都填一样的就行了。父母的ID就填0，代表缺失。 |
| IndividualID |  |
| PaternalID |  |
| MaternalID |  |
| Sex\(1=male;2=female;other=unknown\) |  |
| Phenotype |  |

从第7列开始，Phenotype（基因型，A，C，G，T）。

```
FAM001  1  0 0  1  2  A A  G G  A C
FAM001  2  0 0  1  2  A A  A G  0 0
```

**MAP文件:**

MAP文件主要是用来记录每个maker（一般为SNP）的位置信息。

每行一个maker，每列的含义如下：

| header | tails |
| :--- | :--- |
| Chromosome \(1-22, X, Y or 0 if unplaced\) |  |
| rs\(or Variant identifier\) |  |
| Genetic distance \(morgans\) | 摩尔根距离 |
| Base-pair position \(bp units\) |  |

**FAM文件:**

FAM文件没有header，每行一个样本，六列信息，分别是：

\| header\| tails\|

\| ---- \| ---- \|

\|Family ID \('FID'\)\|\|

\|Within-family ID \('IID'; cannot be '0'\)

\|Within-family ID of father \('0' if father isn't in dataset\)\|

\|Within-family ID of mother \('0' if mother isn't in dataset\)\|

\|Sex code \('1' = male, '2' = female, '0' = unknown\)\|

\|Phenotype value \('1' = control, '2' = case, '-9'/'0'/non-numeric = missing data if case/control\)\|\|

---

## 3. 基于全基因组snp数据如何进行主成分分析（PCA）

### 3.1. 利用vcftools软件进行格式转换：

```
vcftools --vcf tmp.vcf --plink --out tmp

##--remove-filtered-all
```

```
[options]

--remove-filtered-all: Removes all sites with a FILTER flag other than PASS.
```

生成两个文件：tmp.ped 和 tmp.map

### 3.2. 利用plink软件进行数据格式转换\(version: plink-1.07\)：

```
./plink --noweb --file tmp --make-bed --out tmp
#--geno 0.1 --maf 0.01 --hwe 0.000001 --recode
```

生成三个文件：tmp.bed，tmp.bim 和 tmp.fam

### 3.3. 利用gcta软件进行pca构建

#### Ref\_Info

[http://www.bioask.net/question/238](http://www.bioask.net/question/238)

---

## 4. PLINK1.07

官方网站：[http://www.cog-genomics.org/plink2/](http://www.cog-genomics.org/plink2/)

参考网站：[http://zzz.bwh.harvard.edu/plink/](http://zzz.bwh.harvard.edu/plink/)

tutorial：[http://zzz.bwh.harvard.edu/plink/tutorial.shtml](http://zzz.bwh.harvard.edu/plink/tutorial.shtml)

### 4.1. 89 HapMap samples and 80K random SNPs

#### 4.1.1. Start

```bash
unzip  hapmap1.zip

hapmap1.map
hapmap1.ped
pop.phe
qt.ph
```

```
plink --file hapmap1
```

**NOTES:**

##### note1:

可以使用**--ped**和**--map**选项来指定其他路径的PED和MAP文件，而使用**--file**选项时,  这两个文件必须有相同的前缀, 并以**.map**，**.ped**结尾。

##### note2:

PED and MAP files are plain text files; PED files contain genotype information \(one person per row\) and MAP files contain information on the name and position of the markers in the PED file. If you are not familiar with the file formats required for PED and MAP files, please consult this [page](http://zzz.bwh.harvard.edu/plink/data.shtml).  
PED和MAP文件是纯文本文件; PED文件包含基因型信息（每行一个样本），MAP文件包含PED文件中标记名称和位置的信息。

##### note3:

_plink.log_，输出文件的名称可以使用_--out_选项来更改；如果我们没有指定 _--out_选项，则根输出文件名默认为_“plink”_。

得到的结果和教程里不一样。。。。

#### 4.1.2 制作二进制ped文件

```
plink --file hapmap1 --make-bed --out hapmap

hapmap.bed
hapmap.bim
hapmap.fam
```

**NOTES:**

##### note1:

使用_--make-bed_选项时，缺失率和等位基因频率的阈值过滤器被自动设置为排除任何人。

#### 4.1.3. 使用二进制ped文件

```
plink --bfile hapmap
```

#### 4.1.4. 汇总统计：缺失率

```
plink --bfile hapmap --missing --out miss_stat

miss_stat.imiss
miss_stat.lmiss
miss_stat.log
```

**NOTES:**

##### note1:

在miss\_stat.imiss文件中；  
在miss\_stat.imiss文件中，最后一列是该个体的实际基因分型率。

#### 4.1.5. 汇总统计：等位基因频率

```
plink --bfile hapmap --freq --out freq_stat

freq_stat.frq
freq_stat.log
```

**NOTES:**

##### note1:

生成一个名为freq\_stat.frq的文件，其中包含每个SNP的次要等位基因频率和等位基因编码。

通过分类聚类变量进行分层分析（和缺失分析）:

```
plink --bfile hapmap --freq --out freq_stat --within pop.phe

freq_stat.frq.strat
```

每个SNP都被表示了两次：CLST 列表示频率是来自中国人还是日本人，按照pop.phe文件进行编码。

**NOTES:**

##### note1:

每一行为亚群分层的每个SNP的等位基因频率；

#### 4.1.6. 基因关联分析（Basic association analysis）

```
plink --bfile hapmap --assoc --out as

as.assoc
as.log
```

每一列表示：

|  |  |
| :--- | :--- |
| Chromosome | 染色体 |
| SNP identifier | SNP标识符 |
| Code for allele 1 \(the minor, rare allele based on the entire sample frequencies\) | 等位基因1的编码（基于整个样本频率的次要，稀有等位基因） |
| The frequency of this variant in cases |  |
| The frequency of this variant in controls |  |
| Code for the other alleleCode for the other allele |  |
| The chi-squared statistic for this test \(1 df\) |  |
| The asymptotic significance value for this test |  |
| The odds ratio for this test |  |

对关联统计列表进行排序:
```
sort --key=8 -nr as.assoc|head

  13   rs9585021      64274    1    0.625   0.2841    2        20.62    5.586e-06       
   2   rs2222162      10602    1   0.2841   0.6222    2        20.51    5.918e-06       
   9  rs10810856      46335    1   0.2955  0.04444    2        20.01    7.723e-06    

```

----

## 5. PLINK1.90



