"""
run_code.py

Runs a code snippet (Python) in a temporary file and returns the stdout/stderr.
CAUTION: This is NOT a secure sandbox. Do NOT run untrusted code with this tool.
For real sandboxing use a proper execution sandbox (e.g., Docker container with seccomp, restricted user, resource limits).

Usage:
    from tools.run_code import run_python_code
    out = run_python_code("print('hello')", timeout=3)
"""

import subprocess
import tempfile
import os
import sys
from typing import Tuple

def run_python_code(code: str, timeout: int = 5) -> Tuple[int, str, str]:
    """
    Returns (exit_code, stdout, stderr)
    """
    # create temp file
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as tf:
        tf.write(code)
        fname = tf.name

    try:
        proc = subprocess.run(
            [sys.executable, fname],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            text=True
        )
        return proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as e:
        return -1, "", f"TimeoutExpired: exceeded {timeout}s"
    except Exception as e:
        return -2, "", f"Exception: {e}"
    finally:
        try:
            os.remove(fname)
        except OSError:
            pass
