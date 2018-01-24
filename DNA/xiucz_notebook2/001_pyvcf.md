## pyvcf
```
>>> import vcf
>>> vcf_reader = vcf.Reader(filename=r'./input_data.vcf.gz')
```
调用vcf.Reader类处理vcf文件，vcf文件信息就被保存到vcf_reader中了。它是一个可迭代对象，它的迭代元素都是一个_Record**对象**的实例，保存着非注释行的一行信息，即变异位点的具体信息。

```
class vcf.model._Record(CHROM, POS, ID, REF, ALT, QUAL, FILTER, INFO, FORMAT, sample_indexes, samples=None)  
```

其中，_Record是vcf.model中的一个对象，除了它还有_Call，_AltRecord等对象。它的基本**属性**为CHROM，POS，ID，REF，ALT，QUAL，FILTER，INFO，FORMAT，也就是vcf中的一行位点信息:
CHROM：染色体名称，类型为str。
POS：位点在染色体上的位置，类型为int。
ID：一般是突变的rs号，类型为str。如果是‘.’，则为None。
REF：参考基因组在该位点上的碱基，类型为str。
ALT：在该位点的测序结果。是_AltRecord类的子类实例的列表。类型为list。AltRecord类有4个子类，代表了突变的几种类型：如snp，indel，structual variants等。所有的实例都可以进行比较（仅限于相等的比较，没有大于小于之说），部分子类没有实现str方法，也就是说不能转成字符串。返回的是一个列表  不管alt那列是几个碱基，都是返回列表，只有一个也是列表， 并列表中的元素不是字符串， 而是一个类：class 'vcf.model._Substitution'。 把元素转化为对应字符串用i.ALT[0].sequence
QUAL：该位点的测序质量，类型为int或float。
FILTER：过滤信息。将FILTER列按分号分隔形成的字符串列表，类型为list。如果未给出参数则为None。
INFO：该位点的一些测试指标。将‘=’前的参数作为键，后面的参数作为值，构建成的字典。类型为dict。
FORMAT：基因型信息。保存vcf的FORMAT列的原始形式，类型为str。


```
for record in vcf_reader:
    print(record)
    print(type(record))
    print(type(record.CHROM), record.CHROM)
    print(type(record.POS), record.POS)
    print(type(record.ID), record.ID)
    print(type(record.REF), record.REF)
    print(type(record.ALT), record.ALT)
    print(type(record.QUAL), record.QUAL)
    print(type(record.FILTER), record.FILTER)
    print(type(record.INFO), record.INFO)
    #print(type(record.INFO['BaseQRankSum']), record.INFO['BaseQRankSum'])
    print(type(record.FORMAT), record.FORMAT)

Record(CHROM=chr1, POS=13273, REF=G, ALT=[C])
<class 'vcf.model._Record'>
<class 'str'> chr1
<class 'int'> 13273
<class 'NoneType'> None
<class 'str'> G
<class 'list'> [C]
<class 'float'> 411.52
<class 'NoneType'> None
<class 'dict'> {'AC': [2], 'AF': [0.071], 'AN': 28, 'BaseQRankSum': 1.362, 'DP': 476, 'Dels': 0.0, 'ExcessHet': 3.1742, 'FS': 5.833, 'HaplotypeScore': 1.3209, 'InbreedingCoeff': -0.0881, 'MLEAC': [2], 'MLEAF': [0.071], 'MQ': 30.96, 'MQ0': 162, 'MQRankSum': 0.753, 'QD': 4.52, 'ReadPosRankSum': 0.283, 'SOR': 1.342}
<class 'str'> GT:AD:DP:GQ:PL  
```

```
for record in vcf_reader:
    print(record.samples)
    print(record.samples[0].sample)
    print(record.samples[0]['GT']) #按下标访问Call，按.sample访问sample，按键访问FORMAT对应信息  
    print(record.start, record.POS, record.end)
    print(record.REF, record.ALT, record.alleles) #注意G没有引号，它是_AltRecord对象

[Call(sample=F1, CallData(GT=0/0, AD=[51, 0], DP=52, GQ=81, PL=[0, 81, 1011])), Call(sample=F2, CallData(GT=0/0, AD=[30, 0], DP=30, GQ=51, PL=[0, 51, 678])), Call(sample=F3, CallData(GT=0/0, AD=[25, 0], DP=25, GQ=30, PL=[0, 30, 389])), Call(sample=F4, CallData(GT=0/0, AD=[45, 0], DP=45, GQ=75, PL=[0, 75, 902])), Call(sample=F5, CallData(GT=0/1, AD=[54, 12], DP=66, GQ=99, PL=[242, 0, 1022])), Call(sample=F6, CallData(GT=0/0, AD=[49, 0], DP=50, GQ=69, PL=[0, 69, 816])), Call(sample=F7, CallData(GT=0/0, AD=[13, 0], DP=13, GQ=6, PL=[0, 6, 57])), Call(sample=F8, CallData(GT=./., AD=None, DP=None, GQ=None, PL=None)), Call(sample=F9, CallData(GT=0/0, AD=[24, 0], DP=24, GQ=27, PL=[0, 27, 357])), Call(sample=F10, CallData(GT=0/0, AD=[13, 0], DP=13, GQ=15, PL=[0, 15, 177])), Call(sample=F11, CallData(GT=0/1, AD=[15, 10], DP=25, GQ=99, PL=[213, 0, 182])), Call(sample=F12, CallData(GT=0/0, AD=[56, 0], DP=56, GQ=78, PL=[0, 78, 1019])), Call(sample=F13, CallData(GT=0/0, AD=[23, 0], DP=23, GQ=33, PL=[0, 33, 442])), Call(sample=F14, CallData(GT=0/0, AD=[21, 0], DP=21, GQ=15, PL=[0, 15, 206])), Call(sample=F15, CallData(GT=0/0, AD=[25, 0], DP=25, GQ=33, PL=[0, 33, 395]))]
F1
0/0
13272 13273 13273
G [C] ['G', C]
...
```

如果你不想从头到尾循环某个文件。只想取某一部分，可以用fetch, 但是前体是用tabix对文件index， tabix前要用bgzip压缩.
```
bgzip testpyvcf.vcf  #得到testpyvcf.vcf.gz文件
tabix -p vcf testpyvcf.vcf.gz #得到testpyvcf.vcf.gz的index文件,testpyvcf.vcf.gz.tbi
```

```
for i in vcf_reader.fetch('chr1', 13273, 13372): #前开后闭
    print(i)
```

```
vcffile = open('test.vcf', 'r')          # 普通的文件打开操作

outvcf = open('outvcf.vcf', 'w')     #打开要写入的文件

myvcf = vcf.Reader(vcffile)         

woutvcf = vcf.Writer(outvcf, myvcf)          #将myvcf的header信息，写入到outvcf.vcf

for i in myvcf:

    woutvcf.write_record(i)                  #将myvcf的record写入到outvcf.vcf

vcffile.close()             

outvcf.close()            #将打开的文件关闭
```
#### Ref_Info
http://blog.csdn.net/qq_31088877/article/details/76921339   

## cyvcf2
##
https://github.com/vcflib/vcflib#vcffilter

https://github.com/alimanfoo/pysamstats
