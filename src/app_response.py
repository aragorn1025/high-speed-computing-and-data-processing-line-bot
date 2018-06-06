# import json
import sys
sys.path.append('./')
import instruction

def output(inputs):
        try:
                return instruction.get_instruction_response(inputs)
        except Exception as e:
                return 'Error:\n' + str(e)

def append_json(file_name = '../data/record.json', inputs):
        with open(file_name, mode = 'r', encoding='utf-8') as file_in:
                data = json.load(file_in)
        data.append(inputs)
        with open(file_name, mode = 'w', encoding='utf-8') as file_out:
                json.dump(data, file_out)
