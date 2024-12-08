import tkinter as tk
from tkinter import messagebox
from example import main  # example.pyのmain関数をインポート

def execute_main():
    try:
        # 入力値を取得し、float型に変換
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        # example.pyのmain関数を実行
        main(a, b, c)

        # 計算結果をポップアップで表示

    except ValueError:
        # 無効な入力時にエラーメッセージを表示
        messagebox.showerror("エラー", "数値を正しく入力してください！")

# GUIウィンドウの設定
root = tk.Tk()
root.title("Example.py 実行")

# ラベルとエントリーフィールド
tk.Label(root, text="phi rel:").grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="gamma heat:").grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="gamma vapor:").grid(row=2, column=0, padx=10, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=5)

# 実行ボタン
execute_button = tk.Button(root, text="calculation start!", command=execute_main)
execute_button.grid(row=3, columnspan=2, pady=10)

# メインループを開始
root.mainloop()
