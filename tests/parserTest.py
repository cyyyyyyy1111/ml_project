import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.srtCtl.core.parser.srt_parser import SrtParser

def test_parse_first_srt_file():
    # 在工作目录下的 srt-files 目录中选取第一个 .srt 文件
    base = os.getcwd()
    srt_dir = os.path.join(base, "srt-files")
    srt_files = [f for f in os.listdir(srt_dir) if f.lower().endswith(".srt")]
    assert srt_files, "srt-files 文件夹中没有 .srt 文件可供测试"
    srt_path = os.path.join(srt_dir, srt_files[0])

    parser = SrtParser()
    items, length, texts, dedup = parser.parse(srt_path)
    
    print(f"去重去空后的字幕列表: {dedup}")

    # 基本类型检查
    assert isinstance(items, list)
    assert isinstance(length, int) and length == len(items)
    assert isinstance(texts, list)
    assert isinstance(dedup, list)

    # 每个 item 应该有 index、start、end、texts 四个属性
    for itm in items:
        assert hasattr(itm, "index")
        assert hasattr(itm, "start")
        assert hasattr(itm, "end")
        assert hasattr(itm, "texts")
        assert isinstance(itm.texts, list)

    # dedup 中不应包含空字符串，且数量不超过总行数
    assert all(isinstance(t, str) and t.strip() for t in dedup)
    assert len(dedup) <= sum(len(lines) for lines in texts)
    
if __name__ == "__main__":
    test_parse_first_srt_file()