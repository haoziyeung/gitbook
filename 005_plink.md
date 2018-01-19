**ped文件格式:**

PED文件主要是储存每个样本的基因型的，每行代表一个样本，前6列分别为：

\|headers\|tails\|  
FamilyID

| headers | tails |
| :--- | :--- |
| FamilyID |  |

\|----\|----\|

\|\|  
如果是自然群体，那就把family ID和individual ID都填一样的就行了。父母的ID就填0，代表缺失。

\|IndividualID\|\|

\|PaternalID\|\|

\|MaternalID\|\|

\|Sex\(1=male;2=female;other=unknown\)\|\|

\|Phenotype\|\|

从第7列开始，Phenotype（基因型，A，C，G，T）。

\`\`\`

FAM001  1  0 0  1  2  A A  G G  A C

FAM001  2  0 0  1  2  A A  A G  0 0

\`\`\`

\*\*MAP文件：\*\*

MAP文件主要是用来记录每个maker（一般为SNP）的位置信息。

每行一个maker，每列的含义如下：

\|\|\|

\|----\|----\|

\|Chromosome \(1-22, X, Y or 0 if unplaced\)\|\|

\|rs\(or Variant identifier\)\|\|

\|Genetic distance \(morgans\)\|摩尔根距离\|

\|Base-pair position \(bp units\)\|\|

\*\*FAM文件：\*\*

FAM文件没有header，每行一个样本，六列信息，分别是：

\|\|\|

\|----\|----\|

\|Family ID \('FID'\)\|

\|Within-family ID \('IID'; cannot be '0'\)

\|Within-family ID of father \('0' if father isn't in dataset\)\|

\|Within-family ID of mother \('0' if mother isn't in dataset\)\|

\|Sex code \('1' = male, '2' = female, '0' = unknown\)\|

\|Phenotype value \('1' = control, '2' = case, '-9'/'0'/non-numeric = missing data if case/control\)\|

\#\# 3. 基于全基因组snp数据如何进行主成分分析（PCA）

\#\#\# 3.1. 利用vcftools软件进行格式转换：

\`\`\`

vcftools --vcf tmp.vcf --plink --out tmp

\#\#--remove-filtered-all

\`\`\`

\`\`\`

\[options\]

--remove-filtered-all: Removes all sites with a FILTER flag other than PASS.

\`\`\`

生成两个文件：tmp.ped 和 tmp.map

\#\#\# 3.2. 利用plink软件进行数据格式转换\(version: plink-1.07\)：

\`\`\`

./plink --noweb --file tmp --make-bed --out tmp

\#--geno 0.1 --maf 0.01 --hwe 0.000001 --recode

\`\`\`

生成三个文件：tmp.bed，tmp.bim 和 tmp.fam

\#\#\# 3.3. 利用gcta软件进行pca构建

\#\#\#\# Ref\_Info

[http://www.bioask.net/question/238](http://www.bioask.net/question/238)

