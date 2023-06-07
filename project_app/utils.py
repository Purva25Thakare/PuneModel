import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config


class PuneHouse():
    def __init__(self, area_type,availability,size,total_sqft,bath,balcony,site_location):
        self.area_type = "area_type_"+ area_type
        self.availability = "availability_"+ availability
        self.size = "size_"+ size
        self.total_sqft = total_sqft
        self.bath = bath
        self.balcony=balcony
        self.site_location= "site_location_" + site_location

    def load_models(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
        #with open("Pune_linear_model.pkl", "rb") as f:
            self.linear_reg_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
        #with open("Project_data_pune.json", "r") as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):

        self.load_models()   # Creating instance of model and json_data

        area_type_index = list(self.json_data['columns']).index(self.area_type)
        availability_index = list(self.json_data['columns']).index(self.availability)
        size_index = list(self.json_data['columns']).index(self.size)
        site_location_index = list(self.json_data['columns']).index(self.site_location)

        test_array = np.zeros(len(self.json_data['columns']))

        # test_array[area_type_index] = 1
        # test_array[availability_index] = 1
        # test_array[size_index] = 1
        # test_array[3] = self.total_sqft
        # test_array[4] = self.bath
        # test_array[5] = self.balcony
        # test_array[site_location_index]=1
        test_array[0] = self.total_sqft
        test_array[1] =self. bath
        test_array[2] = self.balcony
        test_array[area_type_index] = 1
        test_array[availability_index] = 1
        test_array[size_index] = 1
        test_array[site_location_index] = 1
        
        print("Test Array -->\n", test_array)

        price = round(self.linear_reg_model.predict([test_array])[0],2)

        return price


if __name__ == "__main__":
    area_type="Super built-up  Area"   
    availability="Ready To Move"
    size="2 BHK"
    total_sqft=1056
    bath=2.0
    balcony=1.0
    site_location="Alandi Road"

    pune = PuneHouse(area_type,availability,size,total_sqft,bath,balcony,site_location)
    price = pune.get_predicted_price()
    print("Predicted Price:", price,"Lakhs")