/*

Texting Christmas Tree receiver code
Controls the color of Christmas tree lights

Based on "Tweeting Christmas Tree", http://www.instructables.com/id/Tweeting-Christmas-Tree/, used under a Creative Commons Attribution Non-commercial ShareAlike license: http://creativecommons.org/licenses/by-nc-sa/3.0/.

*/

int sentDat;
int led1 = 4;

int led2 = 5;

int led3 = 6;

int led4 = 7;

void setup() {
  Serial.begin(9600);   
  pinMode(led1, OUTPUT);   
  pinMode(led2, OUTPUT);    
  pinMode(led3, OUTPUT);    
  pinMode(led4, OUTPUT); 
}

void loop() {
  if (Serial.available() > 0) {
	sentDat = Serial.read(); 

        //red control
	if(sentDat == 'a'){
  	  digitalWrite(led1, HIGH);
	}else if(sentDat == 'b'){
  	  digitalWrite(led1, LOW);
	}


        //red control
	if(sentDat == 'c'){
  	  digitalWrite(led2, HIGH);
	}else if(sentDat == 'd'){
  	  digitalWrite(led2, LOW);
	}


        //red control
	if(sentDat == 'e'){
  	  digitalWrite(led3, HIGH);
	}else if(sentDat == 'f'){
  	  digitalWrite(led3, LOW);
	}


        //red control
	if(sentDat == 'g'){
  	  digitalWrite(led4, HIGH);
	}else if(sentDat == 'h'){
  	  digitalWrite(led4, LOW);
	}

  }
}



