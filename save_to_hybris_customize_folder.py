import sublime
import sublime_plugin
import os
import shutil

class SaveToHybrisCustomizeFolder(sublime_plugin.WindowCommand):
  """Assumes the active view is a file within ${HYBRIS_BIN_DIR}
  Make a copy of that file in the ${HYBRIS_CONFIG_DIR}/customize/ folder
  with the sub-directory intact. i.e. all subdirecties will be created.

  e.g. 

  $HYBRIS_BIN_DIR/platform/tomcat/LICENSE

  will create a copy of LICENSE in

  $HYBRIS_CONFIG_DIR/platform/tomcat/
  """
  def run(self):
    # Get the current File Name
    file_name = self.window.active_view().file_name()

    # get everything after "bin"
    pos = file_name.find("bin")

    # subpath
    base_path = file_name[0:pos]
    sub_path_and_file = file_name[pos+3:]

    new_full_file = base_path + "config" + os.path.sep + "customize" + sub_path_and_file

    (new_dir_name, new_file_name) = os.path.split(new_full_file)

    if os.access(new_dir_name, os.F_OK) == False:
      os.makedirs(new_dir_name)

    shutil.copy(file_name, new_full_file)
