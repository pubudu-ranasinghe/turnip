import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.2

import ImportAction 1.0

Window {
    id: importerWindow
    // visible: true

    FontLoader {
        id: interBold
        source: "../fonts/Inter-Bold.ttf"
    }

    FontLoader {
        id: interRegular
        source: "../fonts/Inter-Regular.ttf"
    }

    property string color_primary: "#fcd307"
    property string color_black: "#1b1919"
    property string color_gray: "#ececec"
    property string color_grayish: "#aeabab"
    property string color_dark_gray: "#4e4747"

    width: 640
    height: 480
    title: qsTr("Import Music")

    Text {
        id: headerText

        text: importer.loadingStatus ? qsTr("Loading") : qsTr("Tagging")
        x: 20; y: 36
        font {
            pixelSize: 28
            family: "Inter"
            weight: Font.Bold
            letterSpacing: -1.4
        }
    }

    Text {
        id: currentItemText

        text: importer.currentItem.path
        x: 20; y: 76
        font {
            pixelSize: 16
            family: "Inter"
            weight: Font.Normal
        }
        color: color_grayish

    }

    Text {
        id: candidate1

        text: importer.currentItem.candidates[0].title
        x: 20; y: 146
        font {
            pixelSize: 16
            family: "Inter"
            weight: Font.Normal
        }
        color: color_grayish
    }

    Text {
        id: candidate2

        text: importer.currentItem.candidates[1].title
        x: 20; y: 166
        font {
            pixelSize: 16
            family: "Inter"
            weight: Font.Normal
        }
        color: color_grayish
    }

    Text {
        id: candidate3

        text: importer.currentItem.candidates[2].title
        x: 20; y: 186
        font {
            pixelSize: 16
            family: "Inter"
            weight: Font.Normal
        }
        color: color_grayish
    }

    Text {
        id: candidate4

        text: importer.currentItem.candidates[3].title
        x: 20; y: 206
        font {
            pixelSize: 16
            family: "Inter"
            weight: Font.Normal
        }
        color: color_grayish
    }

    Button {
        x: 20; y: 320
        text: "Skip"
        onClicked: importer.sendAction(ImportAction.SKIP)
    }

    Dialog {
        id: resumeDialog
        visible: false
        title: qsTr("Resume Previous Import")
        standardButtons: StandardButton.Yes | StandardButton.No

        onYes: importer.sendAction(ImportAction.RESUME_YES)
        onNo: importer.sendAction(ImportAction.RESUME_NO)

        Text {
            id: resumeDialogText
            text: qsTr("We found a previous import session. Do you want to continue from where you left off?")
        }
    }

    // TODO Refactor this signal
    signal reEndSession()
    signal reResumePreviousImport()

    Component.onCompleted: {
        importer.endSession.connect(reEndSession)
        importer.resumePreviousImport.connect(reResumePreviousImport)
    }

    Connections {
        target: importerWindow
        onReEndSession: importerWindow.close()
        onReResumePreviousImport: resumeDialog.open()
    }

    BusyIndicator {
        id: busyIndicator
        x: 290
        y: 210
        running: importer.loadingStatus
    }
}




