import QtQuick 2.12
import QtQuick.Controls 2.12

Button {
    id: control

    property alias primaryText: primaryText.text
    property alias secondaryText1: secondaryText1.text
    property alias secondaryText2: secondaryText2.text
    property alias primaryTextcolor: primaryText.color
    property alias backgroundColor: background.color
    property alias image: image.source

    contentItem: Item {
        id: element
        implicitWidth: 200
        implicitHeight: 110
        Column {
            anchors.verticalCenter: parent.verticalCenter
            Text {
                id: primaryText
                font {
                    pixelSize: 18
                    family: "Inter"
                    weight: Font.Normal
                }
                leftPadding: control.height + 15
            }
            Text {
                id: secondaryText1
                font {
                    pixelSize: 18
                    family: "Inter"
                    weight: Font.Normal
                }
                color: color_grayish
                leftPadding: control.height + 15
            }
            Text {
                id: secondaryText2
                font {
                    pixelSize: 18
                    family: "Inter"
                    weight: Font.Normal
                }
                color: color_grayish
                leftPadding: control.height + 15
            }
        }
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
