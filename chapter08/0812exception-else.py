try:
    print("簡単な仕事") # 簡単なお仕事
    raise Exception("error") # エラーを発生させる
except:
    print("エラーが発生しました。")
else:
    print("処理正常") # エラーが発生しなかったら、処理正常と出力する
# else です
