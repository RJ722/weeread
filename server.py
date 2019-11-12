from collections import namedtuple
import os
from pathlib import Path

from flask import abort, Flask, render_template
from flask_common import Common

app = Flask(__name__)
common = Common(app)

PATH = Path.home()/'.weechat/logs' # WIP: Make PATH configurable.
p = Path(PATH)
Message = namedtuple('Message', ['timestamp', 'author', 'text'])
chart = {}
num = 0

class Chat(object):
    def __init__(self, filepath, slug):
        self.filepath = filepath
        self.slug = slug
    
    @property
    def messages(self):
        msgs = []
        with open(self.filepath) as f:
            lines = f.readlines()

        for line in lines:
            broken_message = line.split()
            author = broken_message[2]
            if author in ('<--', '-->', '--', '=!=', '***'):
                continue
            timestamp = ' '.join(broken_message[:2])
            text = ' '.join(broken_message[3:])
            msgs.append(Message(timestamp, author, text))
        return msgs
    
    @property
    def title(self):
        return self.filepath.stem


@app.route('/')
def index():
    return render_template('index.html', chats=list(chart.values()))


@app.route('/chat/<slug>')
def show_chat(slug):
    try:
        chat = chart[int(slug)]
        return render_template('chat.html', chat=chat)
    except (KeyError, ValueError):
        return 'Oops, that chat does not exist! :-)'
    except IOError:
        abort(404)

if __name__ == '__main__':
    for f in sorted(list(p.iterdir()), key=os.path.getctime):
        if f.suffix == '.weechatlog':
            chart[num] = Chat(f.absolute(), slug=num)
            num += 1

    app.debug = True
    common.serve()
