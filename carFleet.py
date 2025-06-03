class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleetNum=0
        lastTime=0
        # The zip() function pairs up elements from multiple iterables (like lists) by their index.
        cars = sorted(zip(position, speed), reverse=True)
    #zip car (speed, position) then sorts
        for position, speed in cars:
            time = (target - position)/speed
            if(time > lastTime):
                fleetNum += 1
                lastTime = time

        return fleetNum