import json
from tqdm import tqdm

sources = []
with open('qua_input.txt', mode='r', encoding='utf-8') as handle:
    for line in handle:
        line = line.strip().split('\t')
        assert len(line) == 2
        sources.append(line[1])

index = 0
targets = []
with open('qua_labels.txt', mode='r', encoding='utf-8') as handle:
    for line in tqdm(handle):
        line = line.strip()
        if line[-1] == ',':
            line = line[:-1]
        line = line.split(', ')
        line = line[1:]
        source = sources[index]
        index += 1
        if line[0] == '-1':
            targets.append(source)
            continue
        
        chars = list(source)
        n = int(len(line) / 4)
        for i in range(n):
            i = i * 4
            p = int(line[i])
            t = line[i + 1]
            l = len(line[i + 2])
            c = line[i + 3]
            if t == '缺失':
                assert l == 0
                chars[p] = c + chars[p]
                continue
            assert source[p : p + l] == line[i + 2]
            if t == '冗余':
                assert c == ''
            chars[p] = c
            for j in range(1, l):
                chars[p + j] = ''

        targets.append(''.join(chars))

for source, target in zip(sources, targets):
    label = int(source != target)
    data = {"source": source, "target": target, "label": label}
    print(json.dumps(data, ensure_ascii=False))

