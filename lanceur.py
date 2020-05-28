import os
import time
import matplotlib.pyplot as plt 


#######################################################################
################### Test points  différent arcs fixe ##################
#######################################################################

# Test avec 250 points et 100 arcs
print("")
print("########################################")
print("")
print("Chemin de 250 points & 100 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 250 100')
time1 = (time.time() - start_time)
print("--- %s seconds ---" % time1)

# Test avec 500 points et 100 arcs
print("")
print("########################################")
print("")
print("Chemin de 500 points & 100 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 500 100')
time2 = (time.time() - start_time)
print("--- %s seconds ---" % time2)

# Test avec 1000 points et 100 arcs
print("")
print("########################################")
print("")
print("Chemin de 1000 points & 100 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 1000 100')
time3 = (time.time() - start_time)
print("--- %s seconds ---" % time3)

# Test avec 1500 points et 100 arcs
print("")
print("########################################")
print("")
print("Chemin de 1500 points & 100 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 1500 100')
time4 = (time.time() - start_time)
print("--- %s seconds ---" % time4)

# Test avec 2000 points et 100 arcs
print("")
print("########################################")
print("")
print("Chemin de 2000 points & 100 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 2000 100')
time5 = (time.time() - start_time)
print("--- %s seconds ---" % time5)

  
x = [250, 500, 1000, 1500, 2000] 
y = [time1, time2, time3, time4, time5] 
plt.plot(y, x, marker='o', markerfacecolor='blue', markersize=12) 
# plt.plot(y, x) 
plt.xlabel('Y - secondes') 
plt.ylabel('X - nombre de points') 
plt.title('Nombre de points différents et nombre de sommet fixe : 100') 
plt.show() 

#######################################################################
############### Test points fixes et arcs différents ###############
#######################################################################

os.system('cls' if os.name == 'nt' else 'clear')

# Test avec 1000 points et 100 arcs
print("")
print("########################################")
print("")
print("Chemin de 1000 points & 100 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 1000 100')
time1 = (time.time() - start_time)
print("--- %s seconds ---" % time1)

# Test avec 1000 points et 250 arcs
print("")
print("########################################")
print("")
print("Chemin de 1000 points & 250 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 1000 250')
time2 = (time.time() - start_time)
print("--- %s seconds ---" % time2)

# Test avec 1000 points et 500 arcs
print("")
print("########################################")
print("")
print("Chemin de 1000 points & 500 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 1000 500')
time3 = (time.time() - start_time)
print("--- %s seconds ---" % time3)

# Test avec 1000 points et 750 arcs
print("")
print("########################################")
print("")
print("Chemin de 1000 points & 750 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 1000 750')
time4 = (time.time() - start_time)
print("--- %s seconds ---" % time4)

# Test avec 1000 points et 100 arcs
print("")
print("########################################")
print("")
print("Chemin de 1000 points & 1000 arcs ")
print("")
start_time = time.time()
os.system('py dijkstraResolver.py 1000 1000')
time5 = (time.time() - start_time)
print("--- %s seconds ---" % time5)


x = [100, 250, 500, 750, 1000] 
y = [time1, time2, time3, time4, time5] 
  
# plt.plot(y, x) 
plt.plot(y, x, marker='o', markerfacecolor='blue', markersize=12) 
plt.xlabel('Y - secondes') 
plt.ylabel('X - nombre de points') 
plt.title('Nombre de points différents et nombre de sommet fixe : 1000') 
  
# function to show the plot 
plt.show() 