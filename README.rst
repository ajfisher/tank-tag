Introduction
=============

`Tank Tag`_ is a game that was designed as a proof of concept to work as a demonstration for a talk I gave at `Web Directions`_, What do you Know on how to use the mobile Device APIs. Since then the concept has evolved and saw another outing at Web Directions south with nearly 100 players involved on the big screen before the network melted through sheer weight of traffic.

Here's a `screencast of the game`_ in action during the presentation.

While related to the work in `django-arduino-socketio`_ this project is sufficient standalone to warrant its own repo and there were people interested in it beyond the arduino elements (controlling servos / lights etc via mobile phone).

Installation
============

Dependencies
------------

Install the following components:

    * `Python`_ (min 2.5)
    * `Django`_ 1.3
    * `django-socketio`_

Each of these should install with a simple:
    
    easy_install django
    
or:

    pip install django
    
etc and it should just work.

Set up
------

Once the dependencies are met, download or take a copy of the Tank Tag repo and you'll need to run up a test database:

    > python manage.py syncdb

After that you should be able to run the game from the command line with a simple:

    > python manage.py runserver_socketio IP:address
    
Where IP and address are where you want to broadcast the game. For testing you can use 127.0.0.1 but you'll have to use your broadcast IP to get to it over the network.

Hit http://<ip>/tanks/game to get the game screen up. If you have a screen with leader board and no of player: 0 then it should be working. You can review the error messages and your log otherwise.

Playing
========
    
There are two components to the game, the play screen for the visualisation and the controller screen for the mobile devices.

To house a game point a modern web browser at: http://<IP>/tanks/game - show this on whatever screen you want to be the game area (computer, TV - 80 ft projection wall - whatever you can get access to!)

Get a mobile device (iOS devices are known to work, Android phones work with Firefox, Android tablets will work with the stock Android browser - untested on Nokias, WP7 etc - if you do let me know!) and point it's web browser at http://<IP>/

You will be asked to create a user account (no password - one off user account only) and then you'll be dropped randomly on the play field.

To control your tank hold your phone in landscape mode, then tilt the phone left and right like you're driving a car. To speed up or slow down tilt forward and back and to fire hit the big fire button.

Get Involved
=============

If you want to fork the game and enhance it then please do, issues will be managed via `the project`_ at github. And if you do something interesting with it, shoot me a link / photos / video at `@ajfisher`_ on twitter.

.. _`@ajfisher`: http://twitter.com/ajfisher
.. _`Django`: http://djangoproject.com/
.. _`django-arduino-socketio`: https://github.com/ajfisher/django-arduino-socketio
.. _`django-socketio`: https://github.com/stephenmcd/django-socketio
.. _`screencast of the game`: http://youtu.be/h86K3wBycLA?t=4m29s
.. _`tank tag`: https://github.com/ajfisher/tank-tag
.. _`the project`: https://github.com/ajfisher/tank-tag
.. _`python`: http://www.python.org
.. _`Web Directions`: http://www.webdirections.org
