import nuke 

def add_toolbar(path):
    ICON_PATH =  path + "/Icons/"

    de_toolbar = nuke.menu('Nuke').addMenu('DE_Menu', icon=ICON_PATH + 'menu_icon.png')

    de_toolbar.addCommand("Project Setting", 'import project_setup; project_setup.project_setting()', icon = ICON_PATH + 'import.png')
    de_toolbar.addCommand("Do the Double Exposure", 'import double_exposure_func; double_exposure_func.double_exposure()', icon = ICON_PATH + 'exp_icon.png')
    de_toolbar.addCommand("Parameter Node", 'import param_node; param_node.param_node()', icon = ICON_PATH + 'param_icon.png')
    de_toolbar.addCommand("Change the Image File", 'import change_file; change_file.change_file_path()', icon = ICON_PATH + 'write.png')
    de_toolbar.addCommand("Help", "import webbrowser; webbrowser.open('https://www.kaylaman.com/double-exposure-plugin-in-nuke.html')", icon= ICON_PATH + 'help.png')
    