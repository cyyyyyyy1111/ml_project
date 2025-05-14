import typer
from pathlib import Path
import pysrt

from src.srtCtl.rule_based import RuleBasedCorrector

app = typer.Typer(help="SRT字幕优化工具")

@app.command()
def correct_srt(
    input_file: str = typer.Option(..., help="输入SRT文件路径"),
    output_file: str = typer.Option(..., help="输出SRT文件路径"),
    show_diff: bool = typer.Option(False, "--diff", help="生成差异对比文件")
):
    """自动修正SRT字幕文件的语法和拼写错误"""
    subs = pysrt.open(input_file)
    corrector = RuleBasedCorrector()
    diff_log = []
    
    for sub in subs:
        original = sub.text
        corrected, changes = corrector.correct_text(original)
        sub.text = corrected
        
        if changes and show_diff:
            diff_log.append(f"Line {sub.index}:")
            diff_log.append(f"  - Original: {original}")
            diff_log.append(f"  + Corrected: {corrected}")
    
    subs.save(output_file)
    typer.echo(f"Corrected subtitle saved to {output_file}")
    
    if show_diff:
        diff_path = Path(output_file).with_suffix(".diff.txt")
        diff_path.write_text("\n".join(diff_log))
        typer.echo(f"Difference saved to {diff_path}")

if __name__ == "__main__":
    app()
