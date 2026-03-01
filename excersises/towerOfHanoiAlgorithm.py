def hanoi_solver(n):
    spot_A = [num for num in reversed(range(1, n + 1 ))]
    spot_B = []
    spot_C = []
    initial_state = f"{spot_A} {spot_B} {spot_C}\n"
    result_string = ""
    result_string += initial_state
    
    def move(n, source, auxiliary, target):
        nonlocal result_string
        if n == 1:
            target.append(source.pop())            
            result_string += f"{spot_A} {spot_B} {spot_C}\n"
        else:
            move(n-1, source, target, auxiliary)
            target.append(source.pop())            
            result_string += f"{spot_A} {spot_B} {spot_C}\n"
            move(n-1, auxiliary, source, target)
    move(n, spot_A, spot_B, spot_C)
    return result_string.rstrip("\n")
    
print(hanoi_solver(2))
