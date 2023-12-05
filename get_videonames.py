import pandas as pd
import numpy as np
import torch
from sentence_transformers import SentenceTransformer, util
import nltk
nltk.download('punkt')
import pymorphy2
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('df_embed_1.csv')

# model = SentenceTransformer('ai-forever/sbert_large_nlu_ru')
# model.save('model.bin')
model = SentenceTransformer('model.bin')

morph = pymorphy2.MorphAnalyzer()

df['vector_embeddings'] = df['vector_embeddings'].apply(lambda x: list(map(float, x.strip('[]').split(','))))

def get_word_embedding(word):
    word_vector = model.encode(word, convert_to_tensor=True)
    return word_vector

def find_similar_words(sentence, dataset):
    tokens = nltk.word_tokenize(sentence)
    for i, word in enumerate(tokens):
        p = morph.parse(word)[0]
        if 'VERB' in p.tag:
            tokens[i] = p.normal_form
        elif 'NOUN' in p.tag:
            tokens[i] = p.normal_form
        else:
            tokens[i] = word
    word_embeddings = [get_word_embedding(word) for word in tokens]
    similar_words = [] 
    similarity_score = []
    for word_vector in word_embeddings:
        similarities = cosine_similarity(word_vector.reshape(1, -1), df['vector_embeddings'].values.tolist())
        max_sim_index = np.argmax(similarities)

        if similarities[0, max_sim_index] >= 0.77:
            similar_words.append((df.loc[max_sim_index, 'text'], dataset[dataset == df.loc[max_sim_index, 'text']].index[0]))
            similarity_score.append(similarities[0, max_sim_index])
    return similar_words, similarity_score

def get_videoname(similar_words):
    b = []
    for i in range(len(similar_words)):
       b.append(df.iloc[similar_words[i][1]]['attachment_id']+'.mp4')
    return b

user_input = input("Введите предложение: ")
similar_words, score = find_similar_words(user_input, df['text'])
list_of_videos = get_videoname(similar_words)
print(f"Близкие слова: {similar_words}")
print(f"Точность слов: {score}")
print(f'Названия видеофайлов: {list_of_videos}')