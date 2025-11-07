import subprocess
import sys

# Get URL from command line or use default
url = sys.argv[1] if len(sys.argv) > 1 else "https://the-internet.herokuapp.com"

print(f"Starting Playwright Codegen for: {url}")
subprocess.run(["playwright", "codegen", url])