import sys
sys.path.append('./')
import instruction

def output(inputs):
        try:
                return instruction.get_instruction_response(inputs)
        except Exception as e:
                return 'Error:\n' + str(e)
