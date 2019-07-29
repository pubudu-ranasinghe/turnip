import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.3

Window {
    id: libraryWindow
    width: 600
    height: 480
    title: qsTr("Library")

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

    Text {
        id: headerText

        text: qsTr("Library")
        x: 20; y: 36
        font {
            pixelSize: 28
            family: "Inter"
            weight: Font.Bold
            letterSpacing: -1.4
        }

    }

    TabBar {
        id: tabBar
        x: 20; y: 92

        CustomTabButton {
            text: qsTr("Albums")
        }

        CustomTabButton {
            text: qsTr("Tracks")
        }

        CustomTabButton {
            text: qsTr("Artists")
        }
    }

    Rectangle {
        width: 575; height: 300
        x: 20; y: 160

        GridView {
            width: parent.width
            height: 300
            boundsBehavior: Flickable.StopAtBounds
            cellWidth: 115
            cellHeight: 150
            clip: true
            model: AlbumModel {}
            delegate: Record {}
            ScrollBar.vertical: ScrollBar {}
        }
    }

}
