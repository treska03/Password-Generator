import platform
import subprocess


def copy_to_clipboard(txt):
    os = platform.system()
    if os == "Darwin":
        cmd='echo '+txt.strip()+'|pbcopy'
        subprocess.check_call(cmd, shell=True)
    else:
        cmd='echo '+txt.strip()+'|clip'
        subprocess.check_call(cmd, shell=True)

