import shutil
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]
RAW_DIR = BASE_DIR / "source" / "Agent Skills_Day_3_images_raw"
FIGURE_DIR = BASE_DIR / "source" / "Agent Skills_Day_3_images"


FIGURES = {
    "picture-012.png": "Figure 1 Skill Failure Modes.png",
    "picture-014.png": "Figure 2 Skill Trigger Gatekeeping.png",
    "picture-016.png": "Figure 3 Evaluation-Driven Development Loop.png",
    "picture-018.png": "Figure 4 Co-loaded Skills Performance Gap.png",
    "picture-020.png": "Figure 5 Agents CLI Install Flow.png",
    "picture-022.png": "Figure 6 Demo-to-Deploy Gap.png",
    "picture-024.png": "Figure 7 Context Rot in Practice.png",
    "picture-026.png": "Figure 8 Token Economics Skill Library.png",
    "picture-028.png": "Figure 9 Production Histories to Procedural Memories.png",
    "picture-030.png": "Figure 10 Meta-Skill Evaluation Gating.png",
    "picture-032.png": "Figure 11 Skills-First Retail Architecture.png",
}


def main() -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    for old_file in FIGURE_DIR.glob("*.png"):
        old_file.unlink()

    for raw_name, figure_name in FIGURES.items():
        source = RAW_DIR / raw_name
        target = FIGURE_DIR / figure_name
        if not source.exists():
            raise FileNotFoundError(f"Missing raw image: {source}")
        shutil.copyfile(source, target)
        print(f"{raw_name} -> {figure_name}")

    print(f"Saved {len(FIGURES)} figures to: {FIGURE_DIR}")


if __name__ == "__main__":
    main()
