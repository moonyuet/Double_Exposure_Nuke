import nuke
import os
def change_file_path():
    change_file_panel = nuke.Panel("Change File")
    change_file_panel.addFilenameSearch("New File Path", "")
    change_file_panel.show()

    new_file_path = change_file_panel.value("New File Path")

    try:
        selected_read_node = nuke.selectedNode()
        read_node_list = nuke.allNodes("Read")
            
        if selected_read_node in read_node_list:
            if os.path.exists(new_file_path):
                selected_read_node["file"].setValue(new_file_path)
        else:
            nuke.message("Warning : The Read node isn't selected")
            
    except ValueError as er:
        nuke.message(str(er))