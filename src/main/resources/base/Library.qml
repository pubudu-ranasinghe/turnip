import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Controls 2.3

Window {
    id: libraryWindow
    width: 640
    height: 480
    title: qsTr("Library")
    visible: true

    Column {
        id: row
        anchors.fill: parent
        anchors.margins: 20
        spacing: 20

        Text {
            id: libraryHeading
            text: qsTr("Music Library")
            font.pixelSize: 24
        }

        Row {
            spacing: 20

            Column {
                spacing: 5

                KeyValue {
                    keyText: qsTr("Total Tracks")
                    valueText: "0"
                }

                KeyValue {
                    keyText: qsTr("Albums")
                    valueText: "0"
                }
                
                KeyValue {
                    keyText: qsTr("Album Artists")
                    valueText: "0"
                }
            }
            Column {
                KeyValue {
                    keyText: qsTr("Total Time")
                    valueText: "0.0 seconds"
                }

                KeyValue {
                    keyText: qsTr("Approximate Total Size")
                    valueText: "0.0 B"
                }
            }
        }
    }
}
