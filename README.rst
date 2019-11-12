weeread
=======

If you ever wanted a nice frontend to read through your old weechat logs, this
is it!

Installation
------------

Clone the project using the following commands:

::

    $ git clone https://github.com/RJ722/weeread
    $ cd weeread

Install the required package (preferably inside a virtual environment) using
`pip3`:

::

    $ pip3 install -r requirements.txt

Edit the `PATH` variable in `server.py` pointing towards the directory which
contains all your weechat logs (defaults to `'~/.weechat/logs/'`).

Finally, run the server:

::

    $ python3 server.py


Open `localhost:5000 <http://localhost:5000/>`_