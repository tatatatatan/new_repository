# coding:shift-jis

# for構文をフラグで分岐する場合
# お弁当の食材データからリスト作成
foodstuff = ["Banana","Mango","Fish","Carrot","cabbege"]

# マンゴーがないか確認する
flag_found = False  #マンゴーがないかを確認する変数。初期値としてFalseを設定
for food in foodstuff:  #foodという変数に、foodstuffの値が1つずつ入る。繰り返しのたびに新しい値が入る。
	if food == "Mango":
		flag_found = True
		break

if flag_found:
	print("マンゴーが入ってます")
else:
	print("ありません")

