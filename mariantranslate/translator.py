from typing import List, Union

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class Translator:
    def __init__(self, lang_from, lang_to):
        self.tokenizer = AutoTokenizer.from_pretrained(
            f"Helsinki-NLP/opus-mt-{lang_from}-{lang_to}"
        )
        self.model = AutoModelForSeq2SeqLM.from_pretrained(
            f"Helsinki-NLP/opus-mt-{lang_from}-{lang_to}"
        )

    def translate(self, s: Union[str, List[str]]) -> Union[str, List[str]]:
        if isinstance(s, list):
            return self._batch_translate(s)
        elif isinstance(s, str):
            return self._single_translate(s)
        else:
            raise TypeError("Input must be string or list of string")

    def _single_translate(self, s: str) -> str:
        batch = self.tokenizer(s, return_tensors="pt")
        generated_text = self.model.generate(**batch)
        result = self.tokenizer.batch_decode(generated_text, skip_special_tokens=True)
        result = result[0]

        return result

    def _batch_translate(self, s: List[str]) -> List[str]:
        batch = self.tokenizer(s, return_tensors="pt", padding=True)
        generated_text = self.model.generate(**batch)
        result = self.tokenizer.batch_decode(generated_text, skip_special_tokens=True)

        return result


# add unable to translate
