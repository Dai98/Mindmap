from abc import ABC, abstractmethod


class DataStructureTemplate(ABC):
    """
        This class is the abstract parent class of all data structure classes
        Here defines the methods that must be implemented by all data structures
    """

    @abstractmethod
    def clear(self):
        raise NotImplementedError("base.py-DataStructureTemplate/Abstract method clear is not implemented in base class.")