program pr2;
var n,i,j:integer;
begin
  writeln(' Введите число');
  readln(n);
  i:= n mod 10;
  j:= n mod 100;
  if (j=11) or (j=12) or (j=13) or (j=14) then writeln ('Ворон')
  else
    case i of
      0,1,2:writeln('Ворона');
      3,4,5:writeln('Вороны');
      6,7,8,9:writeln('Ворон');
    end;
end.