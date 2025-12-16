program pr1;
var R,C,E,Uv,Uvh,h,t,a:real;
begin
  R:=2;
  C:=0.01;
  E:=0.001;
  Uv:=50;
  t:=0.01;
  h:=0.01;
  a:=R*C;
  repeat
    Uvh:=Uv*(1-exp(-t/a));
    writeln('t =',t:0:2,'Uвых =',Uvh:0:6);
    t:=t+h;
  until (abs(Uvh-Uv)<E);
end.