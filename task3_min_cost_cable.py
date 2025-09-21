import heapq

def smart_cable_combiner(cables):
    if not cables:
        return 0

    heapq.heapify(cables) 
    total_cost = 0

    while len(cables) > 1:
        
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        cost = first + second
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost
# Приклад
cables = [5, 3, 2, 4] # 2+3=5, 5+4=9, 5+9=14, всього 5+9+14= 28
result = smart_cable_combiner(cables)
print("Мінімальні витрати на з'єднання:", result)