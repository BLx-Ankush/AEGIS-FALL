from .agents.exploit_agent import ExploitAgent
from .agents.recon_agent import ReconAgent
from .agents.reverse_agent import ReverseAgent


async def orchestrate_target(target: str) -> list[str]:
    recon = ReconAgent().run(target)
    exploit = ExploitAgent().run(target)
    reverse = ReverseAgent().run(target)
    return [recon, exploit, reverse]
