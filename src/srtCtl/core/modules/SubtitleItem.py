from typing import List

class SubtitleItem:
    def __init__(self, index: int, start: str, end: str, texts: List[str]):
        self.index = index
        self.start = start
        self.end = end
        self.texts = texts
        
    # 宠溺定义如何组织成srt的形式，如用于print
    def __str__(self):
        return f"{self.index}\n{self.start} --> {self.end}\n" + "\n".join(self.texts)