from googletrans import Translator
import pandas as pd

# reading and preprocessing CSV file
df = pd.read_csv('./CSVs/41.csv', header=1)
df = df.drop(['Unnamed: 3'], axis=1)
df.loc[-1] = ['79281', 'noun', 'a poker hand with 2 cards of the same value']
df.index = df.index + 1
df = df.sort_index()
df.columns = ['ID', 'POS', 'Gloss']

df['Gloss_persian'] = ''
df['Checked'] = False

# translating
translator = Translator()
translated_list = []
gloss_list = df['Gloss'].tolist()
gloss_persian = df['Gloss_persian']
# print(type(gloss_persian)) # <class 'pandas.core.series.Series'>
for index, value in gloss_persian.items():
    gloss = gloss_list[index]
    translated_obj = translator.translate(gloss, dest='fa')
    gloss_persian[index] = translated_obj.text
    # translated_list.append(translated_obj.text)
    # print(translated_obj.text)
# for index, value in gloss_persian.items():
#     gloss_persian[index] = translated_list[i]
print(gloss_persian)
df['Gloss_persian'] = gloss_persian
# df.to_csv('41_googletrans_translation.csv', index=False)