# KerbalSatelliteNetwork
 KerbalSatelliteNetwork helps you put satellites in the proper final and transfer orbits for a satellite network around a body in Kerbal Space Program.
 KerbalSatelliteNetwork.py currently provides the periods, periapses, apoapses, and semi-major axes of the initial and transfer orbits. Delta-V totals will come in future.
 Documentation of how to use it properly will come soon. Very roughly, start in the transfer orbit, wait until you reach periapsis, detach a satellite, and burn that satellite's engines so that it is in the final orbit. Repeat this until you've detached your desired number of satellites. After you've completed that, ensure that the periods of each satellite are equal.

dvcalc.py is a simple Delta-V calculator that I've included since I didn't know where else to put it. You may find it useful, it's better than calculating Delta-V by hand (although you can also see Delta-V in-game if you'd like).