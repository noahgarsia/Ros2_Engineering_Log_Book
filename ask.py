#!/usr/bin/env python3
"""
ask.py - Logbook Appender
Appends GPT-4o analysis to the bottom of the file instead of overwriting.
"""

import shutil
from datetime import datetime
from pathlib import Path
from openai import OpenAI

# ============================================================
# OPENAI CLIENT
# ============================================================

def get_client() -> OpenAI:
    return OpenAI()

def send_to_ai(prompt: str) -> str:
    client = get_client()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": "You are a technical auditor. Fill the template using ONLY the provided code. Do not hallucinate sensors."
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content

# ============================================================
# WORKSPACE & FILE DISCOVERY
# ============================================================

def find_ros2_workspace(workspace_name: str) -> Path:
    search_roots = [Path.home()]
    for root in search_roots:
        candidate = root / workspace_name
        if candidate.is_dir() and (candidate / "src").is_dir():
            return candidate
    raise FileNotFoundError(f"ROS 2 workspace '{workspace_name}' not found.")

def discover_files(workspace_path: Path) -> list[Path]:
    EXCLUDED = {".git", "build", "install", "log", "__pycache__", ".vscode"}
    files = []
    for path in workspace_path.rglob("*"):
        if path.is_dir() or any(p in EXCLUDED for p in path.parts):
            continue
        if path.suffix in {".py", ".cpp", ".hpp", ".h", ".md", ".yaml", ".xml"}:
            files.append(path)
    return files

# ============================================================
# LOGBOOK FILLER PROMPT
# ============================================================

def build_logbook_filler_prompt(target_log: str, file_contents: dict[str, str]) -> str:
    # FILTER: AI only sees 'src/' files to prevent hallucination
    src_evidence = {p: c for p, c in file_contents.items() if "src/" in p}
    today = datetime.now().strftime("%Y-%m-%d")
    
    evidence_text = ""
    for path, content in src_evidence.items():
        evidence_text += f"\n--- SOURCE CODE EVIDENCE: {path} ---\n{content}\n"

    prompt = (
        f"### TODAY'S DATE: {today}\n\n"
        f"TASK: Update logbook '{target_log}' using ONLY the source code evidence.\n"
        f"Replace 'YYYY-MM-DD' with {today}.\n\n"
        f"### SOURCE CODE EVIDENCE\n{evidence_text}\n"
        f"### TARGET LOGBOOK TEMPLATE\n{file_contents[target_log]}\n"
    )
    return prompt

# ============================================================
# MAIN
# ============================================================

def main():
    try:
        ws_name = input("Enter ROS 2 workspace name: ").strip()
        ws_path = find_ros2_workspace(ws_name)
        
        all_paths = discover_files(ws_path)
        file_contents = {str(p.relative_to(ws_path)): p.read_text(encoding="utf-8", errors="ignore") for p in all_paths}

        print("\n[1] Workspace Analysis\n[2] Fill Logbook (Append Mode)")
        choice = input("Select Mode: ").strip()

        if choice == "2":
            print("\nAvailable Files:")
            for p in file_contents.keys(): print(f" - {p}")
            
            target = input("\nWhich Logbook file are we filling? ").strip()
            if target not in file_contents:
                print("Error: File not found.")
                return

            prompt = build_logbook_filler_prompt(target, file_contents)
            
            print(f"\nProcessing with GPT-4o for: {target}...")
            result = send_to_ai(prompt)
            
            print("\n" + "="*20 + " GENERATED ENTRY " + "="*20)
            print(result)
            
            if input("\nAppend this to the logbook? (y/n): ").lower() == 'y':
                target_path = ws_path / target
                
                # --- APPEND LOGIC ---
                # 1. Split the result to clean up leading/trailing whitespace
                clean_result = result.strip()
                
                # 2. Open in append mode ('a')
                # 3. Add a blank line (\n\n) before the new entry
                with open(target_path, "a", encoding="utf-8") as f:
                    f.write("\n\n---\n") # Adds a horizontal separator
                    f.write(f"### Entry Added on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                    f.write(clean_result)
                
                print(f"Success. Entry appended to {target}")
        
        else:
            print("Analyzing workspace structure...")
            # Using line.split() logic here for titles if needed
            print(send_to_ai(f"Summary of files: {list(file_contents.keys())}"))

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()