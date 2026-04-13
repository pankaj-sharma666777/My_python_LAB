class RemoteControl():
    def__init__(self):
        self.channel = ["HBO","cnn","abc","espn"]
        self.inedx=-1


        def__iter__(self):
            return self


        def__next__(self):
            self.index += 1
            if self.index == len(self.channels):
                raise StopIteration
            return self.channels[self.index]

        r = RemoteControl()
        itr=iter(r)
        print(next(itr)
        print(next(itr)
        print(next(itr)      
            
