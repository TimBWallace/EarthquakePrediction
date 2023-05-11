import pandas as pd
from googletrans import *

translator = Translator()


def translate(word):
    """languages = ('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am',
                'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
                'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn', 'bosnian',
                'bs', 'bulgarian', 'bg', 'catalan', 'ca',
                'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)',
                'zh-cn', 'chinese (traditional)', 'zh-tw',
                'corsican', 'co', 'croatian', 'hr', 'czech', 'cs', 'danish',
                'da', 'dutch', 'nl', 'english', 'en', 'esperanto',
                'eo', 'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi',
                'french', 'fr', 'frisian', 'fy', 'galician', 'gl',
                'georgian', 'ka', 'german', 'de', 'greek', 'el', 'gujarati',
                'gu', 'haitian creole', 'ht', 'hausa', 'ha',
                'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi', 'hmong',
                'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo',
                'ig', 'indonesian', 'id', 'irish', 'ga', 'italian', 'it',
                'japanese', 'ja', 'javanese', 'jw', 'kannada', 'kn',
                'kazakh', 'kk', 'khmer', 'km', 'korean', 'ko', 'kurdish (kurmanji)',
                'ku', 'kyrgyz', 'ky', 'lao', 'lo',
                'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish',
                'lb', 'macedonian', 'mk', 'malagasy',
                'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori',
                'mi', 'marathi', 'mr', 'mongolian', 'mn',
                'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no',
                'odia', 'or', 'pashto', 'ps', 'persian',
                'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa',
                'romanian', 'ro', 'russian', 'ru', 'samoan',
                'sm', 'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho',
                'st', 'shona', 'sn', 'sindhi', 'sd', 'sinhala',
                'si', 'slovak', 'sk', 'slovenian', 'sl', 'somali', 'so',
                'spanish', 'es', 'sundanese', 'su',
                'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil',
                'ta', 'telugu', 'te', 'thai', 'th', 'turkish', 'tr',
                'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug', 'uzbek',
                'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
                'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu')
                """
    translation = translator.translate(word, 'english')
    return translation.text


def importCSV():
    df = pd.read_csv('dataset/earthquakes_japan.csv')
    df.convert_dtypes()
    countRows = len(df)

    translatedCSV = {'震央地名': [], '最大震度': []}

    for index, row in df.iterrows():
        translatedCSV['震央地名'].append(str(translate(row['震央地名'])))

        translatedCSV['最大震度'].append(str(translate(row['最大震度'])))

    df = pd.DataFrame(data=translatedCSV)
    df.to_csv("japTranslated.csv", sep='\t')


importCSV()
