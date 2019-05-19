import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5

Window {
    id: importerWindow
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

    width: 360
    height: 480
    title: qsTr("Select Import Mode")

    Text {
        id: headerText

        text: qsTr("I want to import")
        x: 20; y: 36
        font {
            pixelSize: 28
            family: "Inter"
            weight: Font.Bold
            letterSpacing: -1.4
        }

    }

    Button {
        id: albumImportBtn

        x: 20; y: 100
        width: 320
        horizontalPadding: 20
        verticalPadding: 15

        contentItem: Column {
            spacing: 5
            Text {
                text: qsTr("Albums")
                font {
                    pixelSize: 18
                    family: "Inter"
                    weight: Font.Normal
                }
            }

            Text {
                width: parent.width
                text: qsTr("Each album is organized in their separate directories.")
                wrapMode: Text.WordWrap
                color: color_dark_gray
                font {
                    pixelSize: 14
                    family: "Inter"
                    weight: Font.Normal
                }
            }

            Text {
                width: parent.width
                text: qsTr("Suitable when importing a single album or your music is already organized in albums.")
                wrapMode: Text.WordWrap
                color: color_grayish
                font {
                    pixelSize: 14
                    family: "Inter"
                    weight: Font.Normal
                }
            }
        }

        background: Rectangle {
            color: color_gray
            radius: 5
        }
    }

    Button {
        id: dirImportBtn

        x: 20; y: 245
        width: 320
        horizontalPadding: 20
        verticalPadding: 15

        contentItem: Column {
            spacing: 5
            Text {
                text: qsTr("Directories")
                font {
                    pixelSize: 18
                    family: "Inter"
                    weight: Font.Normal
                }
            }

            Text {
                width: parent.width
                text: qsTr("A directory containing music files belonging to different albums.")
                wrapMode: Text.WordWrap
                color: color_dark_gray
                font {
                    pixelSize: 14
                    family: "Inter"
                    weight: Font.Normal
                }
            }

            Text {
                width: parent.width
                text: qsTr("Suitable when your music files are all over the place 😅")
                wrapMode: Text.WordWrap
                color: color_grayish
                font {
                    pixelSize: 14
                    family: "Inter"
                    weight: Font.Normal
                }
            }
        }

        background: Rectangle {
            color: color_gray
            radius: 5
        }
    }

    Image {
        id: image
        width: 173; height: 66
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        source: "../images/cat_peek.png"
        fillMode: Image.PreserveAspectFit
    }
}
