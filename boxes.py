import math

item_number = int(input ("Enter the number of items: "))
item_per_box = int(input ("Enter the number of items per box: "))

box_amount = item_number / item_per_box

total_boxes = math.ceil(box_amount)

print(f"For {item_number} items, packing {item_per_box} items in each box, you will need {total_boxes} boxes. ")