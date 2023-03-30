# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 16:16:56 2023

@author: grant
"""

# Load GMAT into memory
from load_gmat import *
gmat.Clear()

# Spacecraft configuration preliminaries
earthorb = gmat.Construct("Spacecraft", "EarthOrbiter")
earthorb.SetField("DateFormat", "UTCGregorian")
earthorb.SetField("Epoch", "20 Jul 2020 12:00:00.000")

earthorb.SetField("CoordinateSystem", "EarthMJ2000Eq")
earthorb.SetField("DisplayStateType", "Keplerian")

# with open('inputs.txt', 'r') as f:
#     for line in f:
#         line = line.strip().split(':')
#         param = line[0].strip()
#         value = line[1].strip()

#         if param == 'SMA':
#             earthorb.SetField(param, float(value))
#         elif param == 'ECC':
#             earthorb.SetField(param, float(value))
#         elif param == 'INC':
#             earthorb.SetField(param, float(value))
#         elif param == 'RAAN':
#             earthorb.SetField(param, float(value))
#         elif param == 'AOP':
#             earthorb.SetField(param, float(value))
#         elif param == 'TA':
#             earthorb.SetField(param, float(value))
#         elif param == 'SRPArea':
#             earthorb.SetField(param, float(value))
#         elif param == 'Cr':
#             earthorb.SetField(param, float(value))
#         elif param == 'DryMass':
#             earthorb.SetField(param, float(value))



#Orbital state
earthorb.SetField("SMA", 6900)
earthorb.SetField("ECC", 0.005)
earthorb.SetField("INC", 78)
earthorb.SetField("RAAN", 45)
earthorb.SetField("AOP", 90)
earthorb.SetField("TA", 180)

#Spacecraft ballistic properties for the SRP model
earthorb.SetField("SRPArea", 2.5)
earthorb.SetField("Cr", 1.8)
earthorb.SetField("DryMass", 80)

# ODE Model settings
fm = gmat.Construct("ForceModel", "FM")
fm.SetField("CentralBody", "Earth")

# The 8x8 JGM-3 Gravity Model
earthgrav = gmat.Construct("GravityField", "Earth8x8")
earthgrav.SetField("BodyName","Earth")
earthgrav.SetField("PotentialFile","../data/gravity/earth/JGM3.cof")
earthgrav.SetField("Degree",8)
earthgrav.SetField("Order",8)

# The Point Masses
moongrav = gmat.Construct("PointMassForce", "MoonGrav")
moongrav.SetField("BodyName","Luna")
sungrav = gmat.Construct("PointMassForce", "SunGrav")
sungrav.SetField("BodyName","Sun")

# Drag using Jacchia-Roberts
jrdrag = gmat.Construct("DragForce", "JRDrag")
jrdrag.SetField("AtmosphereModel","JacchiaRoberts")

# Build and set the atmosphere for the model
atmos = gmat.Construct("JacchiaRoberts", "Atmos")
jrdrag.SetReference(atmos)

# Solar Radiation Pressure
srp = gmat.Construct("SolarRadiationPressure", "SRP")


# Add all of the forces into the ODEModel container
fm.AddForce(earthgrav)
fm.AddForce(moongrav)
fm.AddForce(sungrav)
fm.AddForce(srp)

# Note that the drag force is commented out because of a bug in the drag models 
# when the A-Matrix is computed.  Builds that have issue GMT-6950 resolved can 
# use the A-Matrix and drag together.
fm.AddForce(jrdrag)

# Setup the state vector used for the force
psm = gmat.PropagationStateManager()
psm.SetObject(earthorb)

# Include the orbital A-matrix
psm.SetProperty("AMatrix")

psm.BuildState()

fm.SetPropStateManager(psm)
fm.SetState(psm.GetState())

# Assemble all of the objects together 
gmat.Initialize()
