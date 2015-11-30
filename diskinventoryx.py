import sublime, sublime_plugin, os
from subprocess import call

def plugin_loaded():
  if diskInventoryIsInstalled() is False:
    sublime.error_message("Disk Inventory X is not installed at \n /Applications/Disk Inventory X.app")

def diskInventoryIsInstalled():
  return os.path.exists("/Applications/Disk Inventory X.app")

class DiskInventoryCommand(sublime_plugin.WindowCommand):
  def run(self, paths = []):
    for path in paths:
      if os.path.isdir(path):
        call(["open", "/Applications/Disk Inventory X.app", "--args", path])

  def is_visible(self, paths =[]):
    if diskInventoryIsInstalled():
      for path in paths:
        if os.path.isdir(path):
          return True
    return False
