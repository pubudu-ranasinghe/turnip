import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.3

import ActionType 1.0

Window {
    id: resolveDuplicateWindow

    property var oldItem: {}
    property var newItem: {}
    
    signal selectAction(int action)

    width: 360
    height: 480
    title: qsTr("Resolve Duplicate")
    flags: Qt.Dialog
    modality: Qt.ApplicationModal

    Text {
        text: qsTr("We found a similar album in your library")
        x: 20; y: 20
        width: 320; height: 60
        font {
            pixelSize: 18
            family: "Inter"
            weight: Font.Normal
        }
        wrapMode: Text.WordWrap
    }

    Text {
        text: qsTr("Old")
        x: 20; y: 78
        font {
            pixelSize: 16
            family: "Inter"
            weight: Font.Normal
        }
        color: color_grayish
    }

    CustomCard {
        id: oldCard

        x: 20; y: 107
        height: 90; width: 320
        image: "images/placeholder.png"
        primaryText: oldItem.title
        secondaryText1: oldItem.artist
        secondaryText2: oldItem.year
    }

    Text {
        text: qsTr("New")
        x: 20; y: 207
        font {
            pixelSize: 16
            family: "Inter"
            weight: Font.Normal
        }
        color: color_grayish
    }

    CustomCard {
        id: newCard

        x: 20; y: 236
        height: 90; width: 320
        image: "images/placeholder.png"
        primaryText: newItem.title
        secondaryText1: newItem.artist
        secondaryText2: newItem.year
    }

    CustomButton {
        id: replaceButton

        x: 20; y: 350
        width: 155; height: 50
        text: qsTr("Replace")
        backgroundColor: color_gray
        onClicked: {
            resolveDuplicateWindow.selectAction(ActionType.REPLACE_OLD)
            resolveDuplicateWindow.close()
        }
    }

    CustomButton {
        id: skipButton

        x: 185; y: 350
        width: 155; height: 50
        text: qsTr("Skip")
        backgroundColor: color_gray
        onClicked: {
            resolveDuplicateWindow.selectAction(ActionType.SKIP_NEW)
            resolveDuplicateWindow.close()    
        }
    }

    CustomButton {
        id: keepBothButton

        x: 20; y: 410
        width: 155; height: 50
        text: qsTr("Keep Both")
        backgroundColor: color_gray
        onClicked: {
            resolveDuplicateWindow.selectAction(ActionType.KEEP_BOTH)
            resolveDuplicateWindow.close()
        }
    }

    CustomButton {
        id: mergeButton

        x: 185; y: 410
        width: 155; height: 50
        text: qsTr("Merge")
        backgroundColor: color_gray
        onClicked: {
            resolveDuplicateWindow.selectAction(ActionType.MERGE)
            resolveDuplicateWindow.close()
        }
    }

}
