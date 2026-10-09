# signature-blocks

Reads `By` / `Name` / `Title` stacks and lists them.

It does not look at a signature image or an electronic-signature certificate, and it does not check authority.

## Run

```bash
python -m signature_blocks samples/contract.txt --out /tmp/signers.md
python -m unittest discover -s tests
```

Committed output: [samples/signers.md](samples/signers.md). Python 3.10+. No packages.
