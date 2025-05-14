import language_tool_python
import spacy
from typing import Tuple, List, Dict

class RuleBasedCorrector:
    def __init__(self):
        # 初始化LanguageTool（英文规则库）
        self.tool = language_tool_python.LanguageTool('en-US')
        # 初始化spaCy管道
        self.nlp = spacy.load("en_core_web_sm")

    def correct_text(self, text: str) -> Tuple[str, List[Dict]]:
        """修正文本并返回修改记录"""
        # 1. 用LanguageTool检查语法和拼写
        matches = self.tool.check(text)
        corrected_text = language_tool_python.utils.correct(text, matches)
        
        # 2. 用spaCy处理标点（如修复缺失的句号）
        doc = self.nlp(corrected_text)
        corrected_text = self._fix_punctuation(doc)
        
        # 3. 生成修改记录（用于diff输出）
        changes = []
        for match in matches:
            changes.append({
                'offset': match.offset,
                'error': text[match.offset:match.offset + match.errorLength],
                'correction': match.replacements[0] if match.replacements else '',
                'rule': match.ruleId
            })
        
        return corrected_text, changes

    def _fix_punctuation(self, doc) -> str:
        """修复标点（如句尾缺失句号）"""
        sentences = [sent.text.strip() for sent in doc.sents]
        corrected = []
        for sent in sentences:
            if sent and not sent[-1] in {'.', '!', '?'}:
                sent += '.'  # 自动补句号
            corrected.append(sent)
        return ' '.join(corrected)
