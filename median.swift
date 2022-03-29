

    func findMedianSortedArrays(_ nums1: [Int], _ nums2: [Int]) -> Double {
        var result = [Int]()
        let len = nums1.count + nums2.count
        let mid = len / 2
        var lhs = nums1
        var rhs = nums2

        while let l = lhs.first, let r = rhs.first, result.count <= mid + 1 {

            if l < r {
                result.append(l)
                _ = lhs.removeFirst()
            } else {
                result.append(r)
                _ = rhs.removeFirst()
            }
        }
        result.append(contentsOf: lhs)
        result.append(contentsOf: rhs)

        if len % 2 == 1 {
            return Double(result[mid])
        }
        return Double(result[mid] + result[mid - 1]) / 2.0

    }

let first = [1, 2]
let second = [3, 4]

print("\(findMedianSortedArrays(first, second))")
