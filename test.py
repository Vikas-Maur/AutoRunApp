# import json 
        
    # # Data to be written 
    # dictionary ={ 
    # "id": "04", 
    # "name": "sunil", 
    # "depatment": "HR"
    # } 
        
    # # Serializing json 
    # json_object = json.dumps(dictionary, indent = 4) 
    # print(type(json_object)) 

    # with open("sample.json", "w") as outfile:  
    #     json.dump(dictionary, outfile)
    # import pyautogui
    # pyautogui.click(x=1249 , y=15)
import os
present_files = os.listdir()
img_file = []
file_extensions = ["jpeg", "jpg" , "png"]
for file in present_files:
    if ("jpeg" in file) or ("jpg" in file)or ("png" in file):
        img_file.append(file)
print(img_file)