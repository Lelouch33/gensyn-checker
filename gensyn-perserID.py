import requests
import time
from eth_abi import encode, decode
from eth_utils import keccak

# === НАСТРОЙКИ ===
ALCHEMY_RPC = "https://gensyn-testnet.g.alchemy.com/public"
CONTRACT = "0xFaD7C5e93f28257429569B854151A1B8DCD404c2"
PEER_ID_FILE = "peer_id.txt"
SEND_INTERVAL_SECONDS = 3600

BOT_TOKEN = "7939845255:AAG60iw7odo6K1KwpmP0JJu0FCGkbYDKAg0"
CHAT_ID = "410746253"
DEBUG = False

# === Telegram MarkdownV2 escape ===
def escape_md(text: str) -> str:
    for char in r"\_*[]()~`>#+-=|{}.!":
        text = text.replace(char, f"\\{char}")
    return text

def send_telegram(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "MarkdownV2"}
    try:
        resp = requests.post(url, data=payload)
        if resp.status_code != 200:
            print("❌ Telegram error:", resp.text)
    except Exception as e:
        print("⚠️ Telegram send failed:", e)

def eth_call(method_sig: str, encoded_data: str):
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_call",
        "params": [{"to": CONTRACT, "data": "0x" + method_sig + encoded_data}, "latest"]
    }
    response = requests.post(ALCHEMY_RPC, json=payload).json()
    if "error" in response:
        raise Exception(response["error"]["message"])
    return response["result"]

def get_total_rewards(peer_id: str):
    try:
        sig = "80c3d97f"
        encoded = encode(["string[]"], [[peer_id]]).hex()
        raw = eth_call(sig, encoded)
        reward_uint = decode(["uint256[]"], bytes.fromhex(raw[2:]))[0][0]
        return float(reward_uint)
    except Exception as e:
        print(f"[⛔] REWARD failed for {peer_id}: {e}")
        return "⛔"

def get_total_wins(peer_id: str):
    try:
        sig = "099c4002"
        encoded = encode(["string"], [peer_id]).hex()
        return int(eth_call(sig, encoded), 16)
    except Exception as e:
        print(f"[⛔] WINS failed for {peer_id}: {e}")
        return "⛔"

def get_total_wins(peer_id: str):
    try:
        sig = "099c4002"
        encoded = encode(["string"], [peer_id]).hex()
        return int(eth_call(sig, encoded), 16)
    except Exception as e:
        print(f"[⛔] WINS failed for {peer_id}: {e}")
        return "⛔"

def get_voter_vote_count(peer_id: str):
    try:
        sig = "dfb3c7df"
        encoded = encode(["string"], [peer_id]).hex()
        return int(eth_call(sig, encoded), 16)
    except Exception as e:
        print(f"[⛔] VOTES failed for {peer_id}: {e}")
        return "⛔"

def get_current_round():
    try:
        sig = keccak(text="currentRound()")[:4].hex()
        return int(eth_call(sig, ""), 16)
    except Exception as e:
        print(f"[⛔] currentRound failed: {e}")
        return "⛔"

def load_peer_ids():
    try:
        with open(PEER_ID_FILE, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("📄 Файл peer_id.txt не найден.")
        return []

def get_leaderboard():
    url = "https://dashboard.gensyn.ai/api/v1/leaderboard"
    try:
        resp = requests.get(url)
        resp.raise_for_status()
        data = resp.json()
        leaderboard = {}
        for rank, entry in enumerate(data.get("entries", []), start=1):
            peer_id = entry.get("peerId")
            if peer_id:
                leaderboard[peer_id] = rank
        print("✅ Leaderboard loaded successfully.")
        return leaderboard
    except Exception as e:
        print(f"[⛔] Failed to fetch leaderboard: {e}")
        return {}

def format_delta(current, previous):
    if previous is None:
        previous = 0
    delta = current - previous
    sign = "+" if delta >= 0 else "-"
    raw = f"({sign}{abs(delta)})"
    return escape_md(raw)

def main_loop():
    prev_stats = {}

    while True:
        peer_ids = load_peer_ids()
        if not peer_ids:
            time.sleep(SEND_INTERVAL_SECONDS)
            continue

        leaderboard = get_leaderboard()
        current_round = get_current_round()
        timestamp = escape_md(time.strftime('%Y-%m-%d %H:%M:%S'))

        lines = [
            f"*🕵️‍♂️ Gensyn Rewards*",
            f"_{timestamp}_",
            "",
            f"🔄 *Round:* `{escape_md(str(current_round))}`",
            "",
            "*📊 Peer Stats:*",
            ""
        ]

        for pid in peer_ids:
            wins = get_total_wins(pid)
            votes = get_voter_vote_count(pid)
            reward = get_total_rewards(pid)
            rank = leaderboard.get(pid)

            prev = prev_stats.get(pid, {"wins": 0, "votes": 0, "reward": 0})

            wins_delta = format_delta(wins if wins != "⛔" else 0, prev["wins"])
            votes_delta = format_delta(votes if votes != "⛔" else 0, prev["votes"])
            reward_delta = format_delta(reward if reward != "⛔" else 0, prev["reward"])

            wins_val = escape_md(str(wins)) if wins != "⛔" else "⛔"
            votes_val = escape_md(str(votes)) if votes != "⛔" else "⛔"
            reward_val = escape_md(f"{reward:g}") if isinstance(reward, float) else "⛔"
            rank_str = f"🏆 Rank: {rank}" if rank else "🏆 Rank: —"

            lines.append(f"`{escape_md(pid[-10:])}`")
            lines.append(f"  • Wins: {wins_val} {wins_delta}")
            lines.append(f"  • Votes: {votes_val} {votes_delta}")
            lines.append(f"  • Reward: {reward_val} {reward_delta}")
            lines.append(f"  • {rank_str}")
            lines.append("")

            prev_stats[pid] = {"wins": wins if wins != "⛔" else prev["wins"],
                               "votes": votes if votes != "⛔" else prev["votes"],
                               "reward": reward if reward != "⛔" else prev["reward"]}

        message = "\n".join(lines)
        if DEBUG:
            print(message)
        send_telegram(message)
        time.sleep(SEND_INTERVAL_SECONDS)

if __name__ == "__main__":
    main_loop()

