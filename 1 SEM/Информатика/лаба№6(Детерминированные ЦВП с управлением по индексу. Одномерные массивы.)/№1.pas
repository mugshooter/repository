program pr1;
const
  F:array[1..5] of real = (3.5,8,13.5,20,47);
var
  i:integer;
  R,L,C,Z,J,Xc,Xl:real;
begin
  R:=2;
  C:=0.0000078;
  L:=0.1;
  for i:=1 to 5 do begin 
    Xc:=1/(2*Pi*F[i]*C);
    Xl:=2*Pi*F[i]*L;
    Z:=(Xc*sqrt((Xl*Xl)+(R*R)))/(sqrt((R*R)+((Xl-Xc)*(Xl-Xc))));
    J:=arctan((Xl/R)-((Xl*Xl)/(R*Xc))-(R/Xc));
    writeln('Частота F=',F[i],' ','Реактивное сопротивление колеб. контура Z=',Z,'  ','фазовый угол J=',J)
    end;
end.