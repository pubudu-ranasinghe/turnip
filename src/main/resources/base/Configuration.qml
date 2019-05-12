import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.3

Window {
    id: configWindow
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

    width: 360
    height: 480
    title: qsTr("Edit Configuration")

    Text {
        id: headerText

        text: qsTr("Configure")
        x: 20; y: 36
        font {
            pixelSize: 28
            family: "Inter"
            weight: Font.Bold
            letterSpacing: -1.4
        }

    }

    Column {
        x: 20; y: 102
        spacing: 8

        Text {
            id: libraryPathLabel

            text: qsTr("Library Path")
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
        }

        Row {
            spacing: 15

            CustomTextField {
                id: libraryPathInput

                width: 255
                text: config.libraryPath
                enabled: false
            }

            CustomButton {
                id: libraryPathInputBtn

                width: 50; height: 50
                backgroundColor: color_gray

                onClicked: libraryPathDialog.open()
            }
        }
    }

    Column {
        x: 20; y: 196
        spacing: 8

        Text {
            id: configPathLabel

            text: qsTr("Config File")
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
        }

        CustomTextField {
            id: configPathInput

            width: 320
            text: config.configPath
            enabled: false
        }
    }

    Item {
        id: element
        x: 20; y: 290
        width: 320; height: 79

        CustomSwitch {
            id: isCopyControl

            text: (isCopyControl.checked ? "Copy" : "Move") + qsTr(" Files")
            anchors.verticalCenter: parent.verticalCenter
            checked: config.isCopy
            onToggled: {
                config.setIsCopy(isCopyControl.checked)
            }
        }
    }


    CustomButton {
        id: saveButton

        x: 20; y: 407
        width: 120; height: 50
        text: "Save"
        backgroundColor: color_gray
        onClicked: {
            config.save()
            configWindow.close()
        }
    }

    CustomButton {
        id: cancelButton

        x: 155; y: 407
        width: 120; height: 50
        text: "Cancel"
        backgroundColor: color_gray
        onClicked: {
            configWindow.close()
        }
    }

    FileDialog {
        id: libraryPathDialog
        title: qsTr("Select Library Folder")
        selectFolder: true
        selectMultiple: false
        onAccepted: {
            config.setLibraryPath(libraryPathDialog.fileUrl)
        }
    }
}
