import UIKit

var greeting = "Hello, playground"

protocol Valuable {
    var value: Int { get }
}

class Open: Valuable {
    let value: Int
    let close: Close
    init(open: Int, close: Int) {
        self.value = open
        self.close = Close(close: close)
        self.close.open = self
    }
}

class Close: Valuable {
    let value: Int
    var open: Open!
    init(close: Int) {
        self.value = close
    }
}

class Solution {
    func removeCoveredIntervals(_ intervals: [[Int]]) -> Int {
        let sorted = intervals.sorted(by: { $0[0] < $1[0] })
        let opens = sorted.map { Open(open: $0[0], close: $0[1]) }

        let openClose: [Valuable] = opens.flatMap { open in
            [open, open.close]
        }

        let openCloseSorted = openClose.sorted(by: { $0.value < $1.value} )

        for valueable in openCloseSorted {
            
        }

        return 0
    }
}


let s = Solution()
s.removeCoveredIntervals([[1,4],[3,6],[2,8]])
