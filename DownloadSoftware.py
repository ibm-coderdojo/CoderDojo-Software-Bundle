#!/usr/bin/python

import os.path
import urllib

from urlparse import urlparse

baseFolder = os.path.expanduser("~") + os.path.sep + "Downloads" + os.path.sep + "CoderDojoSoftware" + os.path.sep
if not os.path.exists(baseFolder):
    '''Check if the ~/Downloads/CoderDojoSoftware exists and eventually create it'''
    os.makedirs(baseFolder)

def downloadPackage(packageUrl, downloadFolder, fileName=""):
    '''Download a package archive from the network
    
    Keyword arguments:
    packageUrl -- URL of the package archive to download
    downloadFolder -- local path where the package must be saved
    '''

    if not os.path.exists(downloadFolder):
        '''Check if the ~/Downloads/CoderDojoSoftware exists and eventually create it'''
        os.makedirs(downloadFolder)

    if (fileName == ""):
        urlSlice = urlparse(packageUrl)
        fileName = os.path.split(urlSlice.path)
        fileName = fileName[1]

    # TODO: implement also a step --  if not os.file.exists(downloadFolder + fileName)

    return urllib.urlretrieve(packageUrl, downloadFolder + fileName)

packages = dict()
packages["Scratch"] = {
    "1.4": {
        "Linux": ["http://ubuntu.media.mit.edu/ubuntu//pool/universe/s/scratch/scratch_1.4.0.6~dfsg1-2~ubuntu12.04.1_all.deb"],
        "Mac": ["http://download.scratch.mit.edu/MacScratch1.4.dmg"],
        "Windows": ["http://download.scratch.mit.edu/ScratchInstaller1.4.exe"],
        "doc": [
            "http://download.scratch.mit.edu/ScratchGettingStartedv14.pdf",
            "http://download.scratch.mit.edu/ScratchReferenceGuide14.pdf",
            "http://download.scratch.mit.edu/ScratchCardsAll-v1.4-PDF.zip"
        ]
    },
    "2.0": {
        "Linux": [
            "http://airdownload.adobe.com/air/lin/download/2.6/AdobeAIRInstaller.bin",
            "http://cdn.scratch.mit.edu/scratchr2/static/sa/Scratch-431a.air"
        ],
        "Mac_until-10.5": [
            "http://airdownload.adobe.com/air/mac/download/2.6/AdobeAIR.dmg",
            "http://cdn.scratch.mit.edu/scratchr2/static/sa/Scratch-431a.dmg"
        ],
        "Mac_newer": [
            "http://download.macromedia.com/air/mac/download/16.0/AdobeAIR.tbz2",
            "http://cdn.scratch.mit.edu/scratchr2/static/sa/Scratch-431a.dmg"
        ],
        "Windows": [
            "http://download.macromedia.com/air/win/download/16.0/AdobeAIRInstaller.zip",
            "http://cdn.scratch.mit.edu/scratchr2/static/sa/Scratch-431a.exe"
        ],
        "doc": [
            "http://cdn.scratch.mit.edu/scratchr2/static/__6b70b0bfa023343400311915fef8f6cc__/sa/Scratch2StarterProjects.zip",
            "http://cdn.scratch.mit.edu/scratchr2/static/__6b70b0bfa023343400311915fef8f6cc__/pdfs/help/Getting-Started-Guide-Scratch2.pdf",
            "http://cdn.scratch.mit.edu/scratchr2/static/__6b70b0bfa023343400311915fef8f6cc__/pdfs/help/Scratch2Cards.pdf"
        ]
    }
}
packages["AppInventor"] = {
    "2.0": {
        "Linux": [
            "http://commondatastorage.googleapis.com/appinventordownloads/appinventor2-setup_1.1_all.deb",
            "http://commondatastorage.googleapis.com/appinventordownloads/appinventor2-setup_1.1.tar.gz"
        ],
        "Mac": ["http://dl.google.com/appinventor/installers/mac/AppInventor_Setup_v_1.1.dmg"],
        "Windows": ["http://dl.google.com/dl/appinventor/installers/windows/appinventor_setup_installer_v_1_2.exe"],
        "doc": [
            "http://appinventor.mit.edu/explore/sites/all/files/hourofcode/TalkToMePart1_2perpage.pdf",
            "http://appinventor.mit.edu/explore/sites/all/files/hourofcode/TalkToMePart2_2perpage.pdf",
            "http://appinventor.mit.edu/explore/sites/all/files/hourofcode/BallBounceTutorial_2perpage.pdf",
            "http://appinventor.mit.edu/explore/sites/all/files/hourofcode/DigitalDoodle_2perpage.pdf"
        ]
    }
}
packages["Bluemix"] = {
    "CloudFoundry-6.9.0": {
        "Linux": [
            "https://cli.run.pivotal.io/stable?release=debian32&version=6.9.0&source=github-rel",
            "https://cli.run.pivotal.io/stable?release=debian64&version=6.9.0&source=github-rel",
            "https://cli.run.pivotal.io/stable?release=redhat32&version=6.9.0&source=github-rel",
            "https://cli.run.pivotal.io/stable?release=redhat64&version=6.9.0&source=github-rel",
            "https://cli.run.pivotal.io/stable?release=linux32-binary&version=6.9.0&source=github-rel",
            "https://cli.run.pivotal.io/stable?release=linux64-binary&version=6.9.0&source=github-rel"
        ],
        "Mac": [
            "https://cli.run.pivotal.io/stable?release=macosx64&version=6.9.0&source=github-rel",
            "https://cli.run.pivotal.io/stable?release=macosx64-binary&version=6.9.0&source=github-rel"
        ],
        "Windows": [
            "https://cli.run.pivotal.io/stable?release=windows32&version=6.9.0&source=github-rel",
            "https://cli.run.pivotal.io/stable?release=windows64&version=6.9.0&source=github-rel",
            "https://cli.run.pivotal.io/stable?release=windows32-exe&version=6.9.0&source=github-rel",
            "https://cli.run.pivotal.io/stable?release=windows64-exe&version=6.9.0&source=github-rel"
        ]
    }
}
packages["RaspberryPI"] = {
    "MobaXterm-7.4": {
        "Windows": ["http://mobaxterm.mobatek.net/MobaXterm_Setup_7.4.msi"]
    },
    "Putty-0.63": {
        "Windows": [
            "ftp://ftp.chiark.greenend.org.uk/users/sgtatham/putty-latest/x86/putty.exe",
            "ftp://ftp.chiark.greenend.org.uk/users/sgtatham/putty-latest/x86/pscp.exe",
            "ftp://ftp.chiark.greenend.org.uk/users/sgtatham/putty-latest/x86/psftp.exe",
            "ftp://ftp.chiark.greenend.org.uk/users/sgtatham/putty-latest/x86/putty-0.63-installer.exe"
        ]
    },
    "WinSCP-5.5.6": {
        "Windows": ["http://winscp.net/download/winscp556setup.exe"]
    }
}

#    },
#    "RealVNC-5.2.2": {
#        "Linux": [
#            "https://www.realvnc.com/download/binary/1674/",
#            "https://www.realvnc.com/download/binary/1675/",
#            "https://www.realvnc.com/download/binary/1676/",
#            "https://www.realvnc.com/download/binary/1677/"
#        ],
#        "Mac": ["https://www.realvnc.com/download/binary/1673/"],
#        "Windows": [
#            "https://www.realvnc.com/download/binary/1669/",
#            "https://www.realvnc.com/download/binary/1671/"
#        ]

for packageName in packages:
    print "Downloading the package: ", packageName
    for release in packages[packageName]:
        print "\trelease: ", release
        for target in packages[packageName][release]:
            print "\t\ttarget: ", target
            for packageUrl in packages[packageName][release][target]:
                print "\t\t\tFrom URL: ", packageUrl
                downloadFolder = baseFolder + packageName + os.path.sep + release + os.path.sep + target + os.path.sep
                print "\t\t\tTo folder: ", downloadFolder
                #downloadPackage(packageUrl, downloadFolder)

print "Downloads completed!"
