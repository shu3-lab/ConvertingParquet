from abc import ABCMeta,abstractmethod

class abstract_S3(metaclass=ABCMeta):
    
    @abstractmethod
    def from_S3(self,bucketname,filename):
        pass

    @abstractmethod
    def to_S3(self,bucketname,filename):
        pass
