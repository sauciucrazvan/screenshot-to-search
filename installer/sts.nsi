Name "Screenshot to Search - Installer"
OutFile "sts-installer.exe"

Page Directory
Page InstFiles

InstallDir "$PROGRAMFILES\Screenshot to Search"

Section
    InitPluginsDir
    SetOutPath $INSTDIR
    File "C:\Users\Razvan\Desktop\screenshot-to-search.zip"
    ExecWait '"powershell" -Command "Expand-Archive \"$INSTDIR\screenshot-to-search.zip\" -DestinationPath \"$INSTDIR\""'

    SetOutPath "$SMSTARTUP"
    CreateShortcut "$SMSTARTUP\Screenshot to Search.lnk" "$INSTDIR\screenshot-to-search.exe" ;

    Exec '"$INSTDIR\screenshot-to-search.exe"'
SectionEnd
