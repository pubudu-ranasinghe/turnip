import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5

Window {
    id: importerWindow

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

        text: qsTr("Import")
        x: 20; y: 36
        font {
            pixelSize: 28
            family: "Inter"
            weight: Font.Bold
            letterSpacing: -1.4
        }

    }
}