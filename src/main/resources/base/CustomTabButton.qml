import QtQuick 2.12
import QtQuick.Controls 2.12

TabButton {
    id: control

    contentItem: Text {
        id: label
        text: control.text
        font {
            pixelSize: 22
            family: "Inter"
            weight: Font.Normal
        }
        opacity: enabled ? 1.0 : 0.3
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        color: checked ? color_primary : color_gray
    }

    background: Rectangle {
        id: background
        color: "#fff"
    }
}
