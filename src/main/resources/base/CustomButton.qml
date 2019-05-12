import QtQuick 2.12
import QtQuick.Controls 2.12

Button {
    id: control

    FontLoader {
        id: interBold
        source: "../fonts/Inter-Bold.ttf"
    }

    FontLoader {
        id: interRegular
        source: "../fonts/Inter-Regular.ttf"
    }

    property string color_primary: "#fcd307"
    property string color_black: "#1b1919"
    property alias buttonText: label.text
    property alias backgroundColor: background.color
    property alias textcolor: label.color

    contentItem: Text {
        id: label
        text: control.text
        font {
            pixelSize: 18
            family: "Inter"
            weight: Font.Normal
        }
        opacity: enabled ? 1.0 : 0.3
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
    }

    background: Rectangle {
        id: background
        implicitWidth: 100
        implicitHeight: 40
        opacity: enabled ? 1 : 0.3
        radius: 5
    }
}
