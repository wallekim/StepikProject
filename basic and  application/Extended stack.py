import time


class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))


class LoggableList(Loggable, list):
    def append(self, msg):
        super(LoggableList, self).append(msg)
        Loggable.log(self, msg)


a = LoggableList()
a.append('msg1')
# a.append('msg2')
print(a)
