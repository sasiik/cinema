# for 1 side: left or right
def create_iteration(rows_count=7, places_count=7):
    return({"rows_per_side": range(1, rows_count+1), "seats_per_row": range(1, places_count+1)})