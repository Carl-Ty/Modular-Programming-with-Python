import importlib
import sys
import os.path

plugin_dir = os.path.join(os.path.dirname(__file__), "plugins")
sys.path.append(plugin_dir)
files = '\n'.join([plugin for plugin in os.listdir(plugin_dir) if
                   plugin.upper().endswith(".PY")])
prompt = f"{files}\n" \
         f"Enter the selected plugin name "
plugin_name = input(prompt)
if plugin_name != "":
    plugin = importlib.import_module(plugin_name)
    plugin.say_hello()
