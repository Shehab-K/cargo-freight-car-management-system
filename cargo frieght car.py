class container:
    def __init__(self, id, weight, station_instance):
        self.id = id
        self.weight = weight
        self.station_instance = station_instance

    def id_of_container(self):
        return self.id

    def weight_of_container(self):
        return self.weight

    def consumption(self):
        return 0.0

    def gettype(self):
        return "general"

    def check_type(self, other):
        if type(self.id) == type(other.id) and type(self.weight) == type(other.weight):
            return "True"
        else:
            return "false"

    def append_data_to_list(self):
        self.station_instance.containers.append(self)

    def print_list(self):
        return self.station_instance.containers


class normal_container(container):
    def __init__(self, id, weight, station_instance):
        super().__init__(id, weight, station_instance)

    def gettype(self):
        if self.weight <= 3000:
            return "normal container"
        return "heavy container"

    def consumption(self):
        if self.weight <= 3000:
            return 2.50 * self.weight
        return 0.0

    def append_data_to_list(self):
        self.station_instance.containers.append(self)


class heavy_container(container):
    def __init__(self, id, weight, station_instance):
        super().__init__(id, weight, station_instance)

    def gettype(self):
        if self.weight > 3000:
            return "heavy container"
        return "normal container"

    def consumption(self):
        if self.weight > 3000:
            return 3.00 * self.weight
        return 0.0

    def append_data_to_list(self):
        self.station_instance.containers.append(self)


class Refrigerated_container(heavy_container):
    def __init__(self, id, weight, Type, station_instance):
        super().__init__(id, weight, station_instance)
        self.type = Type

    def gettype(self):
        if self.type in ["R", "r"]:
            return "Refrigerated container"
        return "heavy container"

    def consumption(self):
        if self.type in ["R", "r"]:
            return 5.00 * self.weight
        return 0.0

    def append_data_to_list(self):
        self.station_instance.containers.append(self)


class liquid_container(heavy_container):
    def __init__(self, id, weight, Type, station_instance):
        super().__init__(id, weight, station_instance)
        self.type = Type

    def gettype(self):
        if self.type in ["L", "l"]:
            return "liquid container"
        return "heavy container"

    def consumption(self):
        if self.type in ["L", "l"]:
            return 4.00 * self.weight
        return 0.0

    def append_data_to_list(self):
        self.station_instance.containers.append(self)


class station:
    def __init__(self, station_id, x, y):
        self.station_id = station_id
        self.x = x
        self.y = y
        self.containers = []
        self.current_car = []
        self.car_history = []

    def id_of_station(self):
        return self.station_id

    def postion_x(self):
        return self.x

    def postion_y(self):
        return self.y

    def distance(self, other):
        return float(((other.x - self.x) ** 2 + (other.y - self.y) ** 2) ** 0.5)


