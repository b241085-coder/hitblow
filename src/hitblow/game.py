"""ゲームの進行（入力・表示・ループ）。

★ チームで足す機能は **自分の担当の場所**に書く（1機能=1ファイル）。
   下の「ここに足す」場所は3か所（① 開始時 ② 入力コマンド ③ 勝利時）。
   ペアごとに**別の場所**を直すので、並行作業でも衝突しない。
   import も自分の場所の近くに書くこと（ファイル先頭にまとめない＝衝突回避）。
"""

from .core import judge, make_secret


def play(digits=3):
    secret = make_secret(digits)
    print(f"Hit & Blow（{digits} 桁・重複なし）")

    # ===== ① 開始時に足す（難易度・あいさつ など）: ここに書く =====
    from history import add_history, format_history
    turn_count = 0
    history_list = []
    max_turns = 10

    tries = 0
    while True:
        # ===== ② 入力コマンドに足す（ヒント など）: ここに書く（import もここに） =====
        # 例:  from .hint import hint
        #      if guess == "h":
        #          print(hint(secret)); continue

        guess = input("予想 (履歴を見るには 'h' を入力) > ").strip()
        if guess.lower() == 'h':
            print(format_history(history_list))
            continue
        turn_count += 1

        if len(guess) != digits or not guess.isdigit():
            print(f"{digits} 桁の数字で入力してね")
            continue
        tries += 1
        hit, blow = judge(secret, guess)
        print(f"  Hit={hit}  Blow={blow}")

        # ===== ③ 勝利時に足す（スコア・履歴 など）: ここに書く =====
        from gameover import is_gameover, get_gameover_message

        add_history(history_list, guess, hit, blow)

        if hit == 3:
            print("おめでとう！ 正解です！")
            break

        if is_gameover(turn_count, max_turns):
            print(get_gameover_message(secret))
            break

        if hit == digits:
            print(f"正解！ {tries} 回で当たり（答え {secret}）")
            break