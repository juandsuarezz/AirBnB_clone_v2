#!/usr/bin/python3
"""Compresses contents of a folder"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """compresses a folder to a .tgz archive"""
    tar_cmd = "sudo tar -cvzf "
    mkdir_cmd = "sudo mkdir -p versions/"
    date_string = datetime.now().strftime('%Y%m%d%H%M%S')
    local(mkdir_cmd)
    try:
        local(tar_cmd + "versions/web_static_{}.tgz "
              .format(date_string) +
              "web_static")
        return "/versions/web_static_{}.tgz".format(date_string)
    except BaseException:
        return None
