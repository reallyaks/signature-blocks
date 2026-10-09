# signature-blocks

Reads `By` / `Name` / `Title` stacks and lists them.

Not legal advice. It does not check a signature image, a DocuSign envelope, or whether the person had authority.

## Run

```bash
python -m signature_blocks samples/contract.txt --out /tmp/signers.md
python -m unittest discover -s tests
```

Committed output: [samples/signers.md](samples/signers.md). Python 3.10+. No packages.
