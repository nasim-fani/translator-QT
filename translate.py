from googletrans import Translator
from model import Model
import time

class TranslateWordnet:
    @staticmethod
    def translateSentences(startID, endID):
        db = Model()
        translator = Translator()
        for i in range(startID, endID + 1):
            item = db.select(model_name="wordnet",
                             condition="id={}".format(i))  # id:0, pos:1, gloss:2, gloss_persion:3, checked:4
            item = item[0]
            en_sentence = item[2].replace("'", '"')
            translated_obj = translator.translate(en_sentence, dest='fa')
            gloss_persian = translated_obj.text
            if i % 300 == 0:
                time.sleep(20)
            db.update(model_name="wordnet", update_array={
                "gloss_persian": "N'{}'".format(gloss_persian),
                "checked": "false"
            }, condition="id={}".format(i))
            print(i)

if __name__ == '__main__':
    t = TranslateWordnet()
    t.translateSentences(79281, 81262)
