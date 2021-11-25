package PackageVehicles {

    // blocks
    part def Vehicle;
    part def Wheel;

    // a generic vehicle model
    part vehicle:Vehicle {
        part w:Wheel[4];
    }
}
