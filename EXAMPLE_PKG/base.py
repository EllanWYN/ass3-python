
def hello():
    return 'u r so fukin cute'

import os
import re
import glob


class salad():

    def __init__(self):
        self.path = ''

    # input path, [tomato, lettuce], [2,3]
	# output
	# tomato_00.salad
	# tomato_01.salad    
    def write(self, path, salad, n_items):
        # should receive a path
        self.path = path
        print(self.path)
        
        # error handling
        assert len(salad) == len(n_items), 'Not Cool!'
        
        os.makedirs(self.path, exist_ok = True)
        
        for k in range(len(salad)):
            print(salad[k], n_items[k])
            for j in range(n_items[k]):
                file_name = salad[k] + str(j).zfill(2) + '.salad'
                print(os.path.join(self.path, file_name))
                new_file = open(os.path.join(self.path, file_name), 'w')
                new_file.close()


    
    def read(self, path):
        flrst = glob.glob(os.path.join(path,'*.salad'))
        dic = {}
        for file in flrst:
            #pattern = ".salad"
            stripe_salad = os.path.splitext(file)[0]
            split = stripe_salad.split("/")
            value = str(split[len(split[0])-1])
            ingredient = re.sub(r'\d+', '', value)
            if ingredient not in dic.keys():
                dic[ingredient] =1
            else:
                dic[ingredient] +=1
        return dic


 