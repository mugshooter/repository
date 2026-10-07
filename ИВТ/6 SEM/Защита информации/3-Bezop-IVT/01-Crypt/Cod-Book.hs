   -- Демонстрация реализации шифрования и дешифрования
   -- "по книге".
   --
   -- Автор: Швецкий М.В. (07.11.2020)
   -- ********************************
   len = length ['a'..'z']
   lst = ['a'..'z']

   -- ***************************************
   -- Функция возвращает результат шифрования
   -- текста txt по "книге" key
   -----------------------------------
   code txt key = map (\x -> lst !! x) 
                      (res txt key)
   --------------------------------
   res txt key 
         = map (\(a,b) -> (col a lst 0 + col b lst 0) `mod` len)              
               (zip txt key)

   -- *****************************************
   -- Функция возвращает результат дешифрования
   -- кода txt по "книге" key
   -------------------------------------
   deCode txt key = map (\x -> lst !! x) 
                        (res_Dec txt key)
   --------------------------------------
   res_Dec txt key 
         = map (\(a,b) -> (col a lst 0 - col b lst 0) `mod` len)              
               (zip txt key)

   -- ***********************************************
   -- Функция возвращает номер элемента x в  непустом
   -- списке lst; при обращении к функции k=0 или k=1
   --------------------------------------------------
   col x lst k | head lst==x = k
               | True        = col x (tail lst) (k+1)

   -- ***************************
   -- Неудачные тестовые примеры:
   ------------------------------------
   test1 = code "asdfasdfa" "zxczxczxc"
   test2 = code "aaaaaaaa"  "bbbbbbbb"
   -----------------------------------
   test3 = deCode test1 "zxczxczxc"
   test4 = deCode test2 "bbbbbbbb"
   ----------------------------------------
   test5 = deCode (code txt key) key == txt
      where txt = concatMap (replicate 1000) "adgdfgsdfgs"
            key = concatMap (replicate 1000) "zxczxczxcqw"
                                                                