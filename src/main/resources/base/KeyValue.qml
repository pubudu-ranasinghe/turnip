import QtQuick 2.12
import QtQuick.Controls 2.3

Row {
    spacing: 5

    property alias keyText: key.text
    property alias valueText: value.text

    Label {
        id: key
        text: "Key"
    }

    Label {
        id: value
        text: "Value"
    }
}