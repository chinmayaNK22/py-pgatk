import unittest

from pyteomics.parser import cleave

from pypgatk.proteomics.models import PYGPATK_ENZYMES


class MyTestCase(unittest.TestCase):

  def test_something(self):
    self.assertEqual(True, True)

  def test_enzyme_digestion(self):
    protein_sequence = "MRCGPLYRFLWLWPYLSYVEAVPIRKVQDDTKTLIKTIVTRINDISHTQSVSSKQRVTGLDFIPGLHPLLSLSKMDQTLAIYQQILASLPSRNVIQISNDLENLRDLLHLLAASKSCPLPQVRALESLESLGVVLEASLYSTEVVALSRLQGSLQDMLRQLDLSPGC"
    peptides = cleave(protein_sequence, PYGPATK_ENZYMES.enzymes['Trypsin']['cleavage rule'], 0, 0)
    self.assertEqual(len(peptides), 17)

    DESIRED_PEPTIDES = {
      "VTGJDFJPGJHPJJSJSKMDQTJAJYQQJJASJPSRNVJQJSNDJENJRDJJHJJAASK",
      "NVJQJSNDJENJRDJJHJJAASKSCPJPQVRAJESJESJGVVJEASJYSTEVVAJSR",
      "DJJHJJAASKSCPJPQVRAJESJESJGVVJEASJYSTEVVAJSRJQGSJQDMJR",
      "QRVTGJDFJPGJHPJJSJSKMDQTJAJYQQJJASJPSRNVJQJSNDJENJR",
      "JNDJSHTQSVSSKQRVTGJDFJPGJHPJJSJSKMDQTJAJYQQJJASJPSR",
      "SCPJPQVRAJESJESJGVVJEASJYSTEVVAJSRJQGSJQDMJRQJDJSPGC",
      "MDQTJAJYQQJJASJPSRNVJQJSNDJENJRDJJHJJAASKSCPJPQVR",
      "VTGJDFJPGJHPJJSJSKMDQTJAJYQQJJASJPSRNVJQJSNDJENJR",
      "SCPJPQVRAJESJESJGVVJEASJYSTEVVAJSRJQGSJQDMJR",
      "AJESJESJGVVJEASJYSTEVVAJSRJQGSJQDMJRQJDJSPGC",
      "DJJHJJAASKSCPJPQVRAJESJESJGVVJEASJYSTEVVAJSR",
      "MDQTJAJYQQJJASJPSRNVJQJSNDJENJRDJJHJJAASK",
      "QRVTGJDFJPGJHPJJSJSKMDQTJAJYQQJJASJPSR",
      "TJVTRJNDJSHTQSVSSKQRVTGJDFJPGJHPJJSJSK",
      "VTGJDFJPGJHPJJSJSKMDQTJAJYQQJJASJPSR",
      "AJESJESJGVVJEASJYSTEVVAJSRJQGSJQDMJR",
      "CGPJYRFJWJWPYJSYVEAVPJRKVQDDTK",
      "SCPJPQVRAJESJESJGVVJEASJYSTEVVAJSR",
      "JNDJSHTQSVSSKQRVTGJDFJPGJHPJJSJSK",
      "MDQTJAJYQQJJASJPSRNVJQJSNDJENJR",
      "NVJQJSNDJENJRDJJHJJAASKSCPJPQVR",
      "FJWJWPYJSYVEAVPJRKVQDDTKTJJK",
      "MRCGPJYRFJWJWPYJSYVEAVPJRK",
      "MRCGPJYRFJWJWPYJSYVEAVPJR",
      "VQDDTKTJJKTJVTRJNDJSHTQSVSSK",
      "CGPJYRFJWJWPYJSYVEAVPJRK",
      "FJWJWPYJSYVEAVPJRKVQDDTK",
      "CGPJYRFJWJWPYJSYVEAVPJR",
      "AJESJESJGVVJEASJYSTEVVAJSR",
      "TJJKTJVTRJNDJSHTQSVSSKQR",
      "NVJQJSNDJENJRDJJHJJAASK",
      "TJJKTJVTRJNDJSHTQSVSSK",
      "FJWJWPYJSYVEAVPJRK",
      "TJVTRJNDJSHTQSVSSKQR",
      "QRVTGJDFJPGJHPJJSJSK",
      "FJWJWPYJSYVEAVPJR",
      "MDQTJAJYQQJJASJPSR",
      "TJVTRJNDJSHTQSVSSK",
      "JQGSJQDMJRQJDJSPGC",
      "DJJHJJAASKSCPJPQVR",
      "VTGJDFJPGJHPJJSJSK",
      "KVQDDTKTJJKTJVTR",
      "VQDDTKTJJKTJVTR",
      "JNDJSHTQSVSSKQR",
      "NVJQJSNDJENJR",
      "JNDJSHTQSVSSK",
      "KVQDDTKTJJK",
      "VQDDTKTJJK",
      "JQGSJQDMJR",
      "DJJHJJAASK",
      "TJJKTJVTR",
      "MRCGPJYR",
      "SCPJPQVR",
      "KVQDDTK",
      "QJDJSPGC",
      "CGPJYR",
      "VQDDTK",
      "TJVTR",
      "TJJK",
      "MR",
      "QR",
      "K"
    }
    peptides = cleave(protein_sequence, PYGPATK_ENZYMES.enzymes['Trypsin']['cleavage rule'], 3, 0)
    self.assertEqual(len(peptides), len(DESIRED_PEPTIDES))


if __name__ == '__main__':
  unittest.main()
