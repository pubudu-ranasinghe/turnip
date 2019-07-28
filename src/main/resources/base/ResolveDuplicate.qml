import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.3

Window {
    id: resolveDuplicateWindow

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

    width: 360
    height: 480
    title: qsTr("Resolve Duplicate")
    flags: Qt.Dialog

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
        id: oldItem

        x: 20; y: 107
        height: 90; width: 320
        image: "../images/placeholder.png"
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
        id: newItem

        x: 20; y: 236
        height: 90; width: 320
        image: "../images/placeholder.png"
    }

    CustomButton {
        id: replaceButton

        x: 20; y: 350
        width: 155; height: 50
        text: qsTr("Replace")
        backgroundColor: color_gray
    }

    CustomButton {
        id: skipButton

        x: 185; y: 350
        width: 155; height: 50
        text: qsTr("Skip")
        backgroundColor: color_gray
    }

    CustomButton {
        id: keepBothButton

        x: 20; y: 410
        width: 155; height: 50
        text: qsTr("Keep Both")
        backgroundColor: color_gray
    }

    CustomButton {
        id: mergeButton

        x: 185; y: 410
        width: 155; height: 50
        text: qsTr("Merge")
        backgroundColor: color_gray
    }

}
