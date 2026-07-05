"""
ハッシュテーブル
特定の要素xが含まれているかを調べるには、配列、連結リストどちらの場合でもO(N)の計算量を要する。
hash tableの場合、平均的にO(1)の計算量で検索できる。


キーと値のペアを格納するためのデータ構造。ハッシュ関数を使い、各キーの
Pythonではdictがハッシュテーブルとして実装されている。
"""


def is_subset_of_another_ary(ary1: list[int], ary2: list[int]):
    if len(ary1) > len(ary2):
        largerAry, smallerAry = ary1, ary2
    else:
        largerAry, smallerAry = ary2, ary1

    for i in range(len(smallerAry)):
        found_flag = False

        for j in range(len(largerAry)):
            if smallerAry[i] == largerAry[j]:
                found_flag = True
                break
        if not found_flag:
            return False

    return True


"""
is_subset_of_another_aryの計算量はO(N*M)
両方の配列を走査するので、長さが同程度ならO(N^2)になる。
ハッシュテーブルを使うと、is_subset_of_another_ary_hash_verの計算量は平均的にO(N+M)になる。
"""


def is_subset_of_another_ary_hash_ver(ary1: list[int], ary2: list[int]):
    hash_table: dict[int, bool] = {}

    if len(ary1) > len(ary2):
        largerAry, smallerAry = ary1, ary2
    else:
        largerAry, smallerAry = ary2, ary1

    for v in largerAry:
        hash_table[v] = True

    for v in smallerAry:
        if hash_table.get(v) is None:
            return False
    return True


print(is_subset_of_another_ary_hash_ver([2, 3, 4], [1]))
