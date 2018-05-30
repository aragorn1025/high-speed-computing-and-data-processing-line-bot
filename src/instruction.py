import requests
from bs4 import BeautifulSoup

BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100'

__instructions = {
        'help': ['幫助', '說明', 'Help'],
        'top_song': ['推薦', 'TopSong', 'TopSong10'],
        'listen': ['試聽', 'Listen'],
        'best_creator': ['最佳歌手', 'BestCreator', 'BestCreator5'],
        'like': ['讚', 'Like'],
        'report': ['回報', 'Report'],
        'suggest': ['建議', 'Suggest']
}

# __show_all_instructions = '所有指令：\n\t幫助\n\t推薦\n\t試聽\n\t最佳歌手\n\t讚\n\t回報\n\t建議\n\n查看指令規則，請輸入：\n\t幫助 [指令]\n\t例如：幫助 推薦'
__show_all_instructions = '所有指令：\n\t幫助\n\t推薦\n\t試聽\n\n查看指令規則，請輸入：\n\t幫助 [指令]\n\t例如：幫助 推薦'
__show_error_prefix = '指令格式錯誤！\n\n'
__show_help = {
        'help': '列出所有指令，請輸入：\n\t幫助\n\n查看指令規則，請輸入：\n\t幫助 [指令]\n\t例如：幫助 推薦',
        'top_song': '列出推薦的西洋歌曲，請輸入：\n\t推薦',
        'listen': '試聽排行榜上歌曲，請輸入：\n\t試聽 推薦 [排行序]\n\t例如：試聽 推薦 8',
        'best_creator': '設計中',
        'like': '設計中',
        'report': '設計中',
        'suggest': '設計中'
}

def get_instruction_response(inputs):
        tokens = inputs.split(' ')
        instruction = get_instruction(tokens[0])
        if instruction == 'help':
                if len(tokens) == 1:
                        return __show_all_instructions
                if len(tokens) == 2:
                        sub_instruction = get_instruction(tokens[1])
                        if sub_instruction != None:
                                return __show_help[sub_instruction]
        if instruction == 'top_song':
                if len(tokens) == 1:
                        return get_top_songs_response()
        if instruction == 'listen':
                if len(tokens) == 3:
                        sub_instruction = get_instruction(tokens[1])
                        _id = get_integer(tokens[2])
                        if sub_instruction == 'top_song' and _id in range(1, 10 + 1):
                                return get_listen_response(_id)
        if instruction == 'best_creator':
                return '設計中'
        if instruction == 'like':
                return '設計中'
        if instruction == 'report':
                return '設計中'
        if instruction == 'suggest':
                return '設計中'
        if instruction == None:
                return __show_error_prefix + __show_all_instructions
        return __show_error_prefix + __show_help[instruction]

def get_instruction(first_token):
        for key in __instructions.keys():
                if first_token in __instructions[key]:
                        return key
                if first_token == key:
                        return key
        return None

def get_top_songs_response():
        top_songs = get_top_songs()
        s = ''
        for i in range(0, 10):
                s += '{:02}) {}\n'.format(i + 1, top_songs[i])
        return s[:-1]

def get_listen_response(_id):
        song = get_top_songs()[_id - 1]
        return '試聽 {song} ：\nhttps://www.youtube.com/results?search_query={keyword}'.format(song = song, keyword = song.replace(" ", "+"))

def get_top_songs():
        response = requests.get(BILLBOARD_URL)
        soup = BeautifulSoup(response.text)
        returned_list = []
        for item in soup.select('.chart-row__song'):
                returned_list.append(item.text)
        return returned_list

def get_top_songs_creators():
        response = requests.get(BILLBOARD_URL)
        soup = BeautifulSoup(response.text)
        returned_list = []
        for (i, item) in enumerate(soup.select('.chart-row__artist')):
                returned_list.append(item.text.replace('\n', '').replace(' & ', ', ').split(', '))
        return returned_list

def get_integer(s):
    try: 
        return int(s)
    except ValueError:
        return None
