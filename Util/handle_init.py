#coding=utf-8
import sys
import os
import configparser
base_path = os.path.abspath(os.path.join(os.path.dirname(__file__),"../"))
sys.path.append(base_path)
class HandleInit:

    def load_ini(self):
        file_path = base_path+"/Config/config.json"
        cf = configparser.ConfigParser()
        cf.read(file_path,encoding="utf-8-sig")
        #data =cf.get('server','host')
        #print(data)
        return cf

    def get_value(self,key,node=None):
        '''
        获取ini里面的value(section=node)
        '''
        if node == None:
            node = 'server'
        cf = self.load_ini()
        try:
            data = cf.get(node,key)
        except Exception:
            print("没有获取到值")
            data=None
        return data

handle_ini = HandleInit()
if __name__ == '__main__':
    hi = HandleInit()
    print(hi.get_value("host"))