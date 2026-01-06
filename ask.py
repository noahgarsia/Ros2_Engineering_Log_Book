#!/usr/bin/env python3
"""
ask.py - Logbook Appender
Appends GPT-4o analysis to the bottom of the file instead of overwriting.
"""

import shutil
from datetime import datetime
from pathlib import Path
from openai import OpenAI
from typing import Optional

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
                "content": "You are a technical auditor. Fill the template using ONLY the provided code. Do not hallucinate."
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

def locate_readme(target_path: str) -> Optional[str]:
    parts = target_path.split("/")

    valid_headers = {
        "control",
        "simulation",
        "perception",
        "demonstrations",
        "planning",
    }

    for i, part in enumerate(parts):
        if part in valid_headers:
            return "/".join(parts[: i + 1]) + "/README.md"

    return None


def build_logbook_filler_prompt(
    target_log: str,
    file_contents: dict[str, str],
    extra_information: str | None = None,
    locate_readme_path: Optional[str] = None,
) -> str:

    if not isinstance(file_contents, dict):
        raise TypeError(
            f"file_contents must be dict[str, str], got {type(file_contents)}"
        )

    # FILTER: AI only sees 'src/' files to prevent hallucination
    src_evidence = {p: c for p, c in file_contents.items() if "src/" in p}
    today = datetime.now().strftime("%Y-%m-%d")

    evidence_text = ""
    for path, content in src_evidence.items():
        evidence_text += f"\n--- SOURCE CODE EVIDENCE: {path} ---\n{content}\n"

    extra_section = ""
    if extra_information:
        extra_section = (
            "\n### USER-PROVIDED CONTEXT (NON-CODE)\n"
            f"{extra_information.strip()}\n"
        )

    readme_section = ""
    if locate_readme_path:
        readme_section = (
            f"\n### LOGBOOK HEADER AUTHORITY ({locate_readme_path})\n"
            f"{file_contents.get(locate_readme_path, '')}\n"
        )

    prompt = (
        f"### OUTPUT FORMAT (MANDATORY)\n"
        f"Your response MUST begin with a title in the following format:\n\n"
        f"## <Short Descriptive Title>\n\n"
        f"The title must summarise the work completed in this entry.\n\n"
        f"### TODAY'S DATE: {today}\n\n"
        f"TASK: Update logbook '{target_log}' using ONLY the source code evidence.\n"
        f"Replace 'YYYY-MM-DD' with {today}.\n\n"
        f"{readme_section}"
        f"### SOURCE CODE EVIDENCE\n{evidence_text}\n"
        f"{extra_section}"
        f"### TARGET LOGBOOK TEMPLATE\n{file_contents[target_log]}\n"
    )

    return prompt

# ============================================================
# MAIN
# ==========================================================
from datetime import datetime

def main():
    try:
        while True:
            ws_name = input("Enter ROS 2 workspace name: ").strip()
            ws_path = find_ros2_workspace(ws_name)

            all_paths = discover_files(ws_path)
            file_contents = {
                str(p.relative_to(ws_path)): p.read_text(encoding="utf-8", errors="ignore")
                for p in all_paths
            }

            print("\n[1] Workspace Analysis\n[2] Fill Logbook (Append Mode)")
            choice = input("Select Mode: ").strip()

            if choice == "2":
                print("\nAvailable Files:")
                for p in file_contents.keys():
                    print(f" - {p}")

                target = input("\nWhich Logbook file are we filling? ").strip()
                if target not in file_contents:
                    print("Error: File not found.")
                    continue  # 🔧 don't exit whole program

                locate_readme_path = locate_readme(target)
                print(f"Located README for context: {locate_readme_path}")

                extra_information = input(
                    "Any extra information to include? (optional): "
                ).strip()

                prompt = build_logbook_filler_prompt(
                    target,
                    file_contents,
                    extra_information,
                    locate_readme_path
                )

                print(f"\nProcessing with GPT-4o for: {target}...")
                result = send_to_ai(prompt)

                print("\n" + "=" * 20 + " GENERATED ENTRY " + "=" * 20)
                print(result)

                if input("\nAppend this to the logbook? (y/n): ").lower() == "y":
                    target_path = ws_path / target
                    clean_result = result.strip()

                    with open(target_path, "a", encoding="utf-8") as f:
                        f.write("\n\n---\n")
                        f.write(
                            f"### Entry Added on "
                            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
                        )
                        f.write(clean_result)

                    print(f"Success. Entry appended to {target}")

            elif choice == "1":
                print("Analyzing workspace structure...")
                print(send_to_ai(f"Summary of files: {list(file_contents.keys())}"))

            else:
                print("Invalid choice.")

            # 🔧 FIXED: comparison, quotes, and logic
            another_analysis = input("\nProcess another workspace? (y/n): ").lower()
            if another_analysis != "y":
                break

    except Exception as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
