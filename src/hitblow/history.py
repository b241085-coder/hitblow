def add_history(history_list: list, guess: str, hit: int, blow: int) -> None:
    """プレイ履歴のリストに、今回の予想結果を追加する関数"""
    history_list.append({
        "turn": len(history_list) + 1,
        "guess": guess,
        "hit": hit,
        "blow": blow
    })

def format_history(history_list: list) -> str:
    """保存された履歴リストを見やすい表形式の文字列に変換する関数"""
    if not history_list:
        return "まだ履歴はありません。"

    lines = ["\n=== プレイ履歴 ==="]
    for record in history_list:
        lines.append(f"{record['turn']}回目: 予想 [{record['guess']}] -> Hit={record['hit']} / Blow={record['blow']}")
    lines.append("==================\n")
    return "\n".join(lines)