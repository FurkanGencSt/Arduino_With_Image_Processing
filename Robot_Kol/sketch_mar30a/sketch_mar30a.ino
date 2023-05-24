#include <Servo.h>


// Zemindeki servo motor.
Servo servoMotor_1;
Servo servoMotor_2;
Servo servoMotor_3;
Servo servoMotor_4;
long randNumber;

const byte potansiyometre = A0;
int potansiyometre_deger;

void setup() {
  Serial.begin(9600);
  // servoMotor_1.attach(2); // zemin
  // servoMotor_2.attach(3); // gövde hareket
  servoMotor_3.attach(4); // elin dirseği
  // servoMotor_4.attach(5); //elin hareket eden kısmı



}

void loop() {

  if (Serial.available() > 0) { // Seri haberleşmeden veri var mı diye kontrol et
    int value = Serial.read(); // Gelen veriyi oku
    if (value == '1') { // Eğer gelen veri '1' ise
      randNumber = random(150);
      	servoMotor_4.write(randNumber); //Robot elin hereket eden kısmı 0-180 arasında olacak. 180 açık hali 0 ise bir şeyi tutarken ki hali olacak.

    }
  }
	
	// servoMotor_1.write(90);
	// servoMotor_2.write(150); // Elin dirseğinin hareketini sağlayacak kısım. 95-180 arasında çalışacak. 180 olduğunda dirsaek tavana doğru yükselir. 95 olduğunda dirsek zemine doğru iner.
	servoMotor_3.write(90);   // Bu, elin hareketini belirleyecek dirsek kısmı. 0-180 arasında gidecek. 90 olduğunda eli dik olarak havaya kaldıracak şekilde olacak. Tahminimce 0-45 aralığında kullanıcaz. Düz Hali 90, Default hali ise 120
	// servoMotor_4.write(0); //Robot elin hereket eden kısmı 0-180 arasında olacak. 180 açık hali 0 ise bir şeyi tutarken ki hali olacak.


}
