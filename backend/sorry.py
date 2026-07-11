name = input("名前を入力してください: ")

print(f"こんにちは、{name}さん！")
print("今日も一日頑張りましょう！")

score = int(input("テストの点数を入力してください: "))

if score >= 80:
    print("評価: 優秀です！")
elif score >= 60:
    print("評価: 合格です！")
else:
    print("評価: もう少し頑張りましょう。")