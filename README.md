## CTCDataset

本仓库收集了一些开源的中文拼写/语法纠错数据集，可用于中文纠错模型的训练。数据集均已处理为如下的 jsonl 格式：

```json
{
    "source": "完善农产品上行发展机智。",
    "target": "完善农产品上行发展机制。",
    "label": 1
}
```

`source`为可能包含拼写/语法错误的源句子，`target`为纠错后的目标句子，`label`表示源句子中是否包含错误，若`label`为1，则包含错误，否则不包含错误。

### 拼写纠错

- **ECSpell**：法律、医学、政府领域拼写纠错数据集，来自 
  
  https://github.com/aopolin-lv/ECSpell/tree/main/Data/domains_data

- **cscd-ns**：针对母语人士的中文拼写纠错数据集，包括 40,000 个来自新浪微博真实帖子的注释句子。来自 https://github.com/nghuyong/cscd-ns
  
  LCSTS-IME-2M 是一个用于中文拼写检查任务的大规模、高质量的伪数据集，包括超过 200 万个样本。源句子来自 LCSTS 数据集，通过拼音 IME 模拟输入构建。百度网盘下载地址: https://pan.baidu.com/s/1v7wpw65z0mmnB4XOzdF_jQ  提取码: gv7m

- **lemon**：多领域拼写纠错数据集，包括汽车、游戏、医疗、新闻、小说等领域，来自 https://github.com/gingasan/lemon/tree/main/lemon_v2

- **MCSCSet**：医疗领域拼写纠错数据集，来自
  
  https://github.com/yzhihao/MCSCSet/tree/main/data/mcsc_benchmark_dataset

- **sighan**：sighan13、sighan14、sighan15 拼写纠错数据集，来自
  
  https://github.com/onebula/sighan_raw/tree/master/pair_data/simplified

- **Wang271k**：一份基于 OCR 和 ASR 方法合成的中文拼写纠错数据集，包含 27w+ 个句子对，来自 
  
  https://github.com/wdimmy/Automatic-Corpus-Generation/tree/master/corpus

- **yacsc**：包含 2550 个句对的拼写纠错数据集，位于`yacsc/YACSC/YACSC-no_GE.jsonl`
  
  来自 https://github.com/blcuicall/yacsc
  
  该项目同时提供了校对后的 sighan 测试集，缓解原始 sighan 测试集中由于繁简转换带来的噪音以及漏标误标问题，位于`yacsc/sighan_revised/`目录下。

- **NLPCC2023-task8**：中文拼写检查数据集，包含 1000 条手动识别和标记的句子对，其中 500 条包含拼写错误，500 条不含错误。来自 
  
  https://github.com/Arvid-pku/NLPCC2023_Shared_Task8/blob/main/data/data.txt

### 语法错误

- **CTC2021**：中文文本纠错比赛，来自 https://github.com/destwang/CTCResources
- **midu2022**：蜜度中文文本智能校对大赛，初赛阶段约 1000 条真实场景训练集数据位于`midu2022/preliminary_extend_train.jsonl`，初赛阶段约 1000 条真实场景验证集数据位于`midu2022/preliminary_val.jsonl`。决赛阶段约 2900 条真实场景数据位于`midu2022/final.jsonl`。
  
  初赛阶段约 100 万条伪数据下载地址：
  
  https://pan.baidu.com/s/1gS2dpcQIZpvyT-a1jEsGSQ
  
  提取码: 99d7
- **yacsc**：包含 2550 个句对的语法纠错数据集，位于`yacsc/YACSC/YACSC-with_GE.jsonl`，来自 https://github.com/blcuicall/yacsc
- **NLPCC2023-task1**：任务一中文语法纠错数据集，来自 http://tcci.ccf.org.cn/conference/2023/taskdata.php
  
  处理了 HSK 和 MuCGEC 两个数据集，位于`NLPCC2023/grammar/`目录下。

### 样本数量统计

```shell
2460 ECSpell/ec_law.jsonl
3500 ECSpell/ec_med.jsonl
2220 ECSpell/ec_odw.jsonl

40000 cscd-ns/all.jsonl
 5000 cscd-ns/dev.jsonl
 5000 cscd-ns/test.jsonl
30000 cscd-ns/train.jsonl

3410 lemon/car.jsonl
1026 lemon/cot.jsonl
3434 lemon/enc.jsonl
 400 lemon/gam.jsonl
2090 lemon/mec.jsonl
5892 lemon/new.jsonl
6000 lemon/nov.jsonl

196496 MCSCSet/filtered_data.jsonl
 19650 MCSCSet/test.jsonl
157194 MCSCSet/train.jsonl
 19652 MCSCSet/valid.jsonl

271281 Wang271k/data.jsonl

1000 sighan/sighan13_test.jsonl
 350 sighan/sighan13_train.jsonl
1062 sighan/sighan14_test.jsonl
3437 sighan/sighan14_train.jsonl
1100 sighan/sighan15_test.jsonl
2339 sighan/sighan15_train.jsonl

1000 yacsc/sighan_revised/test_sighan13.jsonl
1062 yacsc/sighan_revised/test_sighan14.jsonl
1100 yacsc/sighan_revised/test_sighan15.jsonl
2550 yacsc/YACSC/YACSC-no_GE.jsonl
2550 yacsc/YACSC/YACSC-with_GE.jsonl

217634 CTC2021/train_large_v2.jsonl
   969 CTC2021/val.jsonl

2919 midu2022/final.jsonl
1000 midu2022/preliminary_extend_train.jsonl
1014 midu2022/preliminary_val.jsonl

156831 NLPCC2023/grammar/HSK/hsk.jsonl
  2467 NLPCC2023/grammar/MuCGEC/MuCGEC_dev_all.jsonl
  1137 NLPCC2023/grammar/MuCGEC/MuCGEC_dev_min_edit_distance.jsonl
  1000 NLPCC2023/spell/data.jsonl
```

### 声明

本仓库数据集只能用于学术研究，请勿用作商业。


