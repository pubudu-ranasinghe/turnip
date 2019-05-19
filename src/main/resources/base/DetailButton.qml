import QtQuick 2.12
import QtQuick.Controls 2.12

Button {
    id: control

    property alias primaryText: primaryText.text
    property alias primaryTextcolor: primaryText.color
    property alias backgroundColor: background.color
    property alias image: image.source

    contentItem: Text {
        id: primaryText
        font {
            pixelSize: 18
            family: "Inter"
            weight: Font.Normal
        }
        x: control.height + 20
        verticalAlignment: Text.AlignVCenter
    }

    background: Rectangle {
        id: background
        implicitWidth: 100
        implicitHeight: 40
        opacity: enabled ? 1 : 0.3
        radius: 5

        Image {
            id: image
            source: "file"
            height: parent.height
            width: parent.height
        }
    }
}
