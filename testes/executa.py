import subprocess

subprocess.run(
    ["python", "-m", "uvicorn", "main:app", "--reload"],
    shell=True
)
