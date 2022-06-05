import nuke
def param_node():
    param_node = nuke.createNode('NoOp')

    param_node["name"].setValue('PARAMETER_CONTROLLER')
    custom_name = param_node["name"].getValue()

    #first tab
    param_node.addKnob(nuke.Tab_Knob('Main_Param', "Main_Param"))
    param_node.addKnob(nuke.Keyer_Knob("MC_Keyer","MC_Keyer"))
    param_node["MC_Keyer"].setValue([0.3, 0.55, 1.0, 1.0])
    param_node.addKnob(nuke.Text_Knob( "divider", "" ))

    param_node.addKnob(nuke.Keyer_Knob("OC_Keyer","OC_Keyer"))
    param_node["OC_Keyer"].setValue([0.02, 0.05, 1.0, 1.0])
    param_node.addKnob(nuke.Text_Knob( "divider", "" ))
    param_node.addKnob(nuke.Double_Knob("MC_Blur", "MC_Blur"))
    param_node["MC_Blur"].setValue(1.2)
    param_node.addKnob(nuke.Double_Knob("OC_Blur", "OC_Blur"))
    param_node["OC_Blur"].setValue(20)
    param_node.addKnob(nuke.Text_Knob( "divider", "" ))

    overlay_keyer_node = nuke.allNodes("Keyer")[0]
    overlay_keyer_node.knob("range").setExpression(custom_name + ".OC_Keyer")
    main_keyer_node = nuke.allNodes("Keyer")[1]
    main_keyer_node.knob("range").setExpression(custom_name + ".MC_Keyer")
    blur_node = nuke.allNodes("Blur")[0]
    blur_node.knob("size").setExpression(custom_name + ".MC_Blur")
    edge_blur = nuke.allNodes("EdgeBlur")[0]
    edge_blur.knob("size").setExpression(custom_name + ".OC_Blur")

    #second tab
    param_node.addKnob(nuke.Tab_Knob("Detail_Correction", "Detail_Correction"))
    param_node.addKnob(nuke.Double_Knob("M_Saturation","M_Saturation"))
    param_node["M_Saturation"].setValue(0.4)
    param_node.addKnob(nuke.Double_Knob("M_Contrast","M_Contrast"))
    param_node["M_Contrast"].setValue(0.9)
    param_node.addKnob(nuke.Double_Knob("M_Gamma","M_Gamma"))
    param_node["M_Gamma"].setValue(0.95)
    param_node.addKnob(nuke.Double_Knob("M_Gain","M_Gain"))
    param_node["M_Gain"].setValue(1.5)
    param_node.addKnob(nuke.Text_Knob( "divider", "" ))

    param_node.addKnob(nuke.Double_Knob("Shadow_Gamma","Shadow_Gamma"))
    param_node["Shadow_Gamma"].setValue(1.5)
    param_node.addKnob(nuke.Double_Knob("Mid_Contrast","Mid_Contrast"))
    param_node["Mid_Contrast"].setValue(1.5)
    param_node.addKnob(nuke.Double_Knob("Mid_Gain","Mid_Gain"))
    param_node["Mid_Gain"].setValue(1.2)
    param_node.addKnob(nuke.Double_Knob("High_Gain","High_Gain"))
    param_node["High_Gain"].setValue(1.12)
    param_node.addKnob(nuke.Text_Knob( "divider", "" ))

    color_correct = nuke.allNodes("ColorCorrect")[0]
    color_correct.knob("saturation").setExpression(custom_name + ".M_Saturation")
    color_correct.knob("contrast").setExpression(custom_name + ".M_Contrast")
    color_correct.knob("gamma").setExpression(custom_name + ".M_Gamma")
    color_correct.knob("gain").setExpression(custom_name + ".M_Gain")
    color_correct.knob("shadows.gamma").setExpression(custom_name + ".Shadow_Gamma")
    color_correct.knob("midtones.contrast").setExpression(custom_name + ".Mid_Contrast")    
    color_correct.knob("midtones.gain").setExpression(custom_name + ".Mid_Gain") 
    color_correct.knob("highlights.gain").setExpression(custom_name + ".High_Gain") 
