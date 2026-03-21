def calculate_cost(X, T):

    if X <= 0 or (T != 1 and T != 2):
        raise ValueError("Invalid")
    
    if T == 1:  # Xe máy Xanh SM Bike
        if X <= 2:
            return X * 13200
        else:
            return 2 * 13200 + (X - 2) * 4200
    elif T == 2:  # Ô tô Xanh SM Taxi
        if X <= 2:
            return X * 30500
        elif X <= 12:
            return 2 * 30500 + (X - 2) * 15500
        else:
            return 2 * 30500 + 10 * 15500 + (X - 12) * 13800
    else:
        raise ValueError("Invalid")
