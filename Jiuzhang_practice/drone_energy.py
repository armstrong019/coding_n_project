# Drone Flight Planner
#
# You’re an engineer at a disruptive drone delivery startup and your CTO asks you to come up with an efficient algorithm
# that calculates the minimum amount of energy required for the company’s drone to complete its flight. You know that the drone burns 1 kWh
# (kilowatt-hour is an energy unit) for every mile it ascends,
# and it gains 1 kWh for every mile it descends. Flying sideways neither burns nor adds any energy.
#
# Given an array route of 3D points, implement a function calcDroneMinEnergy that computes and returns the minimal amount of energy
# the drone would need to complete its route. Assume that the drone starts its flight at the first point in route. That is, no energy was expended to place the drone at the starting point.
#
# For simplicity, every 3D point will be represented as an integer array whose length is 3. Also, the values at indexes 0, 1,
# and 2 represent the x, y and z coordinates in a 3D point, respectively.
#

def calc_drone_min_energy(route):
    if not route:
        return 0
    if len(route) == 1:
        return 0
    array = []
    for i in range(1, len(route)):
        array.append(route[i][2] - route[i - 1][2])

    max_eng = 0
    cum_sum = 0 # 这里面注意 比较永远都是从第一位开始比较， 在这个case 初始值为0
    for j in range(len(array))：
        cum_sum += array[j]
        if cum_sum >= max_eng:
            max_eng = cum_sum
    return max_eng
