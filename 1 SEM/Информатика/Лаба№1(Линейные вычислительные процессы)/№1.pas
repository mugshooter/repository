program pr1;
var
  a, b, g : integer;
  c : real;
begin
  writeln('Введите значение переменных a,b');
  readln(a, b);
  g := a + b;
  c := (a + abs(b - sin(g))) / (3 - abs(b + ln(g) / (1 + sin(g))));
  write(c);
end.