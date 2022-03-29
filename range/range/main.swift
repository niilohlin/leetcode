//
//  main.swift
//  range
//
//  Created by Niil Öhlin on 2022-02-22.
//

class Pair {
    let value: Int
    var other: Pair!
    init(open: Int, close: Int) {
        self.value = open
        self.other = Pair(close: close)
        self.other.other = self
    }

    init(close: Int) {
        self.value = close
    }
}

class Solution {
    func removeCoveredIntervals(_ intervals: [[Int]]) -> Int {
        let sorted = intervals.sorted(by: { $0[0] < $1[0] })
        let pairs = sorted.map { Pair(open: $0[0], close: $0[1]) }

        let openClose: [Pair] = pairs.flatMap { open in
            [open, open.other]
        }

        let openCloseSorted = openClose.sorted(by: { $0.value < $1.value} )

        var stack = [Pair]()
        for pair in openCloseSorted {
            if stack.contains(where: { $0.other == pair })

            stack.append(pair)
        }

        return 0
    }
}


let s = Solution()
s.removeCoveredIntervals([[1,4],[3,6],[2,8]])
