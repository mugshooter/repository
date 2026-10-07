   { Демонстрация программы, позволяющей установить }
   { цифровую подпись Вашей программы.              }
   { Автор программы: Бройтман Д.Э.                 }
   { -----------------------------------------------}
   PROGRAM Copyr;
      Uses CRT;
      var f     : Text;
      CopyRight,
      FileName  : String;
      V         : Array[1..80] of Byte; 
                        { Зашифрованный автограф      }
      VL        : Byte; { Длина строки автографа      }
      W         : Word; { Контрольная сумма автографа }
  { ------------------------------------------------- }
   PROCEDURE Crypt;
   { Процедура шифрования строки автографа }
      var i: Byte;
   BEGIN
      VL:=Length(CopyRight);
      For i:=1 to VL do
        V[i]:=Ord(CopyRight[i])-i
   END;
  { ------------------- }
   PROCEDURE CheckSum;
   { Подсчет контрольной суммы строки автографа }
      var i: Byte;
   BEGIN
      W:=0;
      For i:=1 to VL do
        W:=W+Ord(CopyRight[i])
   END;
  { -------------- }
   Var i,j,M: Byte;
   BEGIN
      TextColor(Yellow);
      Write('Введите имя создаваемого файла: ');
      TextColor(LightGreen); ReadLn(FileName);
      Assign(f,FileName);
      {$i-} Rewrite(f); {$i+}
      If IOResult<>0
        then begin
               TextColor(LightRed); WriteLn;
               WriteLn('Ошибка создания файла');
               TextColor(LightBlue); Halt(3)
             end;
      WriteLn;
      TextColor(Yellow); Write('Ваш автограф : ');
      TextColor(LightGreen); ReadLn(Copyright);
      Crypt;
      CheckSum;
      { ------------------------------- }
      WriteLn(f,' PROCEDURE Copyright;');
      WriteLn(f,' { ',CopyRight,' }');
      WriteLn(f,'   type AA=Array[1..',VL,'] of Byte;');
      Write  (f,'   const CopyR: AA=(');
      j:=0;
      For i:=1 to VL do
        begin
          If J=0
            then Write(f,'');
          Write(f,' ',V[i]:4);
          IF i<VL
            then Write(f,',');
          Inc(j);
          IF j>6
            then begin WriteLn(f); J:=0 end
        end;
      WriteLn(f,');');
      WriteLn(f,'         CheckSum= ', W,';');
      WriteLn(f,'    var i,j: Byte; W: Word;');
      WriteLn(f,' BEGIN');
      WriteLn(f,'    W:=0;');
      WriteLn(f,'    For i:=1 to ',VL,' do');
      WriteLn(f,'      begin');
      WriteLn(f,'        j:=CopyR[i]+i;');
      WriteLn(f,'        W:=W+J;');
      WriteLn(f,'        Write(Chr(j))');
      WriteLn(f,'      end;');
      WriteLn(f,'    If W<>CheckSum then Halt(1)');
      WriteLn(f,' END;');
      Close(f)
   END.
