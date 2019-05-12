import QtQuick 2.12
import QtQuick.Controls 2.12

TextField {
    id: control

    property string color_primary: "#fcd307"
    property string color_black: "#1b1919"
    property string color_gray: "#ececec"
    property string color_dark_gray: "#4e4747"

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