class freight_car:
    def __init__(
        self,
        p,
        carid,
        current,
        fuelConsumptionPerKM,
        maxNumberOfAllContainers,
        maxNumberOfHeavyContainers,
        maxNumberOfRefrigeratedContainers,
        maxNumberOfLiquidContainers,
    ):
        self.id = carid
        self.fuel = 0
        self.current = current
        self.currentStation = p
        self.loadedcontainers = []
        self.maxNumberOfAllContainers = maxNumberOfAllContainers
        self.maxNumberOfHeavyContainers = maxNumberOfHeavyContainers
        self.maxNumberOfRefrigeratedContainers = maxNumberOfRefrigeratedContainers
        self.maxNumberOfLiquidContainers = maxNumberOfLiquidContainers
        self.currentnumberofcontainers = 0
        self.currentheavycontainer = 0
        self.currentliquidcontainer = 0
        self.currentnormalcontainer = 0
        self.currentrefrigeratedcontainer = 0
        self.fuelConsumptionPerKM = fuelConsumptionPerKM

    def car_id(self):
        return self.id

    def current(self):
        self.current.current_car.append(self)

    def getCurrentContainers(self):
        return sorted(self.loadedcontainers, key=lambda cont: cont.id)

    def load(self, container):
        if isinstance(container, normal_container):
            if (
                len(
                    [c for c in self.loadedcontainers if isinstance(c, heavy_container)]
                )
                >= self.maxNumberOfHeavyContainers
            ):
                print(
                    f"the Car {self.car_id()} is already at its maximum capacity for containers."
                )
                return False
            else:
                self.currentnormalcontainer += 1
                self.currentnumberofcontainers += 1
                self.loadedcontainers.append(container)
                self.current.containers.append(container)
                return True
        elif isinstance(container, heavy_container):
            if container.weight > 3000:
                if isinstance(container, Refrigerated_container):
                    if (
                        len(
                            [
                                c
                                for c in self.loadedcontainers
                                if isinstance(c, Refrigerated_container)
                            ]
                        )
                        >= self.maxNumberOfRefrigeratedContainers
                    ):
                        print(
                            f"the Car {self.car_id()} is already at its maximum capacity for containers."
                        )
                        return False
                    else:
                        self.currentrefrigeratedcontainer += 1
                        self.currentnumberofcontainers += 1
                        self.loadedcontainers.append(container)
                        self.current.containers.append(container)
                        return True
                elif isinstance(container, liquid_container):
                    if (
                        len(
                            [
                                c
                                for c in self.loadedcontainers
                                if isinstance(c, liquid_container)
                            ]
                        )
                        >= self.maxNumberOfLiquidContainers
                    ):
                        print(
                            f"the Car {self.car_id()} is already at its maximum capacity for containers."
                        )
                        return False
                    else:
                        self.currentliquidcontainer += 1
                        self.currentnumberofcontainers += 1
                        self.loadedcontainers.append(container)
                        self.current.containers.append(container)
                        return True
                else:
                    if (
                        len(
                            [
                                c
                                for c in self.loadedcontainers
                                if isinstance(c, heavy_container)
                            ]
                        )
                        >= self.maxNumberOfHeavyContainers
                    ):
                        print(
                            f"the Car {self.car_id()} is already at its maximum capacity for containers."
                        )
                        return False
                    else:
                        self.currentheavycontainer += 1
                        self.currentnumberofcontainers += 1
                        self.loadedcontainers.append(container)
                        self.current.containers.append(container)
                        return True

    def unload(self, container):
        if container in self.loadedcontainers:
            if isinstance(container, normal_container):
                self.currentnormalcontainer -= 1
                self.currentnumberofcontainers -= 1
                self.loadedcontainers.remove(container)
                self.current.containers.remove(container)
                return True
            elif isinstance(container, heavy_container):
                if container.weight > 3000:
                    if isinstance(container, Refrigerated_container):
                        self.currentrefrigeratedcontainer -= 1
                        self.currentnumberofcontainers -= 1
                        self.loadedcontainers.remove(container)
                        self.current.containers.remove(container)
                        return True
                    elif isinstance(container, liquid_container):
                        self.currentliquidcontainer -= 1
                        self.currentnumberofcontainers -= 1
                        self.loadedcontainers.remove(container)
                        self.current.containers.remove(container)
                        return True
                    else:
                        self.currentheavycontainer -= 1
                        self.currentnumberofcontainers -= 1
                        self.loadedcontainers.remove(container)
                        self.current.containers.remove(container)
                        return True

        else:
            print("Error: Container not found")

    def calculateFuelConsumption(self):
        fuelConsumption = 0
        for container in self.loadedcontainers:
            fuelConsumption += container.consumption()
        if self.currentStation.car_history:
            fuelConsumption += self.fuelConsumptionPerKM * self.currentStation.distance(
                self.currentStation.car_history[-1]
            )
        return fuelConsumption

    def move(self, destination):
        fuelConsumption = self.calculateFuelConsumption()
        if fuelConsumption <= self.fuel:
            self.fuel -= fuelConsumption
            try:
                self.currentStation.current_car.remove(self)
            except ValueError:
                pass
            self.currentStation.car_history.append(self)
            destination.current_car.append(self)
            self.currentStation = destination
            return True
        else:
            return False

    def refuel(self, amount):
        self.fuel += amount


