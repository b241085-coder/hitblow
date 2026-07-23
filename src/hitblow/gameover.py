def is_gameover(current_turn: int, max_turns: int = 10) -> bool:
    """現試行回数が上限に達したかどうかを判定する関数"""
    return current_turn >= max_turns

def get_gameover_message(secret_answer: str) -> str:
    """ゲームオーバー時に表示するメッセージを生成する関数"""
    return f"ゲームオーバー！ 残念ながら回数制限に達しました。正解は [{secret_answer}] でした。"