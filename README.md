========
Aastra SIP Devices Discover
========

This is a Python Command Line Application that discover, from a pre introduced IP Range, all the Aastra SIP Devices and automatically download the "local.cfg" file and create the MAC.cfg file.

This Application is useful for medium and large Aastra SIP devices installation, where is necesary to get the local configuration from any specific device.

At the moment the setup.py is configured only for py2exe.


Getting Started
==========================

1. Install Python ( min 2.7 ) and all prerequisites

* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/)
* [python-iptools](https://github.com/bd808/python-iptools)
* [py2exe](http://www.py2exe.org/)

2. Generate the .exe file

```
python setup.py py2exe
```

3. Add the mac folder into the dist folder

4. That's All