class Main:
    def __init__(self):
        print("--stations--")
        station1 = station(1, 30, 60)
        print(
            "station",
            station1.id_of_station(),
            "(",
            station1.postion_x(),
            ",",
            station1.postion_y(),
            ")",
        )

        station2 = station(2, 50, 70)
        print(
            "station",
            station2.id_of_station(),
            "(",
            station2.postion_x(),
            ",",
            station2.postion_y(),
            ")",
        )

        # containers
        print(" ")
        print("--containers--")
        container1 = normal_container(1, 2000, station1)
        print(
            "container",
            container1.id,
            "(",
            "container weight",
            container1.weight_of_container(),
            ",",
            "container ID:",
            container1.id_of_container(),
            ",",
            "container type:",
            container1.gettype(),
            ")",
        )

        container2 = heavy_container(2, 3500, station1)
        print(
            "container",
            container2.id,
            "(",
            "container weight",
            container2.weight_of_container(),
            ",",
            "container ID:",
            container2.id_of_container(),
            ",",
            "container type:",
            container2.gettype(),
            ")",
        )

        container3 = Refrigerated_container(3, 4000, "R", station1)
        print(
            "container",
            container3.id,
            "(",
            "container weight",
            container3.weight_of_container(),
            ",",
            "container ID:",
            container3.id_of_container(),
            ",",
            "container type:",
            container3.gettype(),
            ")",
        )

        container4 = liquid_container(4, 5000, "L", station1)
        print(
            "container",
            container4.id,
            "(",
            "container weight",
            container4.weight_of_container(),
            ",",
            "container ID:",
            container4.id_of_container(),
            ",",
            "container type:",
            container4.gettype(),
            ")",
        )

        # cars
        print(" ")
        print("--cars--")
        car1 = freight_car(station1, 101, station1, 5, 3, 2, 1, 1)
        print("car", car1.id, ":", "(", "car ID:", car1.car_id(), ")")

        car2 = freight_car(station2, 102, station2, 6, 4, 3, 2, 1)
        print("car", car2.id, ":", "(", "car ID:", car2.car_id(), ")")

        print("the distance between the two stations:", station1.distance(station2))

        # load container 1 to car 1
        car1.load(container1)
        print("---load container 1 to car 1---")
        print("current number of containers: ", car1.currentnumberofcontainers)
        print("current number of normal container:", car1.currentnormalcontainer)
        print("current number of heavy containers: ", car1.currentheavycontainer)
        print("current number of liquid containers: ", car1.currentliquidcontainer)
        print(
            "current number of refrigerated containers: ",
            car1.currentrefrigeratedcontainer,
        )

        # load container 2 to car 1
        car1.load(container2)
        print("---load container 2 to car 1---")
        print("current number of containers: ", car1.currentnumberofcontainers)
        print("current number of normal container:", car1.currentnormalcontainer)
        print("current number of heavy containers: ", car1.currentheavycontainer)
        print("current number of liquid containers: ", car1.currentliquidcontainer)
        print(
            "current number of refrigerated containers: ",
            car1.currentrefrigeratedcontainer,
        )

        # load container 3 to car 1
        car1.load(container3)
        print("---load container 3 to car 1---")
        print("current number of containers: ", car1.currentnumberofcontainers)
        print("current number of normal container:", car1.currentnormalcontainer)
        print("current number of heavy containers: ", car1.currentheavycontainer)
        print("current number of liquid containers: ", car1.currentliquidcontainer)
        print(
            "current number of refrigerated containers: ",
            car1.currentrefrigeratedcontainer,
        )

        print(" ")
        print("---loaded containers in car 1---")
        for container in car1.loadedcontainers:
            print(
                container.gettype(),
                ":",
                "(",
                "container ID:",
                container.id,
                ",",
                "container weight:",
                container.weight,
                ")",
            )

        print(" ")
        print("---move car1 from station 1 to station2---")
        car1.move(station2)
        print("current station ID of the car:", car1.currentStation.station_id)
        print("fuel of the car: ", car1.fuel)
        print("car consumption: ", car1.calculateFuelConsumption())
        car1.refuel(100)
        print("fuel of the car after the refuel: ", car1.fuel)

        # unload container 1 from car 1
        print("---unload container 1 from car 1---")
        car1.unload(container1)
        print("current number of containers: ", car1.currentnumberofcontainers)
        print("current number of normal container:", car1.currentnormalcontainer)
        print("current number of heavy containers: ", car1.currentheavycontainer)
        print("current number of liquid containers: ", car1.currentliquidcontainer)
        print(
            "current number of refrigerated containers: ",
            car1.currentrefrigeratedcontainer,
        )

        # unload container 2 from car 1
        print("---unload container 2 from car 1---")
        car1.unload(container2)
        print("current number of containers: ", car1.currentnumberofcontainers)
        print("current number of normal container:", car1.currentnormalcontainer)
        print("current number of heavy containers: ", car1.currentheavycontainer)
        print("current number of liquid containers: ", car1.currentliquidcontainer)
        print(
            "current number of refrigerated containers: ",
            car1.currentrefrigeratedcontainer,
        )

        print(" ")
        print("---loaded containers in car 1---")
        for container in car1.loadedcontainers:
            print(
                container.gettype(),
                ":",
                "(",
                "container ID:",
                container.id,
                ",",
                "container weight:",
                container.weight,
                ")",
            )

        print("---End of scenario 1---")


if __name__ == "__main__":
    main = Main()
