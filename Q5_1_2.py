# スタックをリストとして初期化
stack = []

# 要素1を追加
stack.append(1)
print("要素1追加後のスタック:", stack)

# 要素2を追加
stack.append(2)
print("要素2追加後のスタック:", stack)

# 先頭(トップ)から要素を取得
top_element1 = stack.pop()
print("1回目の要素取得:", top_element1)
print("1回目の要素取得後のスタック:", stack)

# もう一度先頭(トップ)から要素を取得
top_element2 = stack.pop()
print("2回目の要素取得:", top_element2)
print("2回目の要素取得後のスタック:", stack)

