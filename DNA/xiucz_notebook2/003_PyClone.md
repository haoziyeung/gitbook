Abstract  
We introduce a novel statistical method, PyClone, for inference of clonal population structures in cancers. PyClone is a Bayesian clustering method for grouping sets of deeply sequenced somatic mutations into putative clonal clusters while estimating their cellular prevalences and accounting for allelic imbalances introduced by segmental copy number changes and normal cell contamination. Single cell sequencing validation demonstrates that PyClone infers accurate clustering of mutations that co-occur in individual cells.  
摘要：我们引入了一种新的统计方法，PyClone，用于推断癌症中的克隆群体结构。PyClone是一种贝叶斯聚类方法，用于将一系列深度测序的体细胞突变分组为假定的克隆聚类，同时估计其细胞发生率并考虑由节段拷贝数变化和正常细胞污染引入的等位基因不平衡。单细胞测序验证表明，PyClone推断出在单细胞中共同发生的突变的准确聚类。

## 1. 下载&安装 \[v0.12.3\]
https://github.com/aroth85/pyclone

[https://bitbucket.org/aroth85/pyclone/wiki/Installation](https://bitbucket.org/aroth85/pyclone/wiki/Installation)

```
conda create --name pyclone python=2 #conda3
source activate pyclone
conda install pyclone -c aroth85
source deactivate
```

## 2. Data

## 2.1. Input data

| header | tails |
| :---: | :--- |
| mutation\_id | 唯一 |
| ref\_counts |  |
| var\_counts |  |
| normal\_cn | 样本中正常细胞的突变基因座的拷贝数，大多数情况下是2， |
| minor\_cn | 肿瘤样本预测的次要亲本拷贝数 |
| major\_cn | 肿瘤样本预测的主要亲本拷贝数 |

**NOTES:**

##### note1:

如果样本来自男性，突变位于性染色体（X或Y）上，则正常细胞的拷贝数为1；

如果正常组织具有种系拷贝数变异，则需要将拷贝数设置为预测值。得到这个的唯一方法是对来自同一供体的正常组织进行拷贝数分析。

##### note2:

我们通常不能说出什么样的等位基因是母本或父本，所以我们使用次要和主要的拷贝数。一般，主要拷贝数是两个值中较大的一个。

如果只有肿瘤的总拷贝数，而不是父母拷贝数，则可以将minor\_cn设置为0，将major\_cn设置为预测的总拷贝数。当使用PyClone build\_mutations\_filefile命令时，需要--var\_prior total\_copy\_number在这种情况下设置标志。默认情况下，该命令假定父母拷贝信息通过了。

##### note3:

除了上述6列必须的信息，还可以添加其他额外的列。但它们仅用于您自己的注释。除了上面提到的6个必填字段以外的任何字段都将被PyClone忽略：

* variant\_case：包含该突变的变异基因型的病例的1000个基因组ID。
* variant\_freq：显示变体等位基因的读数部分。
* genotype：具有变体的病例的基因型。

## 2.2. example data

```
tar -zxvf tutorial.tar.gz && cd tutorial && ls

config.yaml
tsv/
```

### 2.2.1 yaml格式的配置文件

参考tutotial data中的config.yaml:


| p | tails |
| :--- | :--- |
| num\_iters | PyClone将执行的MCMC迭代次数。更多的迭代将导致更精确的后验分布估计，代价是更多的计算量。 |
| base\_measure\_params | 克隆频率的基本度量的先验分布。默认值均匀分布在\[0，1\]上，默认。 |
| concentration | Dirichlet过程（DP）中浓度参数的初始值和先验值，默认。 |

  
模型：

| model | tails |
| :--- | :--- |
| gaussian |  |
| binomial |  |
| beta\_binomial |  |
| pyclone\_binomial |  |
| pyclone\_beta\_binomial |  |

**NOTES:**
##### note1:
在yaml配置文件中，working_dir指定一个工作目录，其他的目录都是相对于该目录的，否则使用全路径。

## 2.3. run
### 2.3.1. 
将tsv文件转换成PyClone可以使用的yaml格式

```
mkdir yaml/

PyClone build_mutations_file \
--in_file tsv/SRR385938.tsv 
--out_file yaml/SRR385938.yaml

PyClone build_mutations_file \
--in_file tsv/SRR385939.tsv \
--out_file yaml/SRR385939.yaml

PyClone build_mutations_file \
--in_file tsv/SRR385940.tsv \
--out_file yaml/SRR385940.yaml

PyClone build_mutations_file \
--in_file tsv/SRR385941.tsv \
--out_file yaml/SRR385941.yaml
```

```
head tsv/SRR385938.tsv
mutation_id    ref_counts    var_counts    normal_cn    minor_cn    major_cn    variant_case  variant_freq    genotype
NA12156:BB:chr2:175263063    3812    14    2    0    2    NA12156    0.0036591740721380033    BB

head yaml/SRR385938.yaml 

mutations:
- id: NA12156:BB:chr2:175263063
  ref_counts: 3812
  states:
  - {g_n: AA, g_r: AA, g_v: AB, prior_weight: 1}
  - {g_n: AA, g_r: AA, g_v: BB, prior_weight: 1}
  var_counts: 14
```

**NOTES:**
##### note1:
ref\_counts: 3812:   指定突变的参考数量  
var\_counts: 14:     指定突变的变异计数。

##### note2:

**g\_n:**正常亚群中细胞的基因型;

**g\_r:** 参考子群体中细胞的基因型;  
回顾参考亚群由缺乏突变的所有癌细胞组成。因此，这里有效的基因型不应含有B等位基因。例如A，AA，AAA，AAAAAAAA都是有效的，但是B，AB，BB，AAAAB是无效的。

**g\_v:**变体亚群中细胞的基因型;  
回顾变体亚群由具有突变的所有癌细胞组成。因此，有效的基因型应该包含至少一个 B等位基因。例如B，AB，BB，ABBB都是有效的，但是A，AA，AAB是无效的。

**prior:**

### 2.3.2.
```
PyClone run_analysis --config_file final_config.yaml
```

```
ls trace/

alpha.tsv.bz2
labels.tsv.bz2 
precision.tsv.bz2        
SRR385938.cellular_prevalence.tsv.bz2  SRR385941.cellular_prevalence.tsv.bz2
SRR385939.cellular_prevalence.tsv.bz2
SRR385940.cellular_prevalence.tsv.bz2
```

### 2.3.3. 聚类
(不可用)
### 2.3.4. 绘制相似矩阵
(不可用)
### 2.3.5. 绘制多样本平行坐标
(不可用)
### 
```
PyClone plot_clusters --config_file final_config.yaml --burnin 1000 --plot_file cluster_plots --plot_type scatter
```
选项--burnin 1000, 告诉命令放弃MCMC追踪的前1000个样本作为刻录，推断将基于剩余的9000个样本。所有后续的后处理命令将使用相同的标志。


