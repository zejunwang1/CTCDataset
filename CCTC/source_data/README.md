# The CCTC dataset
## Version: 1.1

## Data Description
```
{"sentences": [["松溪县政法委机关党委开展提升群众安全感满意度宣传活动"], ["为进一步深化\"平安松溪\"建设,全面推进扫黑除恶专项斗争工作深入开展,进一步营造全社会广泛参与平安建设的良好氛围,切实提升群众安全感满意度。", "近日,松溪县政法委机关党委组织党员在辖区沿街店铺开展入户式平安建设专项宣传活动。"], ["活动现场,党员通过向沿街商铺分发\"群众安全感满意度调查问卷\"和\"扫黑除恶\"等宣传资料及小礼品,与群众面对面交流,向群众集中宣传了在接受群众安全感满意度调查时应注意的相关事项。", "同时,向群众介绍开展扫黑除恶专项斗争工作的重大意义和平安建设成效,并讲解了防范邪教、电信诈骗、防火防盗等各类日常生活密切相关的安全防范知识,提醒群众提高安全防范意识和自我保护能力,鼓励和引导群众积极主动参与到扫黑除恶专项斗争和平安建设中来。"], ["本次活动共分发宣传资料70余份,进一步提高群众对社会管理综合治理和平安建设工作的知晓率和参与率,激发广大群众积极主动参与到平安建设工作来,使平安知识深入人心,形成创建平安松溪的良好氛围。"]], "corrections": [[[]], [[], []], [[], []], [[[68, "M", "", "中"]]]], "doc_id": "6919"}
```
sentences: [[sent1, sent2], [sent3, sent4, sent5]] where [sent1, sent2] is a paragraph.

corrections:[[[], []], [[], [], [position, error type, erroneous tokens, correct tokens]]]

position: start from 1 in corresponding sentence

error type: **S**pelling, **R**eduntant, **M**issing, **W**order ordering

if the error type is missing error, we prepend the correct tokens to the position of the sentence.

### Others
Several inappropriate articles have been deleted, so the statistical information is slightly different from the paper.

### Citation
@inproceedings{wang-etal-2022-cctc,
    title = "{CCTC}: A Cross-Sentence {C}hinese Text Correction Dataset for Native Speakers",
    author = "Wang, Baoxin  and
      Duan, Xingyi  and
      Wu, Dayong  and
      Che, Wanxiang  and
      Chen, Zhigang  and
      Hu, Guoping",
    booktitle = "Proceedings of the 29th International Conference on Computational Linguistics",
    month = oct,
    year = "2022",
    address = "Gyeongju, Republic of Korea",
    publisher = "International Committee on Computational Linguistics",
    url = "https://aclanthology.org/2022.coling-1.294",
    pages = "3331--3341",
}