import sublime, sublime_plugin, os
from subprocess import call

global diskInventoryXPath
diskInventoryXPath = "/Applications/Disk Inventory X.app"


def plugin_loaded():
  if diskInventoryIsInstalled() is False:
    sublime.error_message("Disk Inventory X is not installed at \n" + DiskInventoryXPath)

def diskInventoryIsInstalled():
  return os.path.exists(DiskInventoryXPath)

class DiskInventoryCommand(sublime_plugin.WindowCommand):
  def run(self, paths = []):
    for path in paths:
      if os.path.isdir(path):
        call(["open", DiskInventoryXPath, "--args", path])

  def is_visible(self, paths =[]):
    if diskInventoryIsInstalled():
      for path in paths:
        if os.path.isdir(path):
          return True
    return False
