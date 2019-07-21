import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5

Window {
    id: tagRecordWindow
    visible: true

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

    width: 630
    height: 580
    title: qsTr("Tagging")

    Text {
        id: headerText

        text: qsTr("Tagging")
        x: 20; y: 36
        font {
            pixelSize: 28
            family: "Inter"
            weight: Font.Bold
            letterSpacing: -1.4
        }

    }

    Text {
        id: fileName

        text: qsTr("/Users/Downloads/LT - LP")
        x: 20; y: 76
        color: color_grayish
        font {
            pixelSize: 16
            family: "Inter"
            weight: Font.Normal
        }
    }

    DetailButton {
        id: mainSelectionBtn

        x: 20; y: 154
        width: 580; height: 126
        backgroundColor: color_white_two
        image: "../images/placeholder.png"
        primaryText: "Living Things"
    }

    DetailButton {
        id: secondSelectionBtn

        x: 20; y: 300
        width: 580; height: 50
        backgroundColor: color_white_two
        image: "../images/placeholder.png"
        primaryText: "Artist - Some Other Album (53.2 %)"
    }

    DetailButton {
        id: thirdSelectionBtn

        x: 20; y: 360
        width: 580; height: 50
        backgroundColor: color_white_two
        image: "../images/placeholder.png"
        primaryText: "Artist - Another Album (23.3 %)"
    }
}
