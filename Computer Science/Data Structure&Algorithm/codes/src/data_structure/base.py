from abc import ABC, abstractmethod


class DataStructureTemplate(ABC):

    @abstractmethod
    def clear(self):
        raise NotImplementedError("base.py-DataStructureTemplate/Abstract method clear is not implemented in base class.")