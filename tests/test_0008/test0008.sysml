package PackageVehicles {

    part def Vehicle;
    part def ChassisAssembly;
    part def RollBar;
    part def Wheel;
    part def LugBolt;
    part def Cylinder;
    part def Engine;

    part partnotype1;

    part vehicle:Vehicle {

        part partnotype2;

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
