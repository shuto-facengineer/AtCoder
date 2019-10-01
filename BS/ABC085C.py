from sys import exit
_n, _sum = map(int, input().split(" ")) # _n: お札の数, _sum: 合計額
 
if _sum > 10000*_n:
  # そもそも最大効率でもあり得ない場合
  print("-1 -1 -1")
  exit()
 
for _10000 in range(_n + 1):
  for _5000 in range(_n - _10000 + 1):
    # _10000 + _5000 + _1000 = _nの原則で二重ループ
    _1000 = _n - _10000 - _5000
    if _10000*10000 + _5000*5000 + _1000*1000 == _sum:
      # 条件を満たす組み合わせを一つでも見つけたら，出力して終了
      print("{} {} {}".format(_10000, _5000, _1000))
      exit()
print("-1 -1 -1")