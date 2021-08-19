import pytest
from translator import Translator


class TestTranslator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.en_id_translator = Translator("en", "id")

    def test_single_translate(self):
        text_en = "Due to the limited vegetation cover of the Faroe Islands, it is relatively easy to follow the history of geology."
        expected = "Karena tumbuhan terbatas menutupi Kepulauan Faroe, relatif mudah untuk mengikuti sejarah geologi."
        result = self.en_id_translator.translate(text_en)

        assert expected == result

    def test_batch_translate(self):
        texts_en = [
            "The middle basalt series consists of thin lava flows with a highly porous interlayer.",
            "This means that shops and services are now relocating en masse from the villages into the centres",
            "By road, the main islands are connected by bridges and tunnels.",
        ]
        expected = [
            "Seri basal tengah terdiri dari aliran lava tipis dengan interlayer yang sangat berpori.",
            "Ini berarti bahwa toko-toko dan layanan sekarang relokasi massal dari desa-desa ke pusat-pusat",
            "Melalui jalan, pulau-pulau utama terhubung oleh jembatan dan terowongan.",
        ]
        result = self.en_id_translator.translate(texts_en)

        assert expected == result
