import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5

Window {
    id: mainWindow


    FontLoader {
        id: interBold
        source: "../fonts/Inter-Bold.ttf"
    }

    FontLoader {
        id: interRegular
        source: "../fonts/Inter-Regular.ttf"
    }

    property var configWindow: Configuration {}
    property var libraryWindow: Library {}
    property var importerSelectionWindow: ImporterSelection {}
    
    property string color_primary: "#fcd307"
    property string color_black: "#1b1919"
    property string color_gray: "#ececec"
    property string color_grayish: "#aeabab"
    property string color_dark_gray: "#4e4747"  

    visible: true
    width: 360
    height: 480
    title: qsTr("Beets UI")

    Rectangle {
        id: header
        width: parent.width
        height: 100

        Text {
            id: logoType

            text: "Turnip"
            anchors {
                horizontalCenter: parent.horizontalCenter
                verticalCenter: parent.verticalCenter
            }
            font {
                pixelSize: 42
                family: "Inter"
                weight: Font.Bold
                letterSpacing: -2
            }

        }
    }

    Column {
        id: stats

        x: 20
        width: parent.width - 40
        anchors.top: header.bottom
        spacing: 5

        Text {
            text: library.stats.trackCount + " Tracks"
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
        }
        Text {
            text: library.stats.albums + " Albums"
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
        }
        Text {
            text: library.stats.totalTime
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
        }
        Text {
            text: library.stats.totalSize
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
        }
    }

    CustomButton {
        id: importBtn

        x: 20; y: 245
        width: 320; height: 100
        buttonText: "Import"
        backgroundColor: color_primary
        textcolor: color_black

        onClicked: importerSelectionWindow.visible = true
    }

    CustomButton {
        id: libraryBtn

        x: 20; y: 360
        width: 152; height: 100
        buttonText: "Library"
        backgroundColor: color_gray
        textcolor: color_black

        onClicked: libraryWindow.visible = true
    }

    CustomButton {
        id: configureBtn

        x: 188; y: 360
        width: 152; height: 100
        buttonText: "Configure"
        backgroundColor: color_gray
        textcolor: color_black

        onClicked: configWindow.visible = true
    }

}

