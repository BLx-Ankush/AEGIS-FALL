from .prompt_library import PROMPTS


class ReconAgent:
    def run(self, target: str) -> str:
        return f"Recon complete for {target}: {PROMPTS['recon']}"
