import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 400
    height: 600
    x: width - 12
    y: height - 48

    title: "Clock"
    flags: Qt.FramelessWindowHint | Qt.Window
    property string currTime: "00:00:00"
    property QtObject backend

    Connections {
        target: backend
        function onUpdated(msg) {
        currTime = msg;
    }
    }

    Image {
            anchors.fill: parent
            source: "./images/background.png"
            fillMode: Image.PreserveAspectCrop
        }


    Rectangle {
            anchors.fill: parent
            color: "transparent"

            Text {
                anchors{
                    bottom: parent.bottom
                    bottomMargin: 12
                    left: parent.left
                    leftMargin: 12
                }
                text: currTime // used to be; text: "16:38:33"
                font.pixelSize: 48
                color: "white"
            }

        }


}

