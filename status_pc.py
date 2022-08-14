from __future__ import print_function
from doctest import master
import os
import shutil
import sys


def check_reboot():
    """ Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")


def check_disk_full(disk, min_gb, min_percent):
    """Returns True if there isn't enough disk space, Flase otherwise"""
    du = shutil.disk_usage(disk)
    # Calculate the percentage of free space
    percent_free = 100 * du.free / du.total
    # Calculate hoiw many free gigabytes there are
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False


def main():
<<<<<<< HEAD
    if check_reboot():
        print("Pending reboot. ")
        sys.exit(1)
    if check_disk_full(disk="/", min_gb=2, min_percent=10):
        print("Disk full")
=======
    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition full"),
    ]
    everything_ok = True
    for check, msg in checks:
        if check(): 
            print(msg)
            everything_ok = False

    if not everything_ok:
>>>>>>> d9d9bd6093ed557c312d8a52d51b4fdbcd745f11
        sys.exit(1)


    print("Everything ok.")
    sys.exit(0)

    
main()

