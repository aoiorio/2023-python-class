try:
    print("簡単な仕事") # 簡単なお仕事
    raise Exception("error") # エラ
except:
    print("エラーが発生しました。")
else:
    print("処理正常")
