import matplotlib.pyplot as plt
import numpy as np
from property_service import PropertyService

propertyService = PropertyService()

listOfPropertiesForSaleLog = propertyService.fetchAllPropertyForSaleLog();
xpoints = np.array(list(map(lambda property: property.created, listOfPropertiesForSaleLog)))
ypoints = np.array(list(map(lambda property: property.no_properties, listOfPropertiesForSaleLog)))
plt.plot(xpoints, ypoints)
plt.xlabel("Date")
plt.ylabel("Number of properties for sale")
plt.title("Properties on Rightmove - Manchester")
plt.show()