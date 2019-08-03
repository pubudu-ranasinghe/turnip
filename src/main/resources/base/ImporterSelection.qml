import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.3

Window {
    id: importerSelectionWindow
    visible: true

    width: 360
    height: 480
    title: qsTr("Select Import Mode")
    modality: Qt.ApplicationModal

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

        onClicked: importPathDialog.open()
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

        onClicked: importPathDialog.open()
    }

    Image {
        id: image
        width: 173; height: 66
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottom: parent.bottom
        source: "images/cat_peek.png"
        fillMode: Image.PreserveAspectFit
    }

    FileDialog {
        id: importPathDialog
        title: qsTr("Select Import Folder")
        selectFolder: true
        onAccepted: {
            var component = Qt.createComponent("Importer.qml");
            var importerWindow = component.createObject(mainWindow);
            importerWindow.show();
            importer.startSession(importPathDialog.fileUrl)
        }
    }
}
