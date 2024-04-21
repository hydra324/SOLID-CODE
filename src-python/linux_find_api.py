from abc import ABC, abstractmethod
from typing import List
from enum import Enum
class Type(Enum):
    FILE = 0
    DIRECTORY = 1
    SIMLINK = 2
class IFileNode:
    def __init__(self,name:str,size:int, fileType:Type) -> None:
        self.name = name
        self.size = size
        self.fileType = fileType


    def get_name(self) -> str:
        return self.name
    
    def get_size(self):
        return self.size

    def __repr__(self):
        return f"{self.fileType}({self.name})"

class File(IFileNode):
    def __init__(self,name:str,size: int, extension: str) -> None:
        self.extension = extension
        super().__init__(name,size,fileType = Type.FILE)


class Directory(IFileNode):
    def __init__(self,name:str,children: List[IFileNode] = [],size: int = 0) -> None:
        # create a new instance of IFileNode and set the fileType to directory
        super().__init__(name,size,Type.DIRECTORY)
        self.children = children

    def add_child(self,child: IFileNode):
        self.children.append(child)
        self.size += child.get_size()
    
    def remove_child(self,child: IFileNode):
        # validation
        if child not in self.children:
            raise ValueError("Child not found!")
        self.children.remove(child)
        self.size -= child.get_size()

    def get_children(self):
        return self.children



class ICritera(ABC):
    @abstractmethod
    def apply(self,file):
        pass

class FileNameCriteria(ICritera):
    def __init__(self,target_filename:str) -> None:
        self.target_filename = target_filename
        super().__init__()

    # override
    def apply(self, file: IFileNode):
        return file.get_name() == self.target_filename
    
class GreaterThanSizeCriteria(ICritera):
    def __init__(self,target_size:int) -> None:
        super().__init__()
        self.target_size = target_size
    # override
    def apply(self, file: IFileNode):
        return file.get_size() >= self.target_size

class DefaultCriteria(ICritera):
    def apply(self,file):
        return True
    
class ANDCriteria(ICritera):
    def __init__(self,criteria1: ICritera, criteria2: ICritera) -> None:
        self.criteria1 = criteria1
        self.criteria2 = criteria2
    def apply(self,file: IFileNode) -> bool:
        return self.criteria1.apply(file) and self.criteria2.apply(file)
    
class ORCriteria(ICritera):
    def __init__(self,criteria1: ICritera, criteria2: ICritera) -> None:
        self.criteria1 = criteria1
        self.criteria2 = criteria2
    def apply(self,file: IFileNode) -> bool:
        return self.criteria1.apply(file) or self.criteria2.apply(file)

class BuildCriteria:
    def __init__(self) -> None:
        self.build_criteria: ICritera = DefaultCriteria()

    def and_op(self,criteria:ICritera):
        self.build_criteria = ANDCriteria(self.build_criteria,criteria)
        return self
    
    def or_op(self,criteria: ICritera):
        self.build_criteria = ORCriteria(self.build_criteria,criteria)
        return self
    
    def build(self):
        return self.build_criteria


class FindLibrary:
    def findAPI(self,root: IFileNode, criteria: ICritera):
        result = []
        self.find_helper(root,criteria,result)
        return result
        

    def find_helper(self,root:IFileNode,criteria:ICritera,result: List[IFileNode]):
        if root.fileType==Type.FILE:
            result += [root] if criteria.apply(root) else []
            return
        for child in root.get_children():
            self.find_helper(child,criteria,result)
            

if __name__ == "__main__":
    dir1 = Directory('dir1')
    file1 = File('file1',100,'pdf')
    file2 = File('file2',20,'xml')
    dir1.add_child(file1)
    dir1.add_child(file2)
    root = Directory('/',children=[])
    root.add_child(dir1)

    criteria = BuildCriteria() \
                    .and_op(FileNameCriteria(target_filename="file2"))\
                    .and_op(GreaterThanSizeCriteria(target_size=50))\
                    .build()
    lib = FindLibrary()
    print(lib.findAPI(root,criteria))

        