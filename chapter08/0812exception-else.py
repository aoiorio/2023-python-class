try:
    print("簡単な仕事") # 
    raise Exception("error")
except:
    print("エラーが発生しました。")
else:
    print("処理正常")