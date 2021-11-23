package PackageVehicles {

    // blocks
    part def Vehicle;
    part def Wheel;

    // a generic vehicle model
    part vehicle:Vehicle {
        part def Wheel;  // generates textX error
        part w:Wheel[4]; // w should be of the type 'vehicle.Wheel'
    }
}
