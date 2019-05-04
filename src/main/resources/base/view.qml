import QtQuick 2.2
import QtQuick.Window 2.2

Window {
    id: mainWindow
    visible: true
    width: 640
    height: 480
    title: qsTr("Beets UI")

    Rectangle {
        anchors.fill: parent

        color: "#ff5959"

        Text {
            text: "Hello World"
            color: "White"
            anchors.centerIn: parent
        }
    }
}