module Lib
    ( someFunc
    ) where

import Data.List
import Data.List.Unique

someFunc :: IO ()
someFunc = putStrLn "someFunc"

-- | Given a integer n generate the list of all partitions.
type Partition = [[Int]]
partitions :: Int -> Partition
partitions 0 = [[]]
partitions n = [m:p | m <- [1..n], p <- partitions (n-m), (null p || m <= head p)]

-- | given two integers n and l generate all partitions of n and filter it to the partitions
  -- of length l
lengPartitions :: Int -> Int -> Partition
lengPartitions n l = filter (\x -> (length x) == l) $ partitions n

-- | n choose 2.
choose2 :: Int -> Int
choose2 n = ((n-1)*(n)) `div` 2

-- | Implements proposition 4.
prop04 :: [[Int]] -> Int -> Bool
prop04 xs x = (foldl (+) 0 $ map (choose2) $ foldl (++) [] xs) < choose2 x

-- | Calculates what elements in the list will be permuted.
elementsToPermute :: Int -> Int -> [Bool]
elementsToPermute len perm = notPermuting ++ permuting
  where
    notPermuting = take (len - perm) $ repeat False
    permuting    = take (perm) $ repeat True

getPermutations :: [Bool] -> [a] -> [[a]]
getPermutations ps xs = map (\x -> notPerms ++ x) perms
  where
    perms    = permutations $ map (\(x, y) -> y) $ filter (\(x, y) -> x) (zip ps xs)
    notPerms = map (\(x, y) -> y) $ filter (\(x, y) -> not x) (zip ps xs)

combPerm :: [a] -> Int -> [[a]]
combPerm xs n = unique $ foldl (++) [] $
                map (\x -> getPermutations x xs) $
                permutations $ elementsToPermute (length xs) n
