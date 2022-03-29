//
//  main.swift
//  combinationSum
//
//  Created by Niil Öhlin on 2022-02-17.
//
class Solution {

//    func combinationSumRecur(_ candidates: [Int], _ target: Int) -> Set<Int> {
//        if candidates.isEmpty {
//            return []
//        }
//        if candidates.count == 1 && candidates[0] == target {
//            return [candidates[0]]
//        }
//
//
//    }

    func combinationSum(_ candidates: [Int], _ target: Int) -> [[Int]] {
        if target < 0 {
            return []
        }
        if candidates.count == 1 && candidates[0] == target{
            return [candidates]
        }


        let newTargets: [Int] = candidates.compactMap { candidate in
            let newTarget = target - candidate
            if newTarget > 0 {
                return newTarget
            }
            return nil
        }
        return newTargets.flatMap { newTarget in
            combinationSum(candidates, newTarget).map { comb in
                comb + [newTarget - target]
            }
        }
    }
}

//let s = Solution()

//print(s.combinationSum([2,3, 6, 7], 7))

class Solution2 {
    func removeKdigits(_ num: String, _ k: Int) -> String {
        var largest = [String]()

    }
}
// 15235
