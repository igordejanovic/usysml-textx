package PackageVehicles {

    // define blocks
    part def Vehicle;
    part def ChassisAssembly;
    part def RollBar;
    part def Wheel;
    part def LugBolt;
    part def Cylinder;
    part def Engine;

   // define a generic vehicle model
    part vehicle:Vehicle {
        part chs:ChassisAssembly {
            part rb:RollBar[0..1];
            part w:Wheel[4] {
                part lb:LugBolt[6..10];
            }
        }
        part eng:Engine {
            part cyl:Cylinder[4..8];
        }
    }
}
