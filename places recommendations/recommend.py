import pandas as pd
import pickle

def recommend(place):
    place_index = place_dict[place_dict['Name'] == place].index[0]
    distances = similarity[place_index]
    places_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x : x[1])[1:15]
    for i in places_list:
        print(place_dict.iloc[i[0]].Name)
place_dict = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
places = pd.DataFrame(place_dict)
# print(places)
recommend('Jagannath Temple')