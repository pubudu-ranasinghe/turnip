import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5
import QtQuick.Dialogs 1.3

Window {
    width: 420
    height: 480
    visible: true
    title: qsTr("Edit Configuration")

    Column {
        id: element
        spacing: 10
        anchors.margins: 20
        anchors.fill: parent

        Label {
            id: configPathLabel
            width: parent.width
            text: qsTr("Configuration File Location")
        }

        Label {
            id: configPathHelpLabel
            width: parent.width
            text: qsTr("This is the configuration file used by Beets. Some of the configuration options can be set below. You can edit the full configuration by directly opening it with a text editor.")
            color: "#bbb"
            wrapMode: Text.WordWrap
        }

        TextField {
            id: configPathInput
            width: parent.width
            text: config.configPath
            enabled: false
        }

        Label {
            id: libraryPathLabel
            width: parent.width
            text: qsTr("Library Location")
        }

        Label {
            id: libraryPathHelpLabel
            width: parent.width
            text: qsTr("Location of the destination library. This is where autotagged and organized files will be saved to.")
            wrapMode: Text.WordWrap
            color: "#bbb"
        }

        TextField {
            id: libraryPathInput
            width: parent.width
            text: config.libraryPath
            enabled: false
        }

        Button {
            text: "Change"
            onClicked: libraryPathDialog.open()
        }

        Label {
            id: isCopyControlHelp
            width: parent.width
            text: qsTr("If enabled the the original files will be autotagged and copied to the library. Otherwise original file will be moved to library")
            wrapMode: Text.WordWrap
            color: "#bbb"
        }

        Switch {
            id: isCopyControl
            text: (isCopyControl.checked ? "Copy" : "Move") + qsTr(" Files")
            checked: true
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
