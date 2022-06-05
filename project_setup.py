import nuke 


def project_setting():
    nuke.root()["fps"].setValue(24)
    nuke.root()['format'].setValue('HK_1080')

