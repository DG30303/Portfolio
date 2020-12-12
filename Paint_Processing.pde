float  S = 255;
float H=0;
float B= 255;
int h=0;
int t=225;
int colour= color(255,0,0);
int w=0;
int l=10;
int SX=100;
int BX=100;
int SIZE= 25;
float o= 1/2.0 * SIZE;
float p = 4/5.0 * SIZE;
int STAR= 0;
int PEN = 1;
int CUBE = 0;
int k=1;
void setup()
{
  fullScreen();
  noStroke();
  background(0);
  stroke(255);
  cube(132,962);
}

void draw()
{
  o= 1/2.0 * SIZE;
 p = 4/5.0 * SIZE; 

 noStroke();
   fill(55);
  ellipse(25,520,50,50);
  
  fill(55);
  ellipse(100,520,50,50);
  
  fill(55);
  ellipse(175,520,50,50);
  

stroke(255);
fill(0);
ellipse(220,180,50,50);

noStroke();
fill(H,S,B);
ellipse(220,580,50,50);


noStroke();
fill(0);
rect(0,650,285,80);

stroke(255);
fill(255);
ellipse(SX,690,50,50);

noStroke();
fill(0);
rect(0,760,285,93);

stroke(255);
fill(255);
ellipse(BX,790,50,50);

stroke(255);
noFill();
ellipse(45,885,50,50);
ellipse(150,885,50,50);

line(30,885,60,885);
line(135,885,165,885);
line(150,870,150,900);

stroke(255);
noFill();
ellipse(45,980,50,50);
ellipse(150,980,50,50);

stroke(255);
fill(55);
  ellipse(100,1050,50,50);

fill(255);
beginShape();
  vertex(45 + 25, 980);
  vertex(45 - 25, 980);
  vertex(45, 980 + 12.5);
 endShape();
  
  beginShape();
  vertex(45 + 12.5, 980 + 25);
  vertex(45, 980 - 20);
  vertex(45 - 12.5, 980 +25);
   vertex(45, 980 + 12.5);
 endShape();
  
  
  noFill();
 rect(132,962,25,25);
 rect(132+12.5,962+12.5,25,25);
 line(132,962,132+12.5,962+12.5);
 line(132,962+25,132+12.5,962+25+12.5);
 line(132+25,962,132+25+12.5,962+12.5);
 line(132+25,962+25,132+25+12.5,962+25+12.5);
  
  colorMode(HSB);
  while(h<=255)
  {
  stroke(h,255,255);
  line(5,t,255,t);
  h=h+1;
  t=t+1;
  }
  noStroke();
  h=0;
  t=225;
  
  while(w<=255)
  {
    stroke(w);
    line(5,l,255,l);
    w=w+2;
    l=l+1;
  }
 
  noStroke();
  w=0;
  l=10;
  
 
  
  if(mousePressed && mouseX> 285)
  {
    colorMode(HSB);
    fill (H,S,B);
    
 
  
  float i=0;
  
  if (PEN == 1)
  {
  while(i <= 1)
  {
    float x = pmouseX*i + mouseX*(1-i);
    float y = pmouseY*i + mouseY*(1-i);
    i = i+0.05;
    
    ellipse(x,y,SIZE,SIZE);
  }
  }
}
fill(255);
textSize(20);
text("C",17,525);

fill(255);
textSize(20);
text("B",94,525);

fill(255);
textSize(20);
text("P",169,525);

fill(255);
textSize(20);
text("S",95,1055);

textSize(50);
text("ERASER",10,200);

text("COLOR", 10, 600);
textSize(35);
text("SATURATION", 10, 650);

text("BRIGHTNESS", 10, 750);

text("PEN SIZE :" + SIZE, 10,850);


}




void keyPressed()
{
  if (key == 'r')
  {
  background(0);
}
}


