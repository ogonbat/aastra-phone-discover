import os
import re
from BeautifulSoup import BeautifulSoup

__author__ = 'amucci'
import urllib2, base64
from uuid import getnode as get_mac

class Aastra_Check(object):
    timeout = 5
    mac = ""

    def __init__(self,ip_addr, username, password):
        self.ip = ip_addr
        self.username = username
        self.password = password

    def set_timeout(self, timeout):
        self.timeout = timeout

    def check(self):
        request = urllib2.Request("http://%s/sysinfo.html"%(self.ip))
        base64string = base64.standard_b64encode('%s:%s' % (self.username, self.password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        try:
            result = urllib2.urlopen(request, timeout=self.timeout)
            data = result.read()
            tree = BeautifulSoup(data)
            node = tree.find(text=re.compile(r'^([0-9A-F]{2}[:-]){5}([0-9A-F]{2})$'))
            self.mac = node.replace("-", "")
            return True
        except urllib2.URLError:
            return False

    def get_local_file(self):
        request = urllib2.Request("http://%s/localcfg.html"%(self.ip))
        base64string = base64.standard_b64encode('%s:%s' % (self.username, self.password)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        try:
            result = urllib2.urlopen(request, timeout=self.timeout)
            data = result.read()
            path = os.path.dirname(os.path.abspath(__file__))
            file = os.path.join(path,'..', 'mac', '%s.cfg'%self.mac)
            with open(file, "wb") as code:
                code.write(data)
        except urllib2.URLError:
            return False