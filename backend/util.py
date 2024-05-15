import pickle
import json
import numpy as np

class Util:
    def __init__(self):
        self.__data_columns = None
        self.__locations = None
        self.__model = None
        self.load_saved_artifacts()

    #Price prediction
    def get_estimated_price(self, location, sqft, bhk, bath):
        try:
            loc_index = self.__data_columns.index(location.lower())
        except:
            loc_index = -1

        x = np.zeros(len(self.__data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if loc_index>=0:
            x[loc_index] = 1

        return round(self.__model.predict([x])[0],2)

    #loading saved artifacts
    def load_saved_artifacts(self):
        print("loading saved artifacts...start")
        with open("columns.json", "r") as f:
            self.__data_columns = json.load(f)['data_columns']
            self.__locations = self.__data_columns[3:]  # first 3 columns are sqft, bath, bhk

        if self.__model is None:
            with open('banglore_home_prices_model.pickle', 'rb') as f:
                self.__model = pickle.load(f)
        print("loading saved artifacts...done")
        
    #Getting all location names
    def get_location_names(self):
        return self.__locations
    
    #Getting all data columns
    def get_data_columns(self):
        return self.__data_columns

if __name__ == '__main__':
    util = Util()
    print(util.get_location_names())
    print(util.get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(util.get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(util.get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(util.get_estimated_price('Ejipura', 1000, 2, 2))  # other location