   { Демонстрация шифрования и дешифрования }
   { шифра Цезаря                           }
   { ************************************** }
   PROGRAM Sh_Dsh;
      Uses CRT;

   { ------------------------------------------- }
   { Создание файла, содержащего ключ шифрования }
   { ------------------------------------------- }
   PROCEDURE Key;
      var n: Integer;
          f: File of Integer;
   BEGIN
      Assign(f,'N.KEY'); Rewrite(f);
      Write('Введите ключ (смещение): '); ReadLn(n);
      Write(f,n); Close(f)
   END;

   { ----------------- }
   { Шифрование текста }
   { ----------------- }
   PROCEDURE Sekret;
      var slovo, anslovo: Array [1..20] of String [100];
          alfavit       : STRING [34];
          j,n,m,i,k,p   : Integer;
          fkl           : File OF Integer;
          fs            : Text;
   BEGIN
      alfavit:='абвгдеёжзийклмнопрстуфхцчшщъыьэюя ';
      Assign(fkl,'N.key');
      ReSet(fkl); Read(fkl,n); Close(fkl);
      Write('Введите текст: '); ReadLn(slovo[1]);
      j:=1;
      While Slovo[j]<>'' do
        begin j:=j+1; ReadLn(Slovo[j]) end;
      m:=j-1;
      For j:=1 to m do
        begin
          anslovo[j] := '';
          For k:=1 to Length(slovo[j]) do
            For i:=1 to 34 do
              If slovo[j][k]=alfavit[i]
                then begin
                       p:=i+n;
                       IF p>34
                         then p:=p MOD 34;
                       anslovo[j]:=anslovo[j]+alfavit[p]
                     end;
        end;
      Assign(fs,'Shifr.txt'); Rewrite(fs);
      For j:=1 to m do
        WriteLn(fs,anslovo[j]);
      Close(fs);
      Write('Зашифрованный текст: ');
      For i:=1 to m do
        WriteLn(anslovo[i])
   END;

   { ------------------- }
   { Дешифрование текста }
   { ------------------- }
   PROCEDURE RetSek;
      var slovo,anslovo: Array[1..20] of String[100];
          alfavit      : String[34];
          n,j,i,k,p,m  : Integer;
          fi           : File of Integer;
          f            : Text;
   BEGIN
      alfavit:='абвгдеёжзийклмнопрстуфхцчшщъыьэюя ';
      Assign(fi,'N.key');
      Reset(fi); Read(fi,n); Close(fi);
      Assign(f,'Shifr.txt'); Reset(f);
      j:=1;
      While NOT EOF(f) do
        begin ReadLn(f,anslovo[j]); j:=j+1 end;
      m:=j-1;
      Close(f);
      For j:=1 to m do
        begin
          slovo[j] := '';
          For k:=1 TO Length (anslovo[j]) do
            For i:=1 to 34 do
              If anslovo[j][k]=alfavit[i]
                then begin
                       p:=i-n;
                       If p<1
                         then p:=34+p MOD 34;
                       slovo[j]:=slovo[j]+alfavit[p]
                     end
        end;
      WriteLn; Write('Текст шифровки: ');
      For j:=1 to m do
        WriteLn(Slovo[j]);
   END;
  { --- }
   BEGIN
      ClrScr; Key; Sekret; RetSek;
      ReadLn
   END.
