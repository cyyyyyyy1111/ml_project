[中文版](./CDCF&Techs_ZH.md)，[English version](./CDCF&Techs_EN)

---

# CdCF and Techs

## SRT File Optimization

### 1. Objective

To automatically improve the quality of English subtitle (SRT) files downloaded from YouTube, which are often auto-generated and error-prone. This optimization will enhance grammar, fix misrecognized words, and improve overall subtitle clarity and readability.

The result of this project will be a python package, Installable via pip (`pip install srtCtl`) and used as a command or lib. Professional, reusable, versioned!

### 2. Input

- `.srt` subtitle files in English, downloaded from YouTube (e.g. via `yt-dlp`)
- Optional: associated video metadata (title, description, etc.) for context-aware correction
- Users are allowed to choose witch mode to use, for ex., if it will generate the diff file; And maybe there will be multiple models witch users can choose.

### 3. 📤 Output

- `filename.corrected.srt`: a version of the subtitle file with improved English text
- `filename.diff.txt`: a line-by-line "diff" showing the changes from the original

### 4. ✅ Functional Requirements

- Detect issues in the subtitle text such as:
  - Grammar mistakes
  - Punctuation errors
  - Word misuse (e.g. "foreign" used inappropriately)
  - Repetition or misaligned fragments from speech-to-text
- Log each detected issue with:
  - Line number
  - Original text
  - Problem type

- Compare original and corrected subtitles line-by-line and generate a `.diff.txt` showing:

  - Original line
  - Corrected line

- Batch Processing

  - Process multiple SRT files in a directory

  - Preserve original files

  - Output corrected and diff files to a defined output folder

### 5. Constraints

- All tools and scripts must be written in Python
- System must run on a typical development laptop or optionally use local GPU
- Prefer offline models for portability; fallback to API only when necessary

## Technical Selection

To meet the project’s goals of optimizing auto-generated YouTube subtitles (SRT files) **without relying on black-box APIs**, we propose a modular, local, and CPU-friendly solution. The system will use **open-source language models**, **rule-based detection**, and **custom logic** to identify and correct subtitle errors while keeping the code transparent and extendable.

We will explore and benchmark multiple **open-source pre-trained language models** from Hugging Face (e.g., Qwen2.5-1.8B, Mistral-7B, TinyLLaMA). These models will be tested for subtitle correction performance under real conditions. For each model, we will evaluate correction accuracy, speed, and CPU compatibility. Based on this, we will recommend the most appropriate model depending on the user's computing environment.

If time and resources permit, we may create a **small training dataset** (e.g., 100 manually corrected subtitles) to perform **light fine-tuning** using LoRA, and then apply **quantization** to make the model deployable on low-resource machines.

The final deliverable will be a **pip-installable Python CLI package** that supports both batch and single-file processing, and produces corrected subtitles and diff logs. All models used will run locally, and optional quantization ensures the system is usable on typical laptops or developer machines without a GPU.

### Potential Models to Evaluate

- Different LLM Models and the fine-tuned LoRA model

### Tools & Libraries

#### Language Model Inference

- `transformers` (Hugging Face)
- `accelerate`, `auto-gptq`, `gguf` for quantization support

#### Subtitle Handling

- `pysrt`, `srt` – parse and manipulate `.srt` files
- `ffmpeg` extract metadata or audio if extended

#### Rule-based Correction Support

- `spaCy` – part-of-speech and syntax checks
- `LanguageTool` (offline server version) – lightweight grammar checking

#### CLI and Packaging

- `typer` – CLI interface
- `setuptools`, `pyproject.toml` – packaging
- `tqdm`, `logging` – progress and debugging tools

#### Diff Generation

- `difflib` – native Python diff
- `deepdiff` – structured diff (optional)

### Model Evaluation Plan

| Metric             | Description                                          |
| ------------------ | ---------------------------------------------------- |
| **Accuracy**       | Does the output fix errors while preserving meaning? |
| **Fluency**        | Are sentences grammatically and naturally rewritten? |
| **Speed**          | How fast does each model run per SRT file?           |
| **Resource usage** | Can it run smoothly on CPU with 8–16 GB RAM?         |
| **Diff clarity**   | Are the corrections transparent and explainable?     |

We will test models using the same set of SRT files, and recommend different models based on user context (e.g., low RAM, need for speed, best quality).