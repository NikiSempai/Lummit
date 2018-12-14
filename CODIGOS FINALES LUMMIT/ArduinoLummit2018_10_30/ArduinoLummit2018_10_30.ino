/* Codigo de recepcion por puerto serial de un string de la forma @XXXXX
 * Las primeras dos XX corresponde a un valor de led entre 0-65535  el cual corresponde al numero de led a usar
 * luego las siguentes tres X,X,X cada X es un entero de 0-255  de formato RGB
 * Las Leds no se modificaran hasta enviar el comando Send
 */

#include <FastLED.h>
#define NUM_LEDS 1800                                               
#define DATA_PIN 7
#define BUFFERSIZE 6

int count = 0;
  
// Define the array of leds
CRGB leds[NUM_LEDS];                                                                                                                      
byte SerialBuffer[BUFFERSIZE];

//INICIALIZACIONES
void setup() {
  FastLED.addLeds<WS2812, DATA_PIN, GBR>(leds, NUM_LEDS);
  Serial.begin(230400);
  Serial.setTimeout(50);    //50ms por las dudas nunca deberiamos usarlo
  
}


void loop() {  
  while (Serial.available()) 
  {
        Serial.readBytes(SerialBuffer,BUFFERSIZE);
        if(SerialBuffer[0] == '@')      //verificacion
            {                                      
            leds[((SerialBuffer[1])*256 + (SerialBuffer[2]))] = CRGB((SerialBuffer[3]), (SerialBuffer[4]), (SerialBuffer[5]));                    //carga en el string led el el nuevo valor 
            }
        else if((SerialBuffer[0] == 'S')&&(SerialBuffer[1] == 'e')&&(SerialBuffer[2] == 'n')&&(SerialBuffer[3] == 'd'))   //espera un send para enviar para no estar mandando todo el estring por cada cambio de led
            {
            FastLED.show();                                                         //enviar comando de la led
            //delay(80);                                                              //80ms delay para esperar 800 leds
            }
        else{
          //Serial.println("error comand");                   
      }                                             
  }
    
  
}
