from distutils.core import setup
import py2exe

setup(
    console=['discover.py'],
    name='aastra-phone-discover',
    options = {"py2exe": {"skip_archive":1}},
    version='0.0.1',
    packages=['aastra'],
    url='',
    license='GPL',
    author='Andrea Mucci aKa ogonbat',
    author_email='cingusoft@gmail.com',
    description=''
)
