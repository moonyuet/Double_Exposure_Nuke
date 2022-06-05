import nuke
import os
def double_exposure():
    file_setup_panel = nuke.Panel("Scene Creation")
    file_setup_panel.setWidth(400)
    file_setup_panel.addFilenameSearch("Main Comp Path","")
    file_setup_panel.addFilenameSearch("Overlaying Comp Path", "")

    file_setup_panel.addFilenameSearch("DE Save Path", "")

    file_setup_panel.show()

    main_comp_path = file_setup_panel.value("Main Comp Path")
    overlay_comp_path = file_setup_panel.value("Overlaying Comp Path")
    DE_Write_Path = file_setup_panel.value("DE Save Path")


    if os.path.exists(main_comp_path) and os.path.exists(overlay_comp_path):
        
        main_comp_node = nuke.nodes.Read(name = "MAIN_COMP", file = main_comp_path)
        main_reformat_node = nuke.nodes.Reformat(name ="MAIN_REFORMAT")
        main_reformat_node.setInput(0, main_comp_node)

        overlay_comp_node = nuke.nodes.Read(name = "OVERLAY_COMP", file = overlay_comp_path)
        overlay_reformat_node = nuke.nodes.Reformat(name = "OVERLAY_REFORMAT")
        overlay_reformat_node.setInput(0, overlay_comp_node)
        
        color_correct_node = nuke.nodes.ColorCorrect(name = "MAIN_COLOR_CORRECTION")
        #tmp_correct_correction
        color_correct_node["saturation"].setValue(0.4)
        color_correct_node["contrast"].setValue(0.9)
        color_correct_node["gamma"].setValue(0.95)
        color_correct_node["gain"].setValue(1.5)
        color_correct_node["shadows.gamma"].setValue(1.5)
        color_correct_node["midtones.contrast"].setValue(1.5)
        color_correct_node["midtones.gain"].setValue(1.2)
        color_correct_node["highlights.gain"].setValue(1.12)
        color_correct_node.setInput(0, main_reformat_node)

        main_blur_node = nuke.nodes.Blur(name = "MAIN_COMP_BLUR", size = 1.2)
        main_blur_node.setInput(0, main_reformat_node)
        main_keyer_node = nuke.nodes.Keyer(name = "MAIN_COMP_KEY", operation = "luminance key")
        main_keyer_node.knob("range").setValue([0.3, 0.55, 1.0, 1.0])
        main_keyer_node.knob("invert").setValue(1)
        main_keyer_node.setInput(0, main_blur_node)

        overlay_keyer_node = nuke.nodes.Keyer(name = "OVERLAY_COMP_KEY", operation = "luminance key")
        overlay_keyer_node.knob("range").setValue([0.02, 0.05, 1.0, 1.0])
        overlay_keyer_node.setInput(0, overlay_reformat_node)
        edge_blur_node = nuke.nodes.EdgeBlur(name = "FG_EdgeBlur", size = 20)
        edge_blur_node.setInput(0, overlay_keyer_node)
        transform_node = nuke.nodes.Transform(name = "FG_Transform")
        transform_node["translate"].setValue([90, -10])
        transform_node["center"].setValue([1024, 778])
        transform_node.setInput(0, edge_blur_node)
        
        merge_node = nuke.nodes.Merge(name= "DE_Merge")
        merge_node.setInput(0, color_correct_node)
        merge_node.setInput(1, transform_node)
        merge_node.setInput(2, main_keyer_node)

        write_node = nuke.nodes.Write(name = "DE_Write", file = DE_Write_Path)
        write_node.setInput(0, merge_node)

    else:
        nuke.message("Either {0} or {1} (or both) doesn't exist! Please Check!".format(main_comp_path, overlay_comp_path))