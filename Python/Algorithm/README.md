



```python
#!/bin/python3

import math
import os
import random
import re
import sys

```
## 手法の確立
問題文から，まず手法を確立する．
ある配列において，ある数同士（２つ）の和がkで割り切れるかどうかは，その数たちのkによる余りで決まる．
- 余りを見れば，その和が割り切れるか否かわかる．
    * a+bが割り切れるかは，aとbのあまりの和が0になるか否かである．
- 足したときに0になるのは，あまりがrとk-rの組に分けれる
    * mod7において3と4は足したら0になっちゃう．
    * もちろんどちらかの組のみが取り出し可能．どちらも取り出すと余りの和が0になってしまう
    * 多いほうを取り出せばいい．
- 実際の余りのクラスによる処理
    * 余りが0のクラスは２つ選択は不可能なので１つのみ
    * kが偶数のとき
        + 余りがk//2のときは余りがk//2であるなかから1つだけ選べる．
        + rをk//2が最大値として分ける．（rとk-rの組に）
    * kが奇数のとき
        + rをk//2+1が最大値で分ける．（rとk-rの組に）
### ポイント
- 余りを考えると，aとbそれぞれの余りに着目すればよくなる．

- その余りどうしを足して0になるグループでは１つしか選べない．

- ある余りともう片方の余りを足して0になるグループでも１つしか選べない．


以下が記述部分
## 実際のコード
```python

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    counts = [0] * k
    #countsの中身が各要素をkで割った時の余りになる．
    for num in s:
        counts[num % k] += 1

    #counts[0]，余りが0のやつは一つしか選べない
    result = min(counts[0], 1)
    #偶数，奇数における条件
    upper = (k // 2) if (k % 2 == 0) else (k // 2 + 1)
    for i in range(1, upper):
        result += max(counts[i], counts[k - i])

    #偶数で，kの半分の値は，足したら0になっちゃうから1つしか選べない．    
    if k % 2 == 0:
        result += min(counts[k // 2], 1)

    return result
    
```
min(A,B)やmax(A,B)でAとBを比較して最小，最大の値を返す．


```python 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
