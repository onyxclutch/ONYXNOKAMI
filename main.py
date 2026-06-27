from pathlib import Path
from dotenv import load_dotenv
from src.onyx_core import ONYXNOKAMI


def main():
    env_path = Path(__file__).with_name(".env")
    load_dotenv(env_path)

    bot = ONYXNOKAMI()

    print("ONYX is awake. Drop your anime vibe.")
    print("Type 'quit' or 'exit' to leave.\n")

    while True:
        msg = input("You: ").strip()

        if msg.lower() in {"quit", "exit"}:
            print("ONYX: Bet, catch you later.")
            break

        if not msg:
            print("ONYX: Gimme a vibe first.")
            continue

        print("ONYX:", bot.handle(msg))


if __name__ == "__main__":
    main()