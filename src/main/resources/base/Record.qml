import QtQuick 2.12

Rectangle {
    color: "#fafafa"
    width: 100
    height: 100
    Image {
        source: portrait
        anchors.horizontalCenter: parent.horizontalCenter
    }
    Text {
        text: name
        anchors.horizontalCenter: parent.horizontalCenter
    }
}
