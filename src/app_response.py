import json
import os
import sys
sys.path.append('./')
import instruction

def output(inputs):
        try:
                listos = os.listdir() + '\n\n'
                head = 'json: ' + append_json(inputs = inputs) + '\n'
                return listos + head + instruction.get_instruction_response(inputs)
        except Exception as e:
                return 'Error:\n' + str(e)

def append_json(file_name = '../data/record.json', inputs = ''):
        with open(file_name, mode = 'r', encoding='utf-8') as file_in:
                data = json.load(file_in)
        data.append(inputs)
        with open(file_name, mode = 'w', encoding='utf-8') as file_out:
                json.dump(data, file_out)
        with open(file_name, mode = 'r', encoding='utf-8') as file_in:
                return json.load(file_in)
