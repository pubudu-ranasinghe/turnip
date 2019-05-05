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
                    valueText: library.stats.trackCount
                }

                KeyValue {
                    keyText: qsTr("Albums")
                    valueText: library.stats.albums
                }
                
                KeyValue {
                    keyText: qsTr("Artists")
                    valueText: library.stats.artists
                }
            }
            
            Column {
                spacing: 5

                KeyValue {
                    keyText: qsTr("Total Time")
                    valueText: library.stats.totalTime
                }

                KeyValue {
                    keyText: qsTr("Approximate Total Size")
                    valueText: library.stats.totalSize
                }
            }
        }
    }
}
