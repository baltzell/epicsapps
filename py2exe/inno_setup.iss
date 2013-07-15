; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
AppName=Epics Applications
AppVersion=0.1
AppPublisher=Matthew Newville, GSECARS,  The University of Chicago
AppPublisherURL=http://pyepics.github.com/epicsapps/
AppSupportURL=http://pyepics.github.com/epicsapps/
AppUpdatesURL=http://pyepics.github.com/epicsapps/
AppCopyright=Copyright (C) 2012 Matthew Newville
DefaultDirName={pf}\Epics Applications
DefaultGroupName=Epics Applications
AlwaysRestart=no
LicenseFile=C:\Program Files\Epics Applications\license.txt

[Tasks]
Name: "desktopicon"; Description: "Create &desktop icons"; GroupDescription: "Additional icons:"; MinVersion: 4,4

[Files]
Source: "C:\Program Files\Epics Applications\*";   DestDir: "{app}";  Flags: "recursesubdirs"
Source: "C:\Program Files\Epics Applications\README.txt"; DestDir: "{app}"; Flags: isreadme

[Icons]
Name: "{group}\Epics Instruments";         WorkingDir: "{app}"; Filename: "{app}\EpicsInstruments.exe";        IconFilename: "{app}\instrument.ico";
Name: "{group}\Epics AreaDetector Viewer"; WorkingDir: "{app}"; Filename: "{app}\EpicsAreaDetectorViewer.exe"; IconFilename: "{app}\camera.ico";
Name: "{group}\Epics StripChart";          WorkingDir: "{app}"; Filename: "{app}\EpicsStripChart.exe";         IconFilename: "{app}\stripchart.ico";
Name: "{group}\Epics MotorSetup (GSE)";    WorkingDir: "{app}"; Filename: "{app}\EpicsMotorSetup_GSE.exe";     IconFilename: "{app}\motorapp.ico";
Name: "{group}\Epics MotorSetup (Local)";  WorkingDir: "{app}"; Filename: "{app}\EpicsMotorSetup_SQLITE.exe";  IconFilename: "{app}\motorapp.ico";

Name: "{group}\Uninstall Epics Applications"; Filename: "{uninstallexe}"

