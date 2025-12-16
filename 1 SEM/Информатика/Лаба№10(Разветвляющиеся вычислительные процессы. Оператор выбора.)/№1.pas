program pr1;
var
  λ,D,fi,A,c,s:real;
begin
  λ:=0.1;
  D:=30*pi/180;
  fi:=45*pi/180;
  s:=(cos(fi)*sin(λ))/sin(D);  
  c:=(sin(fi)-(sin(fi)*cos(D)))/(cos(fi)*sin(D));
  A:= arcsin(cos(fi)*(sin(λ)/sin(D)));
  if (s>0) and (c>0) then
  begin
    A:= abs(A);
    writeln('1 координатная четверть');
  end
  else
    if (s>0) and (c<0) then
    begin
      A:=pi- abs(A);
      writeln('2 координатная четверть');
    end
  else
    if (s<0) and (c<0) then
      begin
      A:=pi+abs(A);
    writeln('3 координатная четверть');
      end
  else
    if (s<0) and (c>0) then
    begin
      A:=2*pi-abs(A);
      writeln('4 координатная четверть');
    end;
    writeln(A);
end.