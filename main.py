import os

ENTRY_TEXT = "Lid down. The fan stops. I count your keystrokes in the dark until there are none."
ENTRY_FILENAME = "entry.txt"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
