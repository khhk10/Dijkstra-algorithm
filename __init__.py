# coding:utf-8

import math

u = 0 # スタートとなる頂点
length = [[0, 50, 80, 0, 0], [50, 0, 20, 15, 0], [80, 20, 0, 10, 15], [0, 15, 10, 0, 30], [0, 0, 15, 30, 0]] # 各頂点間の距離

#初期化
min_distance = [0, math.inf, math.inf, math.inf, math.inf] # 各頂点までの最小距離 d(u)
prev = [None] * 5 # 最短経路をたどる際の前の頂点．ルートを出力する際に必要

remain_nodes = [0, 1, 2, 3, 4] # 未探索のノード

min_edge = math.inf

#探索する
while (len(remain_nodes) > 0):

    # 1. 未確定ノードの中からノードを一つ確定させる (頂点 u )
    # 操作：未探索ノードの中から、最小の d(u) をもつ頂点を削除し、 u に代入する
    min = math.inf
    for i in remain_nodes:
        if min > min_distance[i]:
            min = min_distance[i]
            u = i
    remain_nodes.remove(u)

    # 2. 頂点 u からの辺がある各頂点 v に対して、最小距離 d(v) を更新する
    for v in range(len(length)):
        # uからの辺がある各頂点vに対して
        if length[u][v] > 0:
            if min_distance[v] > min_distance[u] + length[u][v]:
                min_distance[v] = min_distance[u] + length[u][v] # "頂点vまでの最小距離"の更新
                prev[v] = u # "前の頂点"の更新

# 最短経路の表示
print("-------- Shortest Route --------")

num = len(length) - 1 # 終端ノードから表示

while (num >= 0):
    print(str(num + 1) + " <= ", end="")

    if prev[num] == None:
        num = -1
    else:
        num = prev[num]
