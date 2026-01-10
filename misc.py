from datetime import datetime

def timestamp():
    current_time = datetime.now()
    return current_time.strftime("%H:%M:%S, %d.%m.%Y")

def print_message(message:str):
    print('\n ┌' + '-'*(len(message) +2) + '┐')
    print(f' | {message} |')
    print(' └' + '-'*(len(message) +2) + '┘\n')


def on_start():
    msg = f'Bot started at {timestamp()}'
    print_message(msg)

def on_shutdown():
    msg = f'Bot is down at {timestamp()}'
    print_message(msg)