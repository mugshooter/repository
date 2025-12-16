program pr2;
const n=4;
type mas=array[0..n]of byte;
function calcGorner(x:real;z:mas):real;
var i:byte;
    d:real;
begin
d:=0;
for i:=0 to n do
d:=d*x+z[i];
calcGorner:=d
end;
var a,b:mas;
    x:real;
    i:byte;
begin
write('x=');

readln(x);
writeln('Введите коэффициенты ');
for i:=0 to n do
 begin
  write(i +1, ' = ');
  readln(a[i]);
 end;
writeln('Значение многочлена y=',calcGorner(x,a):0:2);
readln
end.