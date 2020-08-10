import pyautogui
import keyboard
import os
import json

class DataSetter:

    def __init__(self,file_name):
        self.file_name = file_name
        self.content_info = {"COMMAND_INFO":{
            "TOTAL_COMMANDS":None,
            "COMMAND_NAMES" :[],
            "COMMAND_NAMES_WITH_INFO":{}
        }}

    def DumpGivenInstruction(self):
        with open(self.file_name , "w") as f:
            json.dump(self.content_info , f)
        return
    
    def SetTotalCommand(self):
        self.content_info["COMMAND_INFO"]["TOTAL_COMMANDS"] = len(self.content_info["COMMAND_INFO"]["COMMAND_NAMES"])
        return

    def AddNewCommand(self , command_name):
        self.content_info["COMMAND_INFO"]["COMMAND_NAMES"].append(command_name)
        return

    def AddCommandNameWithInfo(self,**kwargs):
        command_name = kwargs["command_name"]
        command_index = kwargs["command_index"]
        command_type = kwargs["command_type"]
        command_value = kwargs["command_value"]
        self.content_info["COMMAND_INFO"]["COMMAND_NAMES_WITH_INFO"][command_name] = [command_index , command_type , command_value]
        return

    def AddNewContentInfo(self,**kwargs):
        self.AddCommandNameWithInfo(**kwargs)
        self.AddNewCommand(kwargs["command_name"])
        self.SetTotalCommand()
        return

    def HandleClickInput(self):
        placing_cursor = True
        print("PRESS 'l' TO LOCK THE CURSOR POSITION")
        while placing_cursor:
            if keyboard.is_pressed('l'):
                keyboard.press_and_release("backspace")
                placing_cursor = False
        command_value = list(pyautogui.position())
        return command_value

    def HandleWriteInput(self):
        command_value = input("WHAT DO YOU WANT TO WRITE ? ")
        return command_value

    def HandleImageInput(self):
        present_files = os.listdir()
        img_file = []
        for file in present_files:
            if ("jpeg" in file) or ("jpg" in file)or ("png" in file):
                img_file.append(file)
        print(img_file)
        img_file_name = int(input("TYPE THE INDEX OF IMG FILE (INDEXING STARTS FROM 0) "))
        return img_file[img_file_name]

    def TakeCommandValue(self,command_type):
        if command_type=="CLICK":
            command_value = self.HandleClickInput()
        elif command_type=="WRITE":
            command_value = self.HandleWriteInput()
        else:
            command_value = self.HandleImageInput()
        return command_value

    def TakeInputToSaveTheFile(self):
        save_or_not = input("SAVE THE FILE OR NOT y/n :- ")
        if "y" in save_or_not.lower():
            self.DumpGivenInstruction()
            print(f"GIVEN INFO HAS BEEN SAVED TO THE FILE ---> {self.file_name}")
        else:
            actual_file = self.file_name
            self.file_name = "default.json"
            self.DumpGivenInstruction()
            self.file_name = actual_file
            print("GIVEN INFO HAS BEEN SAVED TO THE FILE ---> default.json")

    def TakeDataFromUser(self):
        running = True
        available_command_types = ["click" , "image" , "write"]
        command_index = 0
        while running:
            command_name = input("ENTER THE COMMAND'S NAME (MUST BE UNIQUE) ")
            command_type = input("ENTER THE TYPE OF COMMAND YOU WANT \n( 0 for click , 1 for image , 2 for write) ")
            command_type = available_command_types[int(command_type)].upper()
            command_value = self.TakeCommandValue(command_type)
            self.AddNewContentInfo(command_name = command_name , command_index = command_index , command_type = command_type , command_value = command_value)
            exiting = input("PRESS e TO EXIT or ANY KEY TO CONTINUE ")
            command_index += 1
            if exiting.lower() == "e":
                running = False
            else:
                running = True
        self.TakeInputToSaveTheFile()

    def PrintContentInfo(self):
        print(self.content_info)

if __name__ == "__main__":
    test_data_setter = DataSetter("test.json")
    test_data_setter.TakeDataFromUser()