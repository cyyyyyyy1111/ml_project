import pysrt
from src.srtCtl.core.modules.SubtitleItem import SubtitleItem

class SrtParser:
    def parse(self, path):
        try:
            subs = pysrt.open(path, encoding='utf-8')
        except Exception as e:
            raise ValueError(f"Failed to parse SRT file: {e}")
        
        items = [
            SubtitleItem(
                index=sub.index,
                start=str(sub.start),
                end=str(sub.end),
                texts=sub.text.splitlines()
            ) for sub in subs
        ] # 原始数据
        
        length = len(items) # 字幕条数
        
        texts = [item.texts for item in items] # 去重前的字幕，二维列表，texts[i]是第i条字幕的文本，是2行
        
        texts_deduplicated = [] # 去重后的字幕，不包括空行，一维列表
        for lines in texts:
            for line in lines:
                text = line.strip()
                if not text:
                    continue # 空行不记录
                latest_text = texts_deduplicated[-1] if texts_deduplicated else None
                if latest_text != text:
                    texts_deduplicated.append(text)
                
        return items, length, texts, texts_deduplicated