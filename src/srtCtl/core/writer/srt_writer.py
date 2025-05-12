from src.srtCtl.core.modules.SubtitleItem import SubtitleItem

class SrtWriter:
    def write(self, items, out_path):
        with open(out_path, 'w', encoding='utf-8') as f:
            for item in items:
                f.write(f"{item.index}\n")
                f.write(f"{item.start} --> {item.end}\n")
                f.write("\n".join(item.texts) + "\n\n")