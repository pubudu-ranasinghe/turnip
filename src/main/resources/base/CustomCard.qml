import QtQuick 2.12
import QtQuick.Controls 2.12

Rectangle {
    id: control

    property alias primaryText: primaryText.text
    property alias secondaryText1: secondaryText1.text
    property alias secondaryText2: secondaryText2.text
    property alias image: image.source

    radius: 5
    color: color_white_two

    Image {
        id: image
        source: "images/placeholder.png"
        height: parent.height
        width: parent.height
    }

    Column {
        x: control.height + 20
        spacing: 5
        anchors.verticalCenter: parent.verticalCenter

        Text {
            id: primaryText
            text: "Placeholder"
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
            color: color_black
        }

        Text {
            id: secondaryText1
            text: "Placeholder"
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
            color: color_grayish
        }

        Text {
            id: secondaryText2
            text: "Placeholder"
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
            color: color_grayish
        }
    }

}
