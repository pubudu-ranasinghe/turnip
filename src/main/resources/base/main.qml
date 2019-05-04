import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5

QtObject {
    property var mainWindow: Window {
        id: mainWindow
        visible: true
        width: 360
        height: 440
        title: qsTr("Beets UI")

        Rectangle {
            anchors.fill: parent
            color: "#ff5959"

            Button {
                id: importBtn
                width: 320
                height: 120
                x: 20; y: 20
                text: qsTr("Import")
                spacing: -1
                font.family: "Arial"
                font.pointSize: 12
            }
            Button {
                id: libraryBtn
                width: 320
                height: 120
                x: 20; y: 160
                text: qsTr("My Library")
                font.pointSize: 12
            }
            Button {
                id: configBtn
                width: 320
                height: 120
                x: 20; y: 300
                text: qsTr("Configuration")
                font.pointSize: 12
                onClicked: configWindow.visible = true
            }
        }
    }

    property var configWindow: Configuration {}
}