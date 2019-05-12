import QtQuick 2.12
import QtQuick.Controls 2.12

TextField {
    id: control

    placeholderText: qsTr("Enter description")
    font {
        pixelSize: 16
        family: "Inter"
        weight: Font.Normal
    }
    color: color_dark_gray
    background: Rectangle {
        implicitWidth: 200
        implicitHeight: 50
        color: color_gray
        radius: 5
    }
}
