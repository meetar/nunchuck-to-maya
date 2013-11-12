nunchuck-to-maya
================

Connect a Wii Nunchuk to Maya via an Arduino

Simple proof of concept: A Wii Nunchuk controller connected to Maya via an Arduino, which sends the Nunchuk’s accelerometer data through the serial port. Maya uses PySerial to open the serial port, reads the data, and converts it to an attribute value.

You can see that the accelerometer has quite a lot of “ring” from sharp shocks.

I based this test on Tod Kurt’s [BlinkMChuck code](http://thingm.com/products/blinkm). The Nunchuk is connected to the Arduino with [this connector from Todbot](http://todbot.com/blog/2008/02/18/wiichuck-wii-nunchuck-adapter-available/).

And here’s a link to the setup required to configure pySerial: http://zoomy.net/2009/07/26/basic-arduino-to-maya-communication/
