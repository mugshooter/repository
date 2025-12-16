program pr3;
var e,U,S,x,M:real;
k:integer;
begin
  e:=0.0001;
  x:=pi/6;
  U:=1;
  S:=1;
  k:=1;
  repeat
    M:=-(x*x)/(4*k*k-2*k);
    U:=U*M;
    S:=S+U;
    k:=k+1;
  until abs(U)<=e;
  writeln(S);
end.