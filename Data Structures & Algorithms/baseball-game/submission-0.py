class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = []
        for op in operations:
        #    print(f"{x} y {op}")
            match op:
                case '+':
                    x.append( int(x[-2]) + int(x[-1]))
                case 'D':
                    x.append( 2 * int(x[-1]) )
                case 'C':
                    x.pop()
                case _:
                    x.append(op)
        #    print(f"{x}")
        
        return sum([int(i) for i in x])