import os
import shutil

RootDir = r'\Users\KalleNY\Downloads'
TargetPhoto = r'\Users\KalleNY\Pictures\Images'
TargetMusic = r'\Users\KalleNY\Music'
TargetInstallers = r'\Users\KalleNY\Documents\Installers'
TargetRars = r'\Users\KalleNY\Documents\Rars'
TargetDll = r'\Users\KalleNY\Documents\.ddl'
TargetDocs = r'\Users\KalleNY\Documents\Documents'
for root, dirs, files in os.walk((os.path.normpath(RootDir))):
    for name in files:
        if name.endswith('.png'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetPhoto) #copies file to target folder
        elif name.endswith('.jpg'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetPhoto)
        elif name.endswith('.wav'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetMusic)
        elif name.endswith('.mp3'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetMusic)
        elif name.endswith('.msi'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetInstallers)
        elif name.endswith('.gz'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetRars)
        elif name.endswith('.zip'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetRars)
        elif name.endswith('.dll'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetDll)
        elif name.endswith('.txt'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetDocs)
        elif name.endswith('.doc'):
            SourceFolder = os.path.join(root, name)
            shutil.move(SourceFolder, TargetDocs)