import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.2

import ActionType 1.0

Window {
    id: importerWindow
    // visible: true

    FontLoader {
        id: interBold
        source: "fonts/Inter-Bold.ttf"
    }

    FontLoader {
        id: interRegular
        source: "fonts/Inter-Regular.ttf"
    }

    property string color_primary: "#fcd307"
    property string color_black: "#1b1919"
    property string color_gray: "#ececec"
    property string color_grayish: "#aeabab"
    property string color_dark_gray: "#4e4747"
    property string color_white_two: "#fafafa"

    function formatCandidateString(candidate) {
        let result = ""
        if (candidate) {
            result = `(${Math.floor(candidate.distance * 100)} %) ${candidate.title} - ${candidate.artist}`;
        }
        return result
    }

    width: 720
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

            DetailButton {
                width: 600; height: 50
                primaryText: formatCandidateString(importer.currentItem.candidates[index])
                image: "images/placeholder.png"
                backgroundColor: color_white_two
                onClicked: importer.sendAction(ActionType.SELECT_CANDIDATE, index)
            }
        }
    }

    CustomButton {
        id: skipButton
        x: 20; y: 510
        width: 120; height: 50
        backgroundColor: color_gray
        text: qsTr("Skip")
        onClicked: importer.sendAction(ActionType.SKIP)
    }

    CustomButton {
        id: useAsIsButton
        x: 155; y: 510
        width: 120; height: 50
        backgroundColor: color_gray
        text: qsTr("Use as-is")
        onClicked: importer.sendAction(ActionType.USE_AS_IS)
    }

    CustomButton {
        id: asTracksButton
        x: 290; y: 510
        width: 120; height: 50
        backgroundColor: color_gray
        text: qsTr("As Tracks")
        onClicked: importer.sendAction(ActionType.AS_TRACKS)
    }

    CustomButton {
        id: searchButton
        x: 425; y: 510
        width: 120; height: 50
        backgroundColor: color_gray
        text: qsTr("Search")
        enabled: false
        onClicked: importer.sendAction(ActionType.SEARCH)
    }

    CustomButton {
        id: abortButton
        x: 580; y: 510
        width: 120; height: 50
        backgroundColor: color_gray
        text: qsTr("Abort")
        onClicked: importer.sendAction(ActionType.ABORT)
    }

    Dialog {
        id: resumeDialog
        visible: false
        title: qsTr("Resume Previous Import")
        standardButtons: StandardButton.Yes | StandardButton.No

        onYes: importer.sendAction(ActionType.RESUME_YES)
        onNo: importer.sendAction(ActionType.RESUME_NO)

        Text {
            id: resumeDialogText
            text: qsTr("We found a previous import session. Do you want to continue from where you left off?")
        }
    }

    // TODO Refactor this signal
    signal reEndSession()
    signal reResumePreviousImport()
    signal reResolveDuplicate(var oldItem, var newItem)
    signal duplicateSelectAction(var action)

    Component.onCompleted: {
        importer.endSession.connect(reEndSession)
        importer.resumePreviousImport.connect(reResumePreviousImport)
        importer.resolveDuplicate.connect(reResolveDuplicate)
    }

    Connections {
        target: importerWindow
        onReEndSession: importerWindow.close()
        onReResumePreviousImport: resumeDialog.open()
        onReResolveDuplicate: {
            var component = Qt.createComponent("ResolveDuplicate.qml");
            var resolveDialog = component.createObject(importerWindow);
            resolveDialog.oldItem = oldItem;
            resolveDialog.newItem = newItem;
            resolveDialog.onSelectAction.connect(importer.sendAction)
            resolveDialog.show()
        }

    }

    BusyIndicator {
        id: busyIndicator
        x: 290
        y: 210
        running: importer.loadingStatus
    }
}




