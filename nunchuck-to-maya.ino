/*
 * Based on BlinkMChuck (c) 2008 Tod E. Kurt, http://thingm.com/
*/

#include "Wire.h"
#include "BlinkM_funcs.h"
#include "nunchuck_funcs.h"

int blinkm_addr = 0x09; // the address of our BlinkM
int loop_cnt=0;
byte hue, bri;
#define BLINKM_ARDUINO_POWERED 1

void setup() {
    Serial.begin(19200);
    if( BLINKM_ARDUINO_POWERED ) {
        BlinkM_beginWithPower();
    } else {
        BlinkM_begin();
    }
    nunchuck_init(); // send the initilization handshake
}

void loop() {
    if( loop_cnt > 5 ) { // every 50 msecs get new data
        loop_cnt = 0;
        if( ! nunchuck_get_data() ) { 
            Serial.println("error getting nunchuck data");
        }
        hue  = nunchuck_accelx(); // ranges from approx 70 - 182
        bri  = nunchuck_accely(); // ranges from approx 65 - 173

        Serial.print( hue,DEC); Serial.print( ";" );
        Serial.println( bri,DEC);
    }
    loop_cnt++;
    delay(10);
}