import unittest
from pathlib import Path

from signature_blocks.engine import find_signers, render

TEXT = Path("samples/contract.txt").read_text()


class SignerTests(unittest.TestCase):
    def test_two_blocks(self):
        signers = find_signers(TEXT)
        self.assertEqual([(item.name, item.title) for item in signers], [("Ada Okonkwo", "General Counsel"), ("Priya Shah", "Counsel")])

    def test_committed_report(self):
        self.assertEqual(render(find_signers(TEXT), "contract.txt"), Path("samples/signers.md").read_text())


if __name__ == "__main__":
    unittest.main()
