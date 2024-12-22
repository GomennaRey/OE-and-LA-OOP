from abc import ABC, abstractmethod

class Character(ABC):
    @property   
    @abstractmethod
    def __init__(self, name):
        pass
        
    
class Superman(Character):
    def __init__(self, name, alias):
        self.name = name
        self.__alias = alias
      
    @property
    def alias(self):
        return self.__alias
    
Superman = Superman("Clark Kent", "Superman")
print(Superman.alias)
