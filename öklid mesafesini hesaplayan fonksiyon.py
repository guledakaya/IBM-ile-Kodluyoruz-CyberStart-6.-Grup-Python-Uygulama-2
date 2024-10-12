import math

# Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 2D noktaları içeren 'points' listesi
points = [(1, 2), (4, 6), (5, 8), (9, 3)]

# Mesafeleri saklayacak liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print(f"Minimum mesafe: {min_distance}")
