import QtQuick 2.12

Rectangle {
    id: control

    property string color_primary: "#fcd307"
    property string color_black: "#1b1919"
    property string color_gray: "#ececec"

    width: 100
    height: 150

    Image {
        id: image
        width: 100
        height: 100
        source: portrait
        anchors.horizontalCenter: parent.horizontalCenter
    }

    Text {
        text: name
        x: 2; y: 105
        font {
            pixelSize: 14
            family: "Inter"
            weight: Font.Normal
        }
        color: color_black
    }

    Text {
        text: extra ? extra : ""
        x: 2; y: 125
        font {
            pixelSize: 12
            family: "Inter"
            weight: Font.Normal
        }
        color: color_grayish
    }
}
