import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
        def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_konstruktori_nollaa_negatiivisen_tilavuuden(self):
        varasto = Varasto(-10)
        self.assertAlmostEqual(varasto.tilavuus, 0)

    def test_konstruktori_nollaa_negatiivisen_alku_saldon(self):
        varasto = Varasto(10, -5)
        self.assertAlmostEqual(varasto.saldo, 0)

    def test_konstruktori_asettaa_saldon_tilavuuden_kokoiseksi_jos_yli_tilavuuden(self):
        varasto = Varasto(10, 15)
        self.assertAlmostEqual(varasto.saldo, 10)

    def test_lisaa_varastoon_ei_lisaa_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisaa_varastoon_tilavuuden_yli(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ota_varastosta_ei_ota_negatiivista_maaraa(self):
        otettu = self.varasto.ota_varastosta(-5)
        self.assertAlmostEqual(otettu, 0.0)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ota_varastosta_yli_saldo(self):
        self.varasto.lisaa_varastoon(5)
        otettu = self.varasto.ota_varastosta(10)
        self.assertAlmostEqual(otettu, 5)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_string_representation_varied(self):
        self.varasto.lisaa_varastoon(8)
        self.assertEqual(str(self.varasto), "saldo = 8, vielä tilaa 2")
    
