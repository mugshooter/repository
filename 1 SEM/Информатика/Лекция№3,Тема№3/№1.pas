program pr3;
var
  Q:integer;
  a,λ,y:real;
begin
  a:=13.5;
  λ:=3;
  for Q:=0 to 90 do begin
    if(Q mod 5) = 0 then
    begin
      y := (1 + sin(Q)) * cos(Pi*a/λ*cos(Q))/((Pi/2)*(Pi/2) - (Pi*a/λ*cos(Q))*(Pi*a/λ*cos(Q)));
      writeln(Q,' ',y);
    end;
  end;
end.