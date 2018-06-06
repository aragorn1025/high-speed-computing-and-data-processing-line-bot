import json
import sys
sys.path.append('./')
import instruction

def output(user_id, inputs):
        try:
                if user_id = 'Ufb68b93dd139ad3ed7a318305a15b281' and inputs = 'json':
                        return append_json(user_id, inputs, to_return = True)
                return instruction.get_instruction_response(inputs)
        except Exception as e:
                return 'Error:\n' + str(e)

def append_json(user_id, inputs, file_name = './data/record.json', to_return = False):
        with open(file_name, mode = 'r', encoding='utf-8') as file_in:
                data = json.load(file_in)
        data.append({'user': user_id, 'text': inputs})
        with open(file_name, mode = 'w', encoding='utf-8') as file_out:
                json.dump(data, file_out)
        if to_return:
                with open(file_name, mode = 'r', encoding='utf-8') as file_in:
                        return json.load(file_in)
