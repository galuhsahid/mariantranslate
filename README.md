# mariantranslate
Simple translator using Marian NMT.

## installation
```bash
$ pip install mariantranslate
```

or install from source:

```
$ git clone https://github.com/galuhsahid/mariantranslate
$ cd mariantranslate
$ make install_src
```

## usage
View the list of available languages [here](https://huggingface.co/Helsinki-NLP).

```python
from mariantranslate import Translator

lang_from = "en" # source language
lang_to = "id" # target language

en_id_translator = Translator(lang_from, lang_to)
en_id_translator.translate("Due to the limited vegetation cover of the Faroe Islands, it is relatively easy to follow the history of geology.")

>>> Karena tumbuhan terbatas menutupi Kepulauan Faroe, relatif mudah untuk mengikuti sejarah geologi.
```