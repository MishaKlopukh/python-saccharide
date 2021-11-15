from functools import update_wrappers

def FuncNotImplemented(*args, **kwargs):
    raise NotImplementedError

def NoopStub(*args, **kwargs):
    ...

def PassStub(*args, **kwargs):
    if len(args)==1:
        return args[0]
    else:
        return args

class StubWrapper():
    def __init__(self,func):
        self.func = func
        update_wrappers(self,func)
    def __call__(self,*args,**kwargs):
        ...

class PrintStub(StubWrapper):
    def __call__(self,*args,**kwargs):
        print(f"Stub function {self.__qualname__} called"
              f"with arguments: {args}, {kwargs}")`

class ErrorStub(StubWrapper):
    def __call__(self,*args,**kwargs):
        raise NotImplementedError(
                f"{self.__qualname__} is a stub")
