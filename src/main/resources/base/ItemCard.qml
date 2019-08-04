import QtQuick 2.12
import QtQuick.Controls 2.12
import "js/itemHelper.js" as ItemHelper

Rectangle {
    id: control

    property string color_primary: "#fcd307"
    property string color_black: "#1b1919"
    property string color_gray: "#ececec"
    property string color_grayish: "#aeabab"
    property string color_dark_gray: "#4e4747"
    property string color_white_two: "#fafafa"

    property var itemData: ({
        title: "New Divide",
        artist: "Linkin Park"
    })

    width: 250; height: 580
    color: color_gray

    Image {
        x: 20; y: 20
        width: 210; height: 210
        source: "images/placeholder.png"
    }

    Column {
        x: 20; y: 250
        spacing: 5

        Text {
            text: itemData.title
            font {
                pixelSize: 18
                family: "Inter"
                weight: Font.Normal
            }
            color: color_black
        }

        Repeater {
            model: ItemHelper.getItemKeys(itemData)

            Text {
                text: modelData
                font {
                    pixelSize: 18
                    family: "Inter"
                    weight: Font.Normal
                }
                color: color_grayish
            }
        }

    }
}
