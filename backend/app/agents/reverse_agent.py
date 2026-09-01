from .prompt_library import PROMPTS


class ReverseAgent:
    def run(self, target: str) -> str:
        return f"Reverse analysis complete for {target}: {PROMPTS['reverse']}"
