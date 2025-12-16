program pr3;
var
  Q,n,h:integer;
  a,λ,y:real;
begin
  a:=13.5;
  λ:=3;
  n:=0;
  h:=5;
  Q:=0;
  while n<20 do
  begin
    n:=n+1;
    y := (1 + sin(Q)) * cos(Pi*a/λ*cos(Q))/((Pi/2)*(Pi/2) - (Pi*a/λ*cos(Q))*(Pi*a/λ*cos(Q)));
    writeln(n,' ',Q,' ',y);
    Q:=Q+h;
  end;
end.