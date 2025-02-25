import json
import random
from tqdm import tqdm

random.seed(42)

with open('cctc_test_wide.json', mode='r', encoding='utf-8') as handle:
    for line in tqdm(handle):
        data = json.loads(line)
        sentences = data["sentences"]
        corrections = data["corrections"]
        sent_list = []
        num_errors = 0
        for sents, corrs in zip(sentences, corrections):
            for sent, corr in zip(sents, corrs):
                if not corr:
                    sent_list.append(sent)
                    continue
                num_errors += 1
                chars = list(sent)
                for c in corr:
                    p = c[0] - 1
                    t = c[1]
                    l = len(c[2])
                    r = c[3]
                    assert t in ["S", "R", "M", "W"]
                    if t == "M":
                        chars[p] = r + chars[p]
                        continue
                    assert sent[p : p + l] == c[2]
                    chars[p] = r
                    for i in range(1, l):
                        chars[p + i] = ''
                data2 = {"source": sent, "target": ''.join(chars), "label": 1}
                print(json.dumps(data2, ensure_ascii=False))

        if not sent_list:
            continue
        unique_sents = []
        n = int(num_errors / 2) + 1
        for i in range(n):
            sent = random.choice(sent_list)
            if sent in unique_sents:
                sent = random.choice(sent_list)
            if sent in unique_sents:
                continue
            unique_sents.append(sent)
            data2 = {"source": sent, "target": sent, "label": 0}
            print(json.dumps(data2, ensure_ascii=False))

