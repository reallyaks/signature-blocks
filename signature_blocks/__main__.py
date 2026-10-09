import argparse
from pathlib import Path

from signature_blocks.engine import find_signers, render


def main() -> None:
    parser = argparse.ArgumentParser(description="List By/Name/Title signature blocks.")
    parser.add_argument("contract")
    parser.add_argument("--out", default="signers.md")
    args = parser.parse_args()
    signers = find_signers(Path(args.contract).read_text())
    Path(args.out).write_text(render(signers, Path(args.contract).name))
    print(f"{args.out}: {len(signers)} blocks")


if __name__ == "__main__":
    main()
