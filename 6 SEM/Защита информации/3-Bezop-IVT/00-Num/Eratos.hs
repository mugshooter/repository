   import List
   -- ******************************
   primesTo n = eratos [2..n]  where
      eratos []     = []
      eratos (p:xs) = p : eratos (xs `minus` [p*p, p*p+p..n])
   ----------------------------------------------------------
   minus (x:xs) (y:ys) = case (compare x y) of 
      LT -> x : minus  xs (y:ys)
      EQ ->     minus  xs    ys
      GT ->     minus (x:xs) ys
   minus  xs     _     = xs

   -- ***********************
   -- Вариация по типу Эйлера
   -----------------------------------
   primesToEU n = eulers [2..n]  where
      eulers []     = []
      eulers (p:xs) = p : eulers (xs `minus` takeWhile (<= n)
                                                       (map (p*) (p:xs)))
   -- eratos (p:xs) = p : eratos (xs `minus` takeWhile (<= n)
   --                                                  (map (p*) [p..] ))
   --                                               -- [p*p, p*p+p..n]
   -- **********************
   -- Неограниченное решето:
   -- (1) с немедленным отсеиванием (медленно)
   -------------------------------------------
   primesE = sieve [2..]
        where sieve (p:xs) = p : sieve (minus xs [p,p+p..])
   -----------------------------------------------------------
   -- (2) с отложенным отсеиванием, от квадратов простых чисел
   --     (гораздо быстрее)
   -------------------------------------
   primesEQ = 2 : sieve [3..] 4 primesEQ
        where sieve (x:xs) q (p:t)
               | x < q     = x : sieve xs q (p:t)
               | otherwise = sieve (minus xs [q,q+p..]) (head t^2) t
   -----------------------------------------------------------------
   -- (3) с комбинированным решетом (R.Bird):
   ---------------------------------------------
   primesB = 2 : minus [3..] 
                       (foldr (\p r -> (p*p) : union' [p*p+p,p*p+2*p..] r) 
                              [] 
                              primesB)
   --------------------------------------------
   union' (x:xs) (y:ys) = case (compare x y) of 
                           LT -> x : union  xs (y:ys)
                           EQ -> x : union  xs    ys
                           GT -> y : union (x:xs) ys

