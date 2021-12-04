package PackageVehicles {

    part def Vehicle;
    part def Wheel;
    part vehicle_shed;

    part vehicle_repair_shop {
        part def VehicleLift;
    }

    part vehicle:Vehicle {
        part w:Wheel[4];
    }
}
