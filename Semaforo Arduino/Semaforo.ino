int VERMELHO = 13;
int AMARELO = 12;
int VERDE = 11;


void setup() {                
  pinMode(VERMELHO, OUTPUT);
  pinMode(AMARELO, OUTPUT);
  pinMode(VERDE, OUTPUT);  
}

// the loop routine runs over and over again forever:
void loop() {
  digitalWrite(VERMELHO, HIGH);
  digitalWrite(AMARELO, LOW);
  digitalWrite(VERDE, LOW);  
  delay(12000);
  
  digitalWrite(VERMELHO, LOW);
  digitalWrite(AMARELO, HIGH);
  digitalWrite(VERDE, LOW);  
  delay(2000);


  digitalWrite(VERMELHO, LOW);
  digitalWrite(AMARELO, LOW);
  digitalWrite(VERDE, HIGH);  
  delay(20000);

}
