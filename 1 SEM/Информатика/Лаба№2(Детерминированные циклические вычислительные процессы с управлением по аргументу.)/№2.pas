program pr2;
var
  Q,λ:integer;
  y,a,b,c:real;
begin
  a:=13.5;
  λ:=3;
  for Q:=0 to 90 do
  begin
    b:=((Pi*a)/λ)*cos(Q);
    c:=(Pi/2)*(Pi/2);
    y:=((1+sin(Q))*cos(b))/(c-(b*b));
    writeln(y);
  end;
end.