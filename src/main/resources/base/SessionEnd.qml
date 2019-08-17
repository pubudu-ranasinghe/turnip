import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.5

Window {
    id: sessionEndWindow

    property int track_count: 0

    width: 360
    height: 480
    title: qsTr("Import Complete")
    flags: Qt.Dialog
    modality: Qt.ApplicationModal

    Image {
        id: successImage
        x: 103; y: 80
        width: 155; height: 218
        source: "images/success.png"
    }

    Text {
        text: "Successfully imported " + track_count + " tracks to library"
        anchors.horizontalCenter: parent.horizontalCenter
        horizontalAlignment: Text.AlignHCenter
        y: 333
        width: 274
        font {
            pixelSize: 18
            family: "Inter"
            weight: Font.Normal
        }
        wrapMode: Text.WordWrap
        color: color_black
    }

    CustomButton {
        id: okButton

        y: 410
        width: 155; height: 50
        text: qsTr("Ok")
        anchors.horizontalCenter: parent.horizontalCenter
        backgroundColor: color_gray
        onClicked: {
            sessionEndWindow.close()
        }
    }

}
