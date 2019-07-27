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
    property string color_white_two: "#fafafa"

    width: 640
    height: 580
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

    Column {
        x: 20; y: 154
        width: 600
        spacing: 10

        Repeater {
            model: 4

            CustomButton {
                width: 600; height: 50
                text: importer.currentItem.candidates[index] ? importer.currentItem.candidates[index].title : ""
                alignment: Text.AlignLeft
                backgroundColor: color_white_two
                onClicked: importer.sendAction(ImportAction.SELECT_CANDIDATE, index)
            }
        }
    }

    CustomButton {
        id: skipButton
        x: 20; y: 510
        width: 120; height: 50
        backgroundColor: color_gray
        text: qsTr("Skip")
        onClicked: importer.sendAction(ImportAction.SKIP)
    }

    CustomButton {
        id: abortButton
        x: 490; y: 510
        width: 120; height: 50
        backgroundColor: color_gray
        text: qsTr("Abort")
        onClicked: importer.sendAction(ImportAction.ABORT)
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




