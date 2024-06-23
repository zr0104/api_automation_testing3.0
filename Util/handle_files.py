import os
import sys
import pytz
from Base.logger import MyLogging
log = MyLogging().logger
basePath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))
tempPath = "/tmp/auto_check_report/"


class HandleFiles():
    def delete_files(self, basePath):
        try:
            file_list = os.listdir(basePath)
            file_list = [f for f in file_list if not os.path.isdir(os.path.join(basePath, f))]
            file_list.sort(key=lambda f: os.path.getmtime(os.path.join(basePath, f)))
            keep_file = file_list[-5]
            print(file_list, keep_file)
            for file in file_list:
                if file <= keep_file:
                    os.remove(basePath + file)
                    log.info("delete {} file successfully!".format(file))
        except Exception as e:
            log.info(e)
            raise e


if __name__ == '__main__':
    handle_file = HandleFiles()
    filenameLog = os.path.join(basePath + "/logs/")
    filenameReport = os.path.join(basePath + "/Report/")
    print(filenameLog,filenameReport)
    handle_file.delete_files(filenameLog)
    handle_file.delete_files(filenameReport)

    handle_file.delete_files(tempPath)

