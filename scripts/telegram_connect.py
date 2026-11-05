"""
Kayrbeṭ bot Telegram b l'automation (kaykhdem f PC dyalk).

1. Kay9ra TELEGRAM_BOT_TOKEN men fichier .env (machi men chat).
2. Kayl9a chat ID dyalk men l'message /start li sifti l'bot.
3. Kayzid TELEGRAM_BOT_TOKEN w TELEGRAM_CHAT_ID f GitHub Secrets.
4. Kaysifet lik message dyal tjriba f Telegram.

Usage:
  python scripts/telegram_connect.py --env "C:\\path\\text.env" --repo owner/repo
"""
import argparse
import subprocess
import sys

import requests


def read_env(path):
    vals = {}
    for line in open(path, encoding="utf-8-sig"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            vals[k.strip()] = v.strip().strip('"').strip("'")
    return vals


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", required=True)
    ap.add_argument("--repo", required=True)
    a = ap.parse_args()

    token = read_env(a.env).get("TELEGRAM_BOT_TOKEN")
    if not token:
        sys.exit("Zid TELEGRAM_BOT_TOKEN=... f " + a.env)
    api = f"https://api.telegram.org/bot{token}"

    me = requests.get(f"{api}/getMe", timeout=30).json()
    if not me.get("ok"):
        sys.exit("Token ghalṭ: 3awed copier l'token men @BotFather.")
    print(f"Bot: @{me['result']['username']}")

    updates = requests.get(f"{api}/getUpdates", timeout=30).json().get("result", [])
    chats = [u["message"]["chat"] for u in updates if "message" in u and u["message"]["chat"]["type"] == "private"]
    if not chats:
        sys.exit(f"Ma l9it 7ta message. 7ell @{me['result']['username']} f Telegram, sifet /start, w 3awed lanci l'script.")
    chat = chats[-1]
    print(f"Chat: {chat.get('first_name', '')} {chat.get('last_name', '')}".strip())

    for name, value in (("TELEGRAM_BOT_TOKEN", token), ("TELEGRAM_CHAT_ID", str(chat["id"]))):
        subprocess.run(["gh", "secret", "set", name, "-R", a.repo], input=value.encode(), check=True,
                       stdout=subprocess.DEVNULL)
        print(f"  ✓ GitHub secret {name}")

    requests.post(f"{api}/sendMessage", timeout=30, data={
        "chat_id": chat["id"],
        "text": "✅ Lidpet: Telegram mconnecti! Kol post ghadi tjik l'vidéo hna + captions dyal Instagram, Facebook w TikTok."})
    print("\nSalina ✅ Chouf Telegram: siftlek message dyal tjriba.")


if __name__ == "__main__":
    main()
