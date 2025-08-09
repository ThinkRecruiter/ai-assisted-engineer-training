from typing import Dict, Any

def make_candidate_blurb(candidate: Dict[str, Any]) -> str:
    """
    Takes a candidate dict and returns a formatted blurb.
    """
    name = candidate.get("name", "Unknown")
    title = candidate.get("title", "Unknown title")
    highlights = candidate.get("highlights", [])
    bullet = "\n - ".join(highlights) if highlights else "No highlights provided."
    return f"{name} — {title}\n - {bullet}"

if __name__ == "__main__":
    example = {
        "name": "Sydney Sokol",
        "title": "Investor Relations Associate",
        "highlights": ["Strong LP communications", "Prior relationship with Landing Point"]
    }
    print(make_candidate_blurb(example))