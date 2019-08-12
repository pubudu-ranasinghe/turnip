import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.2

import ActionType 1.0

Window {
    id: importerWindow
    // visible: true

    function formatCandidateString(candidate) {
        let result = ""
        if (candidate) {
          result = `(${Math.floor(candidate.distance * 100)} %) ${candidate.title} - ${candidate.artist}`;
        }
        return result
    }

    property int candidateHoverIndex: 0

    width: 970
    height: 580
    title: qsTr("Import Music")
    modality: Qt.ApplicationModal

    Text {
        id: headerText

        text: importer.currentItem.isAlbum ? qsTr("Tagging Album") : qsTr("Tagging Track")
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
                onHoveredChanged: {
                    if (hovered) {
                        candidateHoverIndex = index
                    }
                }
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
        enabled: importer.currentItem.isAlbum
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

    ItemCard {
        id: itemCard
        x: 720
        itemData: importer.currentItem.candidates[candidateHoverIndex]
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
            width: parent.width
            text: "Text"
            wrapMode: Text.WordWrap
        }
    }

    // TODO Refactor this signal
    signal reEndSession()
    signal reResumePreviousImport(string resumePath)
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
        onReResumePreviousImport: {
            resumeDialogText.text = "We found a previous import session at  " + resumePath + ". Do you want to continue from where you left off?"
            resumeDialog.open()
        }
        onReResolveDuplicate: {
            var component = Qt.createComponent("ResolveDuplicate.qml");
            var resolveDialog = component.createObject(importerWindow);
            resolveDialog.oldItem = oldItem;
            resolveDialog.newItem = newItem;
            resolveDialog.onSelectAction.connect(importer.sendAction)
            resolveDialog.show()
        }

    }

    LoaderView {
        id: busyIndicator
        visible: importer.isBusy
    }
}




