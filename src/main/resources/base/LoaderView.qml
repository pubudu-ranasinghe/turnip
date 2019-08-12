import QtQuick 2.12
import QtQuick.Controls 2.12

Item {
    id: control

    width: parent.width; height: parent.height

    Rectangle {
        id: loadingBackground
        anchors.fill: parent
    }

    Image {
        id: loadingImage
        width: 70
        anchors.bottom: loadingText.top
        anchors.bottomMargin: 10
        anchors.horizontalCenter: parent.horizontalCenter
        fillMode: Image.PreserveAspectFit
        source: "images/loading.png"
    }

    Text {
        id: loadingText
        text: qsTr("Loading")
        anchors.verticalCenter: parent.verticalCenter
        anchors.horizontalCenter: parent.horizontalCenter
        font {
            pixelSize: 28
            family: "Inter"
            weight: Font.Bold
        }
        color: color_black
    }
}