void mouseClicked()
{
  if(STAR == 1 && mouseX> 285)
  {
    fill(H,S,B);
  star(mouseX,mouseY);
  }
  
  if(CUBE==1 && mouseX> 285)
  {
    stroke(H,S,B);
   cube(mouseX,mouseY); 
  }
  
   if (dist(mouseX,mouseY,25,520)<= 25)
  {
    background(0);
  }
  
  if (dist(mouseX,mouseY,100,520)<= 25)
  {
    background(colour);
  }
  
   if (dist(mouseX,mouseY,175,520)<= 25)
  {
    PEN= 1;
    STAR=0;
    CUBE=0;
  }
  
  if (dist(mouseX,mouseY,220,180)<= 25)
  {
    PEN= 1;
    STAR=0;
    CUBE=0;
  }
  
  if (dist(mouseX,mouseY,100,1050)<= 25)
  {
    save();
  }
  
  if ( mouseX >=5 && mouseX<=255 && mouseY >= 10 && mouseY<= 480)
  {
    colour=get(mouseX,mouseY);
  H=   hue(colour);
  S= saturation(colour);
  B= brightness(colour);
  
}


if(dist(mouseX,mouseY,45,885)<=25 )
{
 SIZE= SIZE-2; 
}


if(dist(mouseX,mouseY,150,885)<=25)
{
 SIZE= SIZE+2; 
}


if (SIZE<0)
{
  SIZE=1;
}


if (dist(mouseX,mouseY,45,980) <=25)
{
  PEN=0;
  STAR=1;
  CUBE=0;
}

if (dist(mouseX,mouseY,150,980)<=25)
{
  PEN=0;
  STAR=0;
  CUBE=1;
}


}

void mouseDragged()
{
  
  if (dist(mouseX,mouseY,SX,690)<=25 && mouseX> SX && mouseX<=255)
{
  
  SX= mouseX;
  S=SX;
}

 if (dist(mouseX,mouseY,SX,690)<=25 && mouseX< SX && mouseX>=25)
{
  
  SX= mouseX;
  S=SX;
}


 if (dist(mouseX,mouseY,BX,790)<=25 && mouseX> BX && mouseX<=255)
{
  
  BX= mouseX;
  B=BX;
}

 if (dist(mouseX,mouseY,BX,790)<=25 && mouseX< BX && mouseX>=25)
{
  
  BX= mouseX;
  B=BX;
}

}

void star(float a, float b)
{
  
  beginShape();
  vertex(a + SIZE, b);
  vertex(a - SIZE, b);
  vertex(a, b + o);
 endShape();
  
  beginShape();
  vertex(a + o, b + SIZE);
  vertex(a, b - p);
  vertex(a - o, b +SIZE);
   vertex(a, b + o);
 endShape();
}

void cube(float a, float b)
{
  noFill();
 rect(a,b,SIZE,SIZE);
 rect(a+o,b+o,SIZE,SIZE);
 line(a,b,a+o,b+o);
 line(a,b+SIZE,a+o,b+SIZE+o);
 line(a+SIZE,b,a+SIZE+o,b+o);
 line(a+SIZE,b+SIZE,a+SIZE+o,b+SIZE+o);
}


void save()
{
 save("C:\\Users\\0611032043\\Desktop\\myDrawing"+k+".jpg"); 
 
 k=k+1;
}

// beginShape();
  //vertex(a + SIZE, b);
 // vertex(a - SIZE, b);
  //vertex(a, b + o);
 // endShape();
  
 // beginShape();
  //vertex(a + o, b + SIZE);
 // vertex(a, b - p);
  //vertex(a - o, b +SIZE);
  // vertex(a, b + o);
 // endShape();
 
 
  //beginShape();
 //vertex(a + 10, b);
  //vertex(a - 10, b);
  //vertex(a, b + 5);
  //endShape();
  
  //beginShape();
 // vertex(a + 5, b + 10);
 // vertex(a, b - 8);
  //vertex(a - 5, b +10);
  // vertex(a, b + 5);
 // endShape();