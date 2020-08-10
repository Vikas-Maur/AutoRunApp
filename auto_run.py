import pyautogui
import keyboard
import json

class AutoRun:
    def __init__(self, command_file):
        self.command_file = command_file
        self.command_dict = self.CommandFileAsDict()
        self.command_info = self.command_dict["COMMAND_INFO"]
        self.total_command_no = self.command_info["TOTAL_COMMANDS"]
        # self.command_list = self.command_info["COMMAND_LIST"]
        self.command_names = self.command_info["COMMAND_NAMES"]
        self.command_info_with_name = self.command_info["COMMAND_NAMES_WITH_INFO"]

    def ExecuteClick(self,value):
        # if type(value)=="str":
        #     click_value = value.replace("(","")
        #     click_value = click_value.replace(")","")
        #     click_value = click_value.split(",")
        #     click_x = int(click_value[0])
        #     click_y = int(click_value[1])
        # else:
        click_x , click_y = value[0] , value[1]
        pyautogui.click(x=click_x , y=click_y)
        return

    def ExecuteImage(self,value):
        image_x , image_y = pyautogui.locateCenterOnScreen(value)
        return self.ExecuteClick([image_x,image_y])

    def ExecuteWrite(self,value):
        keyboard.write(value)
        return

    def ProcessCommand(self,command_type,command_value ,command_name):
        if command_type.upper()=="CLICK":
            self.ExecuteClick(command_value)
        elif command_type.upper()=="IMAGE":
            self.ExecuteImage(command_value)
        elif command_type.upper()=="WRITE":
            self.ExecuteWrite(command_value)
        else:
            raise Exception(f"INVALID COMMAND TYPE GOT AT FUNCTION ProcessCommand : {command_name} , {command_type}")
        return

    def ExecuteSingleCommand(self,command_name,command_in_sequence=False):
        if command_name in self.command_names:
            happening_command_info = self.command_info_with_name[command_name]
            happening_command_index = happening_command_info[0]
            happening_command_type = happening_command_info[1]
            happening_command_value = happening_command_info[-1]
            if command_in_sequence:
                valid_command_happening = self.command_names.index(command_name)==happening_command_index
                if not valid_command_happening:
                    raise Exception(f"ERROR AT ExecuteSingleCommand : command_name and associated index and happening index not equal\n command_name : {command_name}\n associatedIndex : {happening_command_index}\n happeningIndex : {self.command_names.index(command_name)}")
            return self.ProcessCommand(happening_command_type , happening_command_value , command_name)
        else:
            raise Exception(f"INVALID COMMAND_NAME AT FUNCTION ExecuteSingleCommand : {command_name}")
    
    def ExecuteAllCommands(self):
        for command_name in self.command_names:
            self.ExecuteSingleCommand(command_name , True)
        return

    def CommandFileAsDict(self):
        with open(self.command_file) as f:
            dict_command_file = json.load(f)
        return dict_command_file

    @classmethod
    def ReturnNeededKeys(cls):
        print(
            "1.) COMMAND_INFO\t ( MAIN KEY FROM WHERE PROGRAM STARTS READING )"
        )
        print("1.1) TOTAL_COMMANDS\t ( MUST BE AN INT )")
        print(
            "1.2) COMMAND_LIST\t [ x : x (str) is of the format:- commandName_executionType_commandValue ]"
        )
        print("1.3) COMMAND_NAMES\t [ x : x is commandName ]")
        print(
            "1.4) COMMAND_NAMES_WITH_INFO\t { x:y , x is commandName  y is [commandExecutionIndex , commandExecutionType , commandExecutionValue]}"
        )
        print("NOTE , IN KEYS 1.2 , 1.3 THE INDEX OF VALUES MUST BE ACCORDING TO THEIR EXECUTION_INDEX")
        print("EXECUTABLE COMMAND VALUE :-  A. CLICK   B. IMAGE   C. WRITE")

if __name__ == "__main__":
    testDrive = AutoRun("test.json")
    testDrive.ExecuteAllCommands()