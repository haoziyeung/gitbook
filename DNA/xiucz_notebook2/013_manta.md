利用intansv包对SV结果进行处理；
https://bioconductor.org/packages/release/bioc/html/intansv.html

https://github.com/Illumina/manta

## breakdancer
```
https://sourceforge.net/projects/breakdancer/files/breakdancer-1.1.2_2013_03_08.zip/download
cd breakdancer-1.1.2/cpp/

## 发现版本太低，换安装方法
#https://cmake.org/files/v3.10/cmake-3.10.0-rc3.tar.gz
tar -zxvf cmake-3.10.0-rc3.tar.gz
cd cmake-3.10.0-rc3


#git clone git@github.com:genome/breakdancer.git ##......
git clone --recursive git://github.com/genome/breakdancer.git
cd breakdancer/
```

## TMAP
```
tmap mapall \
-v -n 20 -o 2 -a 0 -m 10 \
-f  genome.fa  \
-r Sample.fastq stage1 map1 map2 map3 > Sample.bam
参数说明：
-n 代表所运行线程数目;-f 参考序列；-r 测序数据
-0 代表的是输出的比对格式;
   0-SAM;
   1-BAM(compressed)
   2-BAM (uncompressed)                                                                            
 -a 比对输出过滤:
    1 - random best hit;
    2 - all best hits;                                                       
    3 - all alignments;
-m 比对输出过滤
   mapping quality threshold for read rescue
```




## Reference_Info
http://blog.sina.com.cn/s/blog_49beed9d0102wl71.html  
