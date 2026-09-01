import subprocess


def build_sandbox(image_name: str, dockerfile_path: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "build", "-t", image_name, "-f", dockerfile_path, "."],
        check=False,
        text=True,
        capture_output=True,
    )


def run_in_sandbox(image_name: str, command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "run", "--rm", image_name, *command],
        check=False,
        text=True,
        capture_output=True,
    )
