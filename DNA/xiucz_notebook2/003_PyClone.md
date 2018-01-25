Abstract  
We introduce a novel statistical method, PyClone, for inference of clonal population structures in cancers. PyClone is a Bayesian clustering method for grouping sets of deeply sequenced somatic mutations into putative clonal clusters while estimating their cellular prevalences and accounting for allelic imbalances introduced by segmental copy number changes and normal cell contamination. Single cell sequencing validation demonstrates that PyClone infers accurate clustering of mutations that co-occur in individual cells.  
摘要：我们引入了一种新的统计方法，PyClone，用于推断癌症中的克隆群体结构。PyClone是一种贝叶斯聚类方法，用于将一系列深度测序的体细胞突变分组为假定的克隆聚类，同时估计其细胞发生率并考虑由节段拷贝数变化和正常细胞污染引入的等位基因不平衡。单细胞测序验证表明，PyClone推断出在单细胞中共同发生的突变的准确聚类。

## 2.1. 下载&安装
https://bitbucket.org/aroth85/pyclone/wiki/Installation

```
conda create --name pyclone python=2
```

## 2.2. Input data

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

如果只有肿瘤的总拷贝数，而不是父母拷贝数，则可以将minor_cn设置为0，将major_cn设置为预测的总拷贝数。当使用PyClone build_mutations_filefile命令时，需要--var_prior total_copy_number在这种情况下设置标志。默认情况下，该命令假定父母拷贝信息通过了。
##### note3:
除了上述6列必须的信息，还可以添加其他额外的列。但它们仅用于您自己的注释。除了上面提到的6个必填字段以外的任何字段都将被PyClone忽略：

+ variant_case：包含该突变的变异基因型的病例的1000个基因组ID。
+ variant_freq：显示变体等位基因的读数部分。
+ genotype：具有变体的病例的基因型。

