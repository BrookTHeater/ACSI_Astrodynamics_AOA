# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:21:40 2023

@author: grant
"""

# Load GMAT into the Python environment
from load_gmat import *

# Load a force model used for the propagation
from GMATReentryScript import *

# Build the propagation container class 
pdprop = gmat.Construct("Propagator","PDProp")

# Create and assign a numerical integrator for use in the propagation
gator = gmat.Construct("PrinceDormand78", "Gator")
pdprop.SetReference(gator)

# Assign the force model imported from BasicFM
pdprop.SetReference(fm)

# Set some of the fields for the integration
pdprop.SetField("InitialStepSize", 60.0)
pdprop.SetField("Accuracy", 1.0e-12)
pdprop.SetField("MinStep", 0.0)

# Perform top level initialization
gmat.Initialize()

# Setup the spacecraft that is propagated
pdprop.AddPropObject(earthorb)
pdprop.PrepareInternals()

# Refresh the 'gator reference
gator = pdprop.GetPropagator()

# Take a 600 second steps for 1 day, showing the state before and after
time = 0.0
step = 60.0
#print(time, " sec, state = ", gator.GetState())

# Propagate for 1 day (via 144 10-minute steps)
#for x in range(144):
#   gator.Step(step)
#   time = time + step
#   print(time, " sec, state = ", gator.GetState())

# Define Results
results = []
import numpy as np 


i=0

while True: 

    gator.Step(step) 
    state = gator.GetState() #(r, v) 
    radius = np.linalg.norm(state[0:3]) #KM 
    i += 1 
    time = (i*step)/86400 #days 
    results.append([time, radius])
   

    if radius < 6578.1: 

        break 
    
    # Write time and radius data to file
    with open("outputs.txt", "a") as f:
        f.write("{:.6f}\t{:.6f}\n".format(time, radius))

print (time, radius)

print(f"The Natural Reentry Time for the spacecraft is {time:.2f} days")


