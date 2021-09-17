c.InteractiveShellApp.extensions = [
    'sql'
]

c.InteractiveShellApp.exec_lines = [
    '%sql sqlite:///jobs.db ',
    '%config SqlMagic.autolimit = 50'
    '%config SqlMagic.displaycon = True'
]