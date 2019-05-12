import QtQuick 2.12
import QtQuick.Controls 2.12

Switch {
    id: control

    text: qsTr("Switch")
    checked: false
    spacing: 8
    font {
        pixelSize: 18
        family: "Inter"
        weight: Font.Normal
    }

    indicator: Rectangle {
        implicitWidth: 60
        implicitHeight: 30
        x: control.leftPadding
        y: parent.height / 2 - height / 2
        radius: 15
        color: control.checked ? color_primary : color_gray

        Rectangle {
            x: control.checked ? parent.width - width - 3 : 3
            y: 3
            width: 24
            height: 24
            radius: 12
            color: "#ffffff"
        }
    }

    contentItem: Text {
        text: control.text
        font: control.font
        opacity: enabled ? 1.0 : 0.3
        color: color_black
        verticalAlignment: Text.AlignVCenter
        leftPadding: control.indicator.width + control.spacing
    }
}
