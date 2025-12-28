from datetime import datetime

def taimestamp():
    current_time = datetime.now()
    return current_time.strftime("%H:%S, %d.%m.%Y")

def print_message(message:str):
    print('\n ┌' + '-'*(len(message) +2) + '┐')
    print(f' | {message} |')
    print(' └' + '-'*(len(message) +2) + '┘')


def on_start():
    msg = f'Bot started at {taimestamp()}'
    print_message(msg)

def on_shutdown():
    msg = f'Bot is down at {taimestamp()}'
    print_message(msg)