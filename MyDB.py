class MyDB:
    def __init__(self):
        self.connection = Connection()
    def connect(self, connection_string):
        return self,self.connection

class Connection:
    def __init__(self):
        self.cur = cursor()  
    
    def __init__(self):
        return self.cur
    
    def close(self):
        pass


class cursor():
    def execute(self, query):
        if query == "select id from employee_db where name=John":
            return 123
        elif query == "select id from employee_db where name=Tom":
            return 789
        else:
            return -1
        def close(self):
            pass    