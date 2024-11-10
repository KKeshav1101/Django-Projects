class MyError1(Exception):
    def __init__(self,message="Text Box Error"):
        self.message=message
        super().__init__(self.message)
