import requests
import sys
sys.path.append('./')
import instruction

def output(user_id, inputs):
        try:
                # sql_insert(user_id, inputs, url = 'http://***.***.***.***/aragorn/index.php')
                return instruction.get_instruction_response(inputs)
        except Exception as e:
                return 'Error:\n' + str(e)

def sql_insert(user_id, inputs, url):
        response = requests.get('{}?user_id={}&record={}'.format(url, user_id, inputs.replace('\n', ' ').replace('\r', ' ').replace('\'', '\\\'').replace('\"', '\\\"')))